#!/usr/bin/env python3
"""Static site generator for the Upper Limb Atlas template.

    python3 build.py

Reads articles_data.py and writes:
    index.html, graph.html, articles/<slug>.html, assets/data.js
Relations: two articles are connected when they share at least one card (tag).
Edge weight = number of shared cards.
"""
import html
import itertools
import json
import math
import os

from articles_data import ARTICLES, CATEGORIES, SITE, TAGS

ROOT = os.path.dirname(os.path.abspath(__file__))
E = html.escape

# ---------------------------------------------------------------- derive data
by_slug = {a["slug"]: a for a in ARTICLES}
for a in ARTICLES:
    for t in a["tags"]:
        assert t in TAGS, f"unknown tag {t} in {a['slug']}"
    assert a["cat"] in CATEGORIES, a["slug"]
    words = sum(len(" ".join(s["p"] + s["ul"]).split()) for s in a["sections"]) + len(a["summary"].split())
    a["read"] = max(2, math.ceil(words / 200))
    a["url"] = f"articles/{a['slug']}.html"

edges = []
for x, y in itertools.combinations(ARTICLES, 2):
    shared = [t for t in x["tags"] if t in y["tags"]]
    if shared:
        edges.append({"a": x["slug"], "b": y["slug"], "w": len(shared), "shared": shared})


def related(slug):
    out = []
    for e in edges:
        if slug in (e["a"], e["b"]):
            other = e["b"] if e["a"] == slug else e["a"]
            out.append((other, e["w"], e["shared"]))
    out.sort(key=lambda r: (-r[1], by_slug[r[0]]["title"]))
    return out


for a in ARTICLES:
    a["rel"] = related(a["slug"])
    a["strong"] = sum(1 for r in a["rel"] if r[1] >= 2)

atlas = {
    "cats": CATEGORIES,
    "tags": {k: {"label": v[0], "kind": v[1]} for k, v in TAGS.items()},
    "nodes": [{"id": a["slug"], "title": a["title"], "cat": a["cat"], "summary": a["summary"],
               "tags": a["tags"], "url": a["url"]} for a in ARTICLES],
    "edges": edges,
}
os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
os.makedirs(os.path.join(ROOT, "articles"), exist_ok=True)
with open(os.path.join(ROOT, "assets", "data.js"), "w", encoding="utf-8") as f:
    f.write("window.ATLAS = " + json.dumps(atlas, ensure_ascii=False, indent=1) + ";\n")

# ---------------------------------------------------------------- shared chunks
LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true"><g stroke="currentColor" stroke-width="1.4" opacity=".55" fill="none">'
        '<path d="M8 9 16 17 24 8M16 17 7 25M16 17 25 25"/></g>'
        '<circle cx="8" cy="9" r="3.5" fill="var(--c-shoulder)"/><circle cx="24" cy="8" r="3.5" fill="var(--c-elbow)"/>'
        '<circle cx="16" cy="17" r="4.2" fill="var(--accent)"/><circle cx="7" cy="25" r="3.2" fill="var(--c-hand)"/>'
        '<circle cx="25" cy="25" r="3.2" fill="var(--c-wrist)"/></svg>')
SUN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M18.7 5.3l-1.6 1.6M6.9 17.1l-1.6 1.6"/></svg>'
SEARCH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="6.5"/><path d="m16 16 4.5 4.5"/></svg>'

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700;9..144,800'
         '&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">')

THEME_INIT = ('<script>try{var t=localStorage.getItem("ula-theme");if(t)document.documentElement.setAttribute("data-theme",t)}catch(e){}</script>')


def head(title, desc, root):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{E(title)}</title><meta name="description" content="{E(desc)}">'
            f'{THEME_INIT}{FONTS}<link rel="stylesheet" href="{root}assets/style.css"></head>')


def header(root, active):
    def a(label, href, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{root}{href}"{cur}>{label}</a>'
    return (f'<a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="wrap">'
            f'<a class="brand" href="{root}index.html">{LOGO}<span>{E(SITE["name"])}</span></a>'
            f'<nav class="nav" aria-label="Primary">{a("Articles", "index.html#articles", "articles")}'
            f'{a("Network graph", "graph.html", "graph")}{a("Topics", "index.html#topics", "topics")}'
            f'{a("Notice", "index.html#notice", "notice")}</nav>'
            f'<button class="icon-btn" id="theme" aria-label="Toggle light / dark theme">{SUN}</button></div></header>')


NOTICE = ('<aside class="notice" id="notice"><div class="wrap"><h2>Important notice</h2>'
          '<p>This is a design template populated with <strong>sample educational content</strong>. It is a general overview of upper limb '
          'surgery topics and is not a substitute for clinical judgement, local protocols or the primary literature. '
          'Replace the sample text and add your own references before publishing.</p>'
          '<p>Connections between articles are computed automatically from the cards (topics) they share. '
          'A shared card indicates a common anatomical structure, pathology or approach, not a clinical recommendation.</p>'
          '<div class="foot-links"><span>© Upper Limb Atlas template</span></div>{extra}</div></aside>')


def scripts(root):
    return (f'<script src="{root}assets/data.js"></script><script src="{root}assets/graph.js"></script>'
            f'<script src="{root}assets/app.js"></script></body></html>')


def dotstyle(cat):
    return f'style="--dot:var(--c-{cat})"'


def card(a, root, shared=None):
    meta = ""
    if shared is None:
        meta = (f'<div class="meta"><span>{a["read"]} min read</span><span>{len(a["tags"])} cards</span>'
                f'<span>{a["strong"]} strongly related</span></div>')
    else:
        chips = "".join(f'<span class="tag-pill">{E(TAGS[t][0])}</span>' for t in shared)
        meta = f'<div class="meta shared" style="display:block"><div class="shared">{chips}</div></div>'
    search = " ".join([a["title"], a["summary"]] + [TAGS[t][0] for t in a["tags"]] + [CATEGORIES[a["cat"]]]).lower()
    return (f'<a class="card" href="{root}{a["url"]}" {dotstyle(a["cat"])} data-slug="{a["slug"]}" data-cat="{a["cat"]}" '
            f'data-tags="{" ".join(a["tags"])}" data-title="{E(a["title"])}" data-date="{a["date"]}" data-conn="{a["strong"]}" '
            f'data-search="{E(search)}"><div class="top"><span class="tag-pill"><span class="dot"></span>{CATEGORIES[a["cat"]]}</span>'
            f'<span>{a["type"]}</span><span>· {a["date"]}</span></div><h3>{E(a["title"])}</h3><p>{E(a["summary"])}</p>{meta}</a>')


# ---------------------------------------------------------------- index
def build_index():
    n_cond = sum(1 for a in ARTICLES if a["type"] == "Condition")
    n_proc = sum(1 for a in ARTICLES if a["type"] == "Procedure")
    stats = [(len(ARTICLES), "Articles"), (n_cond, "Conditions"), (n_proc, "Procedures"), (len(TAGS), "Topic cards"), (len(edges), "Connections")]
    stat_html = "".join(f'<div class="stat"><b data-count="{n}">{n}</b><span>{l}</span></div>' for n, l in stats)

    region_chips = '<button class="chip" aria-pressed="true" data-cat="all">All regions</button>' + "".join(
        f'<button class="chip" aria-pressed="false" data-cat="{c}" {dotstyle(c)}><span class="dot"></span>{l}</button>'
        for c, l in CATEGORIES.items())

    ordered = sorted(ARTICLES, key=lambda a: a["date"], reverse=True)
    cards = "".join(card(a, "") for a in ordered)

    kinds = {}
    for t, (label, kind) in TAGS.items():
        kinds.setdefault(kind, []).append((t, label))
    topics = ""
    for kind in ["Region", "Structure", "Pathology", "Approach"]:
        items = "".join(
            f'<a class="topic" href="index.html#tag={t}"><span>{E(l)}</span><b>{sum(1 for a in ARTICLES if t in a["tags"])}</b></a>'
            for t, l in kinds[kind])
        topics += f'<div class="kind"><h3>{kind}</h3><div class="topic-grid">{items}</div></div>'

    sitemap = "".join(f'<li><a href="{a["url"]}"><span class="dot" {dotstyle(a["cat"])}></span>{E(a["title"])}</a></li>'
                      for a in sorted(ARTICLES, key=lambda a: a["title"]))
    extra = f'<ul class="sitemap" aria-label="All articles">{sitemap}</ul>'

    return (head(f'{SITE["name"]} — Upper limb surgery reference', SITE["description"], "") +
            '<body data-root="">' + header("", "home") + '<main id="main">'
            '<section class="hero"><div class="wrap">'
            '<span class="eyebrow">Upper limb surgery · Evidence atlas</span>'
            '<h1>Upper Limb <em>Atlas</em></h1>'
            f'<p class="lede">A cross-linked reference covering the shoulder, elbow, wrist, hand and nerve reconstruction. '
            f'{len(ARTICLES)} articles, {len(TAGS)} topic cards and {len(edges)} connections, explorable as a list or as a live network.</p>'
            f'<form class="search" role="search" onsubmit="return false">{SEARCH}<label class="sr-only" for="q">Search articles</label>'
            '<input id="q" type="search" placeholder="Search conditions, procedures, structures…" autocomplete="off"></form>'
            f'<div class="stats">{stat_html}</div></div></section>'

            '<section class="block" id="articles"><div class="wrap">'
            '<div class="sec-head"><div><span class="eyebrow">Key articles</span><h2>Browse the atlas</h2></div>'
            '<a class="more" href="graph.html">See how they connect →</a></div>'
            f'<div class="toolbar"><div class="chips" id="region-chips">{region_chips}</div>'
            '<span class="active-filter" id="active-filter"><span class="chip on">Card: <b id="af-label"></b></span>'
            '<button class="chip" id="af-clear">Clear ×</button></span>'
            '<label class="sr-only" for="sort">Sort</label><select class="select" id="sort"><option value="new">Newest first</option>'
            '<option value="az">A to Z</option><option value="conn">Most connected</option></select></div>'
            '<div class="count-note" id="count" aria-live="polite"></div>'
            f'<div class="grid" id="card-list">{cards}</div>'
            '<div class="empty" id="empty">No articles match these filters.</div></div></section>'

            '<section class="block" id="network"><div class="wrap"><div class="graph-block">'
            '<div class="graph-intro"><div><span class="eyebrow">Network graph</span>'
            '<h2 style="font-family:var(--font-display);margin:6px 0 8px;font-size:1.8rem">Every article, connected by what it shares</h2>'
            '<p>Each node is an article; each line means two articles share one or more cards (structure, pathology or approach). '
            'Thicker lines mean more shared cards (3 or more shown here). Drag, click to inspect, filter by region.</p></div>'
            '<a class="btn" href="graph.html">Open network graph →</a></div>'
            '<div style="padding:14px 24px;border-bottom:1px solid var(--line)"><div class="legend" id="legend-index"></div></div>'
            '<div class="graph-wrap" id="graph-index"><div class="g-panel" role="dialog" aria-label="Article details"></div></div>'
            '</div></div></section>'

            '<section class="block" id="topics"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">Cards</span>'
            '<h2>Browse by topic</h2></div></div>' + topics + '</div></section>'

            '<section class="block" id="about"><div class="wrap"><div class="signup"><div><span class="eyebrow">Newsletter</span>'
            '<h2>New articles, straight to your inbox</h2><p>Template sign-up block. Connect it to your email provider.</p></div>'
            '<form id="signup-form"><label class="sr-only" for="em">Email</label><input id="em" type="email" placeholder="you@hospital.org" required>'
            '<button class="btn" type="submit">Subscribe</button><small id="signup-msg">You can unsubscribe at any time.</small></form></div></div></section>'
            '</main>' + NOTICE.replace("{extra}", extra) + scripts(""))


# ---------------------------------------------------------------- graph page
def build_graph():
    return (head(f'Network graph — {SITE["name"]}', "Interactive network of upper limb surgery articles.", "") +
            '<body data-root="">' + header("", "graph") + '<main id="main"><div class="graph-page"><aside class="graph-side">'
            '<div><span class="eyebrow">Network graph</span><h1>Article relations</h1>'
            '<p>Articles are linked when they share cards. Select a node to open its connections.</p></div>'
            '<div class="field"><label for="g-q">Search</label><input id="g-q" type="search" placeholder="e.g. instability, ulnar…"></div>'
            '<div class="field"><span class="lab">Minimum shared cards</span><input id="g-w" type="range" min="1" max="5" value="3" aria-label="Minimum shared cards">'
            '<div class="range-row"><span>looser</span><span id="g-wv">3+</span><span>tighter</span></div></div>'
            '<div class="field"><span class="lab">Region</span><div class="legend" id="g-cats"></div></div>'
            '<div class="field"><span class="lab">Highlight a card</span><div class="tag-scroll" id="g-tags"></div></div>'
            '<button class="btn ghost" id="g-reset" type="button">Reset view</button></aside>'
            '<div class="graph-wrap full" id="graph-full"><div class="g-panel" role="dialog" aria-label="Article details"></div></div>'
            '</div></main>' + scripts(""))


# ---------------------------------------------------------------- article pages
def build_article(i, a):
    root = "../"
    cat = a["cat"]
    rel = a["rel"]
    body = ""
    for s in a["sections"]:
        body += f'<h2>{E(s["h"])}</h2>'
        for p in s["p"]:
            body += f"<p>{E(p)}</p>"
        if s["ul"]:
            body += "<ul>" + "".join(f"<li>{E(x)}</li>" for x in s["ul"]) + "</ul>"
    key = ('<div class="keybox"><h2>Key points</h2><ul>' + "".join(f"<li>{E(k)}</li>" for k in a["key_points"]) + "</ul></div>")
    refs = '<div class="refs"><strong>References.</strong> Template placeholder: add citations to guidelines, trials and reviews here.</div>'

    chips = "".join(f'<a class="chip" href="{root}index.html#tag={t}">{E(TAGS[t][0])}</a>' for t in a["tags"])
    top = rel[:6]
    rel_cards = "".join(card(by_slug[s], root, sh) for s, w, sh in top)

    by_card = ""
    for t in a["tags"]:
        others = [by_slug[o["slug"]] for o in sorted(
            (x for x in ARTICLES if x["slug"] != a["slug"] and t in x["tags"]), key=lambda x: x["title"])]
        if not others:
            continue
        lis = "".join(f'<li><a href="{root}{o["url"]}"><span class="dot" {dotstyle(o["cat"])}></span>{E(o["title"])}</a></li>' for o in others)
        by_card += (f'<section><h3><a href="{root}index.html#tag={t}">{E(TAGS[t][0])}</a><small>{len(others)}</small></h3><ul>{lis}</ul></section>')

    ordered = sorted(ARTICLES, key=lambda x: x["date"])
    idx = ordered.index(a)
    prev_a = ordered[idx - 1] if idx > 0 else None
    next_a = ordered[idx + 1] if idx < len(ordered) - 1 else None
    pager = ""
    pager += (f'<a href="{root}{prev_a["url"]}"><small>← Previous</small>{E(prev_a["title"])}</a>' if prev_a else "<span></span>")
    pager += (f'<a class="next" href="{root}{next_a["url"]}"><small>Next →</small>{E(next_a["title"])}</a>' if next_a else "<span></span>")

    return (head(f'{a["title"]} — {SITE["name"]}', a["summary"], root) + '<body data-root="../">' + header(root, "articles") +
            f'<main id="main" {dotstyle(cat)}><header class="art-head" {dotstyle(cat)}><div class="wrap">'
            f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{root}index.html">Home</a><span>/</span>'
            f'<a href="{root}index.html#articles">Articles</a><span>/</span><span>{CATEGORIES[cat]}</span></nav>'
            f'<span class="tag-pill" style="margin-top:18px"><span class="dot" {dotstyle(cat)}></span>{CATEGORIES[cat]} · {a["type"]}</span>'
            f'<h1>{E(a["title"])}</h1><p class="lede">{E(a["summary"])}</p>'
            f'<div class="meta-strip"><div><small>Region</small><span>{CATEGORIES[cat]}</span></div><div><small>Type</small><span>{a["type"]}</span></div>'
            f'<div><small>Updated</small><span>{a["date"]}</span></div><div><small>Reading time</small><span>{a["read"]} min</span></div>'
            f'<div><small>Connected</small><span>{len(rel)} articles</span></div></div></div></header>'
            f'<div class="wrap"><div class="art-layout"><article class="prose" {dotstyle(cat)}>{body}{key}{refs}</article>'
            f'<aside class="aside"><section><h2>Cards on this article</h2><div class="chips">{chips}</div></section>'
            f'<section><h2>Local network</h2><div class="graph-wrap mini" id="graph-mini" data-focus="{a["slug"]}"></div>'
            f'<a class="link-all" href="{root}graph.html#focus={a["slug"]}">Open in full graph →</a></section></aside></div>'
            f'<section class="rel-section"><div class="sec-head"><div><span class="eyebrow">Related</span><h2>Most closely connected</h2></div></div>'
            f'<div class="grid">{rel_cards}</div></section>'
            f'<section class="rel-section" style="padding-top:48px"><div class="sec-head"><div><span class="eyebrow">By card</span>'
            f'<h2>Every article sharing a card</h2></div></div><div class="by-card">{by_card}</div></section>'
            f'<nav class="pager" aria-label="Previous and next">{pager}</nav></div></main>' +
            NOTICE.replace("{extra}", "") + scripts(root))


def write(path, content):
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as f:
        f.write(content)


write("index.html", build_index())
write("graph.html", build_graph())
for i, a in enumerate(ARTICLES):
    write(a["url"], build_article(i, a))

print(f"{len(ARTICLES)} articles, {len(TAGS)} cards, {len(edges)} connections "
      f"({sum(1 for e in edges if e['w'] >= 2)} with 2+ shared)")
