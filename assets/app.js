/* Page behaviour: theme, counters, article filtering, graph wiring. */
(function () {
  var A = window.ATLAS, body = document.body, ROOT = body.getAttribute('data-root') || '';
  var byId = {}; A.nodes.forEach(function (n) { byId[n.id] = n; });
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- theme ---------- */
  var tbtn = $('#theme');
  function current() {
    var t = document.documentElement.getAttribute('data-theme');
    return t || (matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
  }
  if (tbtn) tbtn.addEventListener('click', function () {
    var next = current() === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    try { localStorage.setItem('ula-theme', next); } catch (e) {}
    document.dispatchEvent(new Event('themechange'));
  });

  /* ---------- counters ---------- */
  $$('[data-count]').forEach(function (el) {
    var target = +el.getAttribute('data-count');
    if (reduce) { el.textContent = target; return; }
    var t0 = performance.now(), dur = 900;
    (function step(t) {
      var p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * e);
      if (p < 1) requestAnimationFrame(step);
    })(t0);
  });

  /* ---------- graph panel ---------- */
  function showPanel(panel, m, ctl) {
    if (!m) { panel.classList.remove('show'); return; }
    var rel = A.edges.filter(function (e) { return e.a === m.id || e.b === m.id; })
      .map(function (e) { return { id: e.a === m.id ? e.b : e.a, w: e.w, shared: e.shared }; })
      .sort(function (x, y) { return y.w - x.w; });
    var html = '<button class="close" aria-label="Close">×</button>' +
      '<span class="tag-pill" style="--dot:var(--c-' + m.cat + ')"><span class="dot"></span>' + esc(A.cats[m.cat]) + '</span>' +
      '<h4>' + esc(m.title) + '</h4><p>' + esc(m.summary) + '</p>' +
      '<a class="btn" href="' + ROOT + m.url + '">Open article →</a>' +
      '<div class="lbl">Cards</div><div class="chips">' +
      m.tags.map(function (t) { return '<a class="chip" href="' + ROOT + 'index.html#tag=' + t + '">' + esc(A.tags[t].label) + '</a>'; }).join('') + '</div>' +
      '<div class="lbl">Connected (' + rel.length + ')</div><ul>' +
      rel.slice(0, 7).map(function (r) {
        var o = byId[r.id];
        return '<li><a href="' + ROOT + o.url + '"><span class="dot" style="--dot:var(--c-' + o.cat + ')"></span>' + esc(o.title) + '<small>' + r.w + ' shared</small></a></li>';
      }).join('') + '</ul>';
    panel.innerHTML = html;
    panel.classList.add('show');
    panel.querySelector('.close').addEventListener('click', function () { ctl.select(null); });
  }

  function setupGraph(wrap, o) {
    var panel = $('.g-panel', wrap), ctl;
    var opts = { root: ROOT, onSelect: function (m) { if (panel) showPanel(panel, m, ctl); } };
    for (var k in o) opts[k] = o[k];
    ctl = window.createGraph(wrap, opts);
    if (opts.mode !== 'mini') {
      var z = document.createElement('div'); z.className = 'g-zoom';
      z.innerHTML = '<button aria-label="Zoom in">+</button><button aria-label="Zoom out">−</button><button aria-label="Reset view">⟲</button>';
      var b = z.querySelectorAll('button');
      b[0].onclick = ctl.zoomIn; b[1].onclick = ctl.zoomOut; b[2].onclick = ctl.reset;
      wrap.appendChild(z);
      var h = document.createElement('div'); h.className = 'g-hint';
      h.textContent = 'drag nodes · click to inspect' + (opts.wheelZoom ? ' · scroll to zoom' : '');
      wrap.appendChild(h);
    }
    return ctl;
  }

  function legend(host, ctl) {
    var on = {}; Object.keys(A.cats).forEach(function (c) { on[c] = true; });
    host.innerHTML = Object.keys(A.cats).map(function (c) {
      return '<button class="chip" aria-pressed="true" data-c="' + c + '" style="--dot:var(--c-' + c + ')"><span class="dot"></span>' + esc(A.cats[c]) + '</button>';
    }).join('');
    $$('button', host).forEach(function (b) {
      b.addEventListener('click', function () {
        var c = b.getAttribute('data-c'); on[c] = !on[c]; b.setAttribute('aria-pressed', on[c]);
        var all = Object.keys(on).every(function (k) { return on[k]; });
        ctl.setFilter({ cats: all ? null : JSON.parse(JSON.stringify(on)) });
      });
    });
  }

  /* ---------- index page ---------- */
  var gi = $('#graph-index');
  if (gi) {
    var ctlI = setupGraph(gi, { mode: 'full', minW: 3, wheelZoom: false });
    legend($('#legend-index'), ctlI);
  }

  var cards = $$('.card[data-slug]');
  if (cards.length && $('#articles')) {
    var st = { q: '', cat: 'all', tag: null, sort: 'new' };
    var list = $('#card-list'), qEl = $('#q'), countEl = $('#count'), emptyEl = $('#empty'), af = $('#active-filter');
    function apply() {
      var n = 0, q = st.q.toLowerCase().trim();
      cards.forEach(function (c) {
        var ok = (st.cat === 'all' || c.getAttribute('data-cat') === st.cat) &&
          (!st.tag || (' ' + c.getAttribute('data-tags') + ' ').indexOf(' ' + st.tag + ' ') >= 0) &&
          (!q || c.getAttribute('data-search').indexOf(q) >= 0);
        c.hidden = !ok; if (ok) n++;
      });
      countEl.textContent = 'Showing ' + n + ' of ' + cards.length + ' articles';
      emptyEl.classList.toggle('show', n === 0);
      if (st.tag) { af.classList.add('show'); $('#af-label', af).textContent = A.tags[st.tag] ? A.tags[st.tag].label : st.tag; } else af.classList.remove('show');
      if (typeof ctlI !== 'undefined') ctlI.setFilter({ tag: st.tag, q: st.q });
    }
    function sortCards() {
      var arr = cards.slice();
      arr.sort(function (a, b) {
        if (st.sort === 'az') return a.getAttribute('data-title').localeCompare(b.getAttribute('data-title'));
        if (st.sort === 'conn') return b.getAttribute('data-conn') - a.getAttribute('data-conn');
        return b.getAttribute('data-date').localeCompare(a.getAttribute('data-date'));
      });
      arr.forEach(function (c) { list.appendChild(c); });
    }
    qEl.addEventListener('input', function () { st.q = qEl.value; apply(); });
    $$('#region-chips .chip').forEach(function (b) {
      b.addEventListener('click', function () {
        st.cat = b.getAttribute('data-cat');
        $$('#region-chips .chip').forEach(function (x) { x.setAttribute('aria-pressed', x === b); });
        apply();
      });
    });
    $('#sort').addEventListener('change', function (e) { st.sort = e.target.value; sortCards(); });
    $('#af-clear').addEventListener('click', function () { location.hash = '#articles'; });
    function readHash() {
      var m = /tag=([a-z0-9-]+)/.exec(location.hash);
      st.tag = m ? m[1] : null; apply();
      if (m) { var s = $('#articles'); if (s) s.scrollIntoView(); }
    }
    window.addEventListener('hashchange', readHash);
    sortCards(); readHash();
  }

  /* ---------- newsletter (template: no backend) ---------- */
  var nf = $('#signup-form');
  if (nf) nf.addEventListener('submit', function (e) {
    e.preventDefault(); $('#signup-msg').textContent = 'Template form: connect your email provider to enable sign-ups.';
  });

  /* ---------- full graph page ---------- */
  var gp = $('#graph-full');
  if (gp) {
    var ctlG = setupGraph(gp, { mode: 'full', minW: 3, wheelZoom: true });
    legend($('#g-cats'), ctlG);
    $('#g-q').addEventListener('input', function (e) { ctlG.setFilter({ q: e.target.value }); });
    var rng = $('#g-w'), rv = $('#g-wv');
    rng.addEventListener('input', function () { rv.textContent = rng.value + '+'; ctlG.setMinW(+rng.value); });
    var tagHost = $('#g-tags'), curTag = null;
    tagHost.innerHTML = Object.keys(A.tags).map(function (t) {
      return '<button class="chip" aria-pressed="false" data-t="' + t + '">' + esc(A.tags[t].label) + '</button>';
    }).join('');
    function setTag(t) {
      curTag = (curTag === t) ? null : t;
      $$('button', tagHost).forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-t') === curTag); });
      ctlG.setFilter({ tag: curTag });
    }
    $$('button', tagHost).forEach(function (b) { b.addEventListener('click', function () { setTag(b.getAttribute('data-t')); }); });
    $('#g-reset').addEventListener('click', function () {
      curTag = null; $$('button', tagHost).forEach(function (b) { b.setAttribute('aria-pressed', 'false'); });
      $('#g-q').value = ''; rng.value = 3; rv.textContent = '3+';
      $$('#g-cats button').forEach(function (b) { b.setAttribute('aria-pressed', 'true'); });
      ctlG.setFilter({ cats: null, tag: null, q: '' }); ctlG.setMinW(3); ctlG.select(null); ctlG.reset();
    });
    var hm = /tag=([a-z0-9-]+)/.exec(location.hash), hf = /focus=([a-z0-9-]+)/.exec(location.hash);
    if (hm && A.tags[hm[1]]) setTag(hm[1]);
    if (hf && byId[hf[1]]) setTimeout(function () { ctlG.select(hf[1]); }, 50);
  }

  /* ---------- article page: ego graph ---------- */
  var gm = $('#graph-mini');
  if (gm) {
    var focus = gm.getAttribute('data-focus');
    var rel = A.edges.filter(function (e) { return e.a === focus || e.b === focus; })
      .map(function (e) { return { id: e.a === focus ? e.b : e.a, w: e.w }; })
      .sort(function (x, y) { return y.w - x.w; }).slice(0, 8);
    var keep = {}; keep[focus] = 1; rel.forEach(function (r) { keep[r.id] = 1; });
    window.createGraph && setupGraph(gm, {
      mode: 'mini', navigate: true, focus: focus, minW: 1, nodeIds: Object.keys(keep),
      edgeFilter: function (e) { return e.a === focus || e.b === focus || e.w >= 2; }
    });
  }
})();
