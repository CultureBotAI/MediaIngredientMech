# Native content construction stopped before save

Native inspect succeeded. The content builder then raised ValueError for the genuine retained source access timestamp `2026-11-08 05:58:54 UTC` in I1201-MEDIA-CMRL-PRODUCT-HISTORY. No native bundle was saved. The error was observed in the tool transcript; no separate raw stderr capture was created for that builder invocation.

The formatter now accepts that explicit UTC form and renders the same instant as ISO UTC. No evidence timestamp or capture bytes are changed. Because the builder script changed, all mechanical gates and independent helper controls are rerun with fresh exact input bindings.
