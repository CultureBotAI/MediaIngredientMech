"""Authorized seven-issue updates; exact bodies, live dedup, no retry/closure."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess

T = Path(__file__).resolve().parent
REPO = "repos/CultureBotAI/MediaIngredientMech"
PLAN_SHA = "0fb7e73a2dbc435bb031fb7bb4014c9b1cb3097167e9a490cae3521f4f554e59"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def main():
    plan_raw = (T / "publication-plan.json").read_bytes()
    require(sha(plan_raw) == PLAN_SHA, "publication plan changed")
    plan = json.loads(plan_raw)
    require(plan["issues"] == [1122, 1123, 1124, 1125, 1126, 901, 1117], "issue scope changed")
    require([x["issue"] for x in plan["files"]] == plan["issues"], "body scope changed")
    for entry in plan["files"]:
        body = (T / entry["body_path"]).read_bytes()
        request = (T / entry["request_path"]).read_bytes()
        require(sha(body) == entry["body_sha256"] and sha(request) == entry["request_sha256"], "body bytes changed")
        require(json.loads(request) == {"body": body.decode()}, "request differs from body file")
        require("@" not in body.decode() and "PR_LINK_PENDING" not in body.decode(), "mention or unresolved PR")
    with (T / "publication-results.json").open("x") as summary, (T / "publication-trace.jsonl").open("x") as trace:
        state = {"state": "running", "plan_sha256": PLAN_SHA, "operator_sha256": sha(Path(__file__).read_bytes()), "pr": 1128, "head": plan["head"], "comments": [], "no_closures": True}

        def save():
            summary.seek(0)
            summary.truncate()
            json.dump(state, summary, indent=2)
            summary.write("\n")
            summary.flush()

        def api(name, method, endpoint, request=None, paged=False):
            command = ["gh", "api", "--method", method, endpoint]
            if request:
                command += ["--input", str(T / request)]
            if paged:
                command += ["--paginate", "--slurp"]
            event = {"name": name, "argv": command, "started_at": datetime.datetime.now(datetime.timezone.utc).isoformat()}
            trace.write(json.dumps(event) + "\n")
            trace.flush()
            process = subprocess.run(command, capture_output=True)
            with (T / (name + ".json")).open("xb") as output:
                output.write(process.stdout)
            with (T / (name + ".stderr")).open("xb") as output:
                output.write(process.stderr)
            event.update(exit_code=process.returncode, finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat(), response_sha256=sha(process.stdout), stderr_sha256=sha(process.stderr))
            trace.write(json.dumps(event) + "\n")
            trace.flush()
            require(process.returncode == 0, "API failed; stop without retry: " + name)
            return json.loads(process.stdout)

        save()
        try:
            pr = api("pr1128-immediate-preflight", "GET", REPO + "/pulls/1128")
            require(pr["state"] == "open" and not pr["merged"] and pr["head"]["sha"] == plan["head"], "PR publication head/state changed")
            for entry in plan["files"]:
                issue = entry["issue"]
                body = (T / entry["body_path"]).read_text()
                require(sha(body.encode()) == entry["body_sha256"], "body changed before publication")
                pages = api(f"issue-{issue}-comments-immediate", "GET", f"{REPO}/issues/{issue}/comments?per_page=100", paged=True)
                comments = [comment for page in pages for comment in page]
                matches = [comment for comment in comments if comment["body"] == body or entry["marker"] in comment["body"]]
                require(len(matches) <= 1, "multiple existing update markers")
                if matches:
                    posted = matches[0]
                    require(posted["body"] == body, "existing marker has different bytes; do not duplicate or edit")
                    action = "retained_identical_existing"
                else:
                    posted = api(f"issue-{issue}-post-response", "POST", f"{REPO}/issues/{issue}/comments", request=entry["request_path"])
                    action = "posted_once"
                require(posted["body"] == body, "server body differs")
                require(posted["issue_url"].endswith("/issues/" + str(issue)), "wrong issue response")
                readback = api(f"issue-{issue}-readback", "GET", f"{REPO}/issues/comments/{posted['id']}")
                require(readback["body"] == body and readback["html_url"] == posted["html_url"], "readback differs")
                result = {"issue": issue, "action": action, "comment_id": posted["id"], "url": posted["html_url"], "body_sha256": entry["body_sha256"], "readback_sha256": sha((T / f"issue-{issue}-readback.json").read_bytes())}
                state["comments"].append(result)
                save()
                print(json.dumps(result), flush=True)
            state.update(state="complete", completed_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
            save()
        except Exception as error:
            state.update(state="failed", error=str(error), stop="No automatic retry. Preserve prior successes and raw responses.")
            save()
            raise


if __name__ == "__main__":
    main()
