/* Dependency-free force-directed graph (SVG).
   createGraph(container, options) -> controller
   options: { nodeIds?, focus?, mode: 'full'|'mini', minW, navigate, wheelZoom, onSelect, root } */
(function () {
  var NS = 'http://www.w3.org/2000/svg';
  var A = window.ATLAS;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  function cssVar(n) { return getComputedStyle(document.documentElement).getPropertyValue(n).trim(); }
  function mk(tag, attrs, parent) {
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  }
  function trunc(s, n) { return s.length > n ? s.slice(0, n - 1).trim() + '…' : s; }

  window.catColor = function (c) { return cssVar('--c-' + c) || '#888'; };

  window.createGraph = function (el, opt) {
    opt = opt || {};
    var mini = opt.mode === 'mini';
    var root = opt.root || '';
    var byId = {}; A.nodes.forEach(function (n) { byId[n.id] = n; });
    var ids = opt.nodeIds || A.nodes.map(function (n) { return n.id; });
    var idSet = {}; ids.forEach(function (i) { idSet[i] = 1; });

    // all candidate edges inside the node subset
    var allEdges = A.edges.filter(function (e) { return idSet[e.a] && idSet[e.b]; });
    if (opt.edgeFilter) allEdges = allEdges.filter(opt.edgeFilter);

    var W = el.clientWidth || 800, H = el.clientHeight || 500;
    var svg = mk('svg', { role: 'img', 'aria-label': 'Network graph of related articles' }, el);
    var vp = mk('g', {}, svg);
    var gE = mk('g', {}, vp), gN = mk('g', {}, vp);

    var nodes = ids.map(function (id, i) {
      var m = byId[id], ang = (i / ids.length) * Math.PI * 2;
      var deg = 0;
      allEdges.forEach(function (e) { if (e.a === id || e.b === id) deg++; });
      return { id: id, m: m, x: W / 2 + Math.cos(ang) * 120, y: H / 2 + Math.sin(ang) * 120, vx: 0, vy: 0, deg: deg, fx: null, fy: null };
    });
    var nIdx = {}; nodes.forEach(function (n, i) { nIdx[n.id] = i; });
    var cats = Object.keys(A.cats);
    var ringIdx = {}, ringN = 0; nodes.forEach(function (n) { if (n.id !== opt.focus) ringIdx[n.id] = ringN++; });

    var minW = opt.minW || 1, links = [], edgeEls = [], tf = { k: 1, x: 0, y: 0 };
    var hl = null, selId = null, filt = { cats: null, tag: null, q: '' };

    function buildLinks() {
      var best = {};
      allEdges.forEach(function (e) {
        [e.a, e.b].forEach(function (id) { if (!best[id] || e.w > best[id].w) best[id] = e; });
      });
      var keep = allEdges.filter(function (e) { return e.w >= minW || best[e.a] === e || best[e.b] === e; });
      links = keep.map(function (e) { return { s: nIdx[e.a], t: nIdx[e.b], w: e.w, e: e }; });
      gE.textContent = '';
      edgeEls = links.map(function (l) {
        var ln = mk('line', { 'class': 'g-edge', 'stroke-width': (0.8 + l.w * 0.6).toFixed(1), 'stroke-opacity': Math.min(0.2 + l.w * 0.14, 0.8).toFixed(2) }, gE);
        var t = mk('title', {}, ln);
        t.textContent = byId[l.e.a].title + ' ↔ ' + byId[l.e.b].title + ' — ' + l.e.shared.map(function (s) { return A.tags[s].label; }).join(', ');
        return ln;
      });
    }

    function radius(n) { return (mini ? 6 : 7) + Math.sqrt(n.deg) * (mini ? 1.0 : 1.5); }

    var nodeEls = nodes.map(function (n) {
      var g = mk('g', { 'class': 'g-node', tabindex: 0, role: 'link', 'aria-label': n.m.title + ' — ' + A.cats[n.m.cat] }, gN);
      var r = radius(n);
      n.r = r;
      mk('circle', { 'class': 'ring', r: r + 5 }, g);
      mk('circle', { 'class': 'body', r: r }, g);
      var t = mk('text', { y: r + 14 }, g);
      t.textContent = mini ? n.m.title : trunc(n.m.title, 30);
      g.addEventListener('keydown', function (ev) {
        if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); activate(n); }
      });
      g.addEventListener('mouseenter', function () { gN.appendChild(g); highlight(n.id); });
      g.addEventListener('mouseleave', function () { highlight(selId); });
      g.addEventListener('focus', function () { highlight(n.id); });
      g.addEventListener('blur', function () { highlight(selId); });
      return g;
    });
    if (opt.focus && nIdx[opt.focus] !== undefined) nodeEls[nIdx[opt.focus]].classList.add('focus');

    function paintColors() {
      nodes.forEach(function (n, i) { nodeEls[i].querySelector('.body').setAttribute('fill', window.catColor(n.m.cat)); });
    }

    function neighbours(id) {
      var s = {}; s[id] = 1;
      links.forEach(function (l) { if (nodes[l.s].id === id) s[nodes[l.t].id] = 1; if (nodes[l.t].id === id) s[nodes[l.s].id] = 1; });
      return s;
    }
    function highlight(id) {
      hl = id;
      if (!id) { nodeEls.forEach(function (g) { g.classList.remove('dim'); }); edgeEls.forEach(function (l) { l.classList.remove('dim'); }); return; }
      var nb = neighbours(id);
      nodes.forEach(function (n, i) { nodeEls[i].classList.toggle('dim', !nb[n.id]); });
      links.forEach(function (l, i) { edgeEls[i].classList.toggle('dim', nodes[l.s].id !== id && nodes[l.t].id !== id); });
    }

    function applyFilter() {
      var q = filt.q.toLowerCase();
      nodes.forEach(function (n, i) {
        var ok = true;
        if (filt.cats && !filt.cats[n.m.cat]) ok = false;
        if (ok && filt.tag && n.m.tags.indexOf(filt.tag) < 0) ok = false;
        if (ok && q) {
          var hay = (n.m.title + ' ' + n.m.summary + ' ' + n.m.tags.map(function (t) { return A.tags[t].label; }).join(' ')).toLowerCase();
          ok = hay.indexOf(q) >= 0;
        }
        nodeEls[i].classList.toggle('nomatch', !ok);
      });
    }

    // ---------- physics ----------
    var alpha = 1, raf = null;
    function anchor(cat) {
      var i = cats.indexOf(cat), a = (i / cats.length) * Math.PI * 2 - Math.PI / 2, R = Math.min(W, H) * 0.3;
      return { x: W / 2 + Math.cos(a) * R, y: H / 2 + Math.sin(a) * R };
    }
    function tick() {
      var i, j, a, b, dx, dy, d2, d, f;
      var rep = mini ? 2200 : 11000;
      for (i = 0; i < nodes.length; i++) {
        a = nodes[i];
        for (j = i + 1; j < nodes.length; j++) {
          b = nodes[j]; dx = a.x - b.x; dy = a.y - b.y; d2 = dx * dx + dy * dy + 60; d = Math.sqrt(d2);
          f = rep / d2 * alpha; dx = dx / d * f; dy = dy / d * f;
          a.vx += dx; a.vy += dy; b.vx -= dx; b.vy -= dy;
        }
      }
      links.forEach(function (l) {
        a = nodes[l.s]; b = nodes[l.t]; dx = b.x - a.x; dy = b.y - a.y; d = Math.sqrt(dx * dx + dy * dy) || 1;
        var L = mini ? 100 : 200 - l.w * 22; if (L < 70) L = 70;
        f = (d - L) * 0.012 * (0.6 + 0.15 * l.w) * alpha * (mini ? 0.5 : 1.2);
        dx = dx / d * f; dy = dy / d * f; a.vx += dx; a.vy += dy; b.vx -= dx; b.vy -= dy;
      });
      nodes.forEach(function (n) {
        n.vx += (W / 2 - n.x) * 0.004 * alpha; n.vy += (H / 2 - n.y) * 0.004 * alpha;
        if (!mini) { var an = anchor(n.m.cat); n.vx += (an.x - n.x) * 0.014 * alpha; n.vy += (an.y - n.y) * 0.014 * alpha; }
        else if (n.id !== opt.focus) { var k = ringIdx[n.id], ang = (k / ringN) * Math.PI * 2 - Math.PI / 2; n.vx += (W / 2 + Math.cos(ang) * W * 0.34 - n.x) * 0.06 * alpha; n.vy += (H / 2 + Math.sin(ang) * H * 0.36 - n.y) * 0.06 * alpha; }
        if (n.fx !== null) { n.x = n.fx; n.y = n.fy; n.vx = n.vy = 0; return; }
        n.vx *= 0.8; n.vy *= 0.8; n.x += n.vx; n.y += n.vy;
      });
      if (opt.focus && nIdx[opt.focus] !== undefined) { var c = nodes[nIdx[opt.focus]]; c.x = W / 2; c.y = H / 2; c.vx = c.vy = 0; }
    }
    function draw() {
      nodes.forEach(function (n, i) { nodeEls[i].setAttribute('transform', 'translate(' + n.x.toFixed(1) + ',' + n.y.toFixed(1) + ')'); });
      links.forEach(function (l, i) {
        var a = nodes[l.s], b = nodes[l.t], e = edgeEls[i];
        e.setAttribute('x1', a.x.toFixed(1)); e.setAttribute('y1', a.y.toFixed(1)); e.setAttribute('x2', b.x.toFixed(1)); e.setAttribute('y2', b.y.toFixed(1));
      });
    }
    function loop() {
      tick(); draw(); alpha *= 0.985;
      if (alpha > 0.02 || dragging) raf = requestAnimationFrame(loop); else raf = null;
    }
    function reheat(a) { alpha = Math.max(alpha, a || 0.6); if (!raf && !reduce) raf = requestAnimationFrame(loop); else if (reduce) { for (var i = 0; i < 200; i++) { tick(); alpha *= 0.985; } draw(); } }

    function setSize() {
      W = el.clientWidth || W; H = el.clientHeight || H;
    }

    // ---------- interaction ----------
    var dragging = null, panning = null, moved = 0, pt0 = null;
    function toGraph(ev) {
      var r = svg.getBoundingClientRect();
      return { x: (ev.clientX - r.left - tf.x) / tf.k, y: (ev.clientY - r.top - tf.y) / tf.k };
    }
    function applyTf() { vp.setAttribute('transform', 'translate(' + tf.x.toFixed(1) + ',' + tf.y.toFixed(1) + ') scale(' + tf.k.toFixed(3) + ')'); }
    function activate(n) {
      if (opt.navigate) { location.href = root + n.m.url; return; }
      select(n.id);
    }
    function select(id) {
      selId = id; nodeEls.forEach(function (g, i) { g.classList.toggle('sel', nodes[i].id === id); });
      highlight(id);
      if (opt.onSelect) opt.onSelect(id ? byId[id] : null);
    }
    nodeEls.forEach(function (g, i) {
      g.addEventListener('pointerdown', function (ev) {
        ev.stopPropagation();
        dragging = nodes[i]; moved = 0; pt0 = { x: ev.clientX, y: ev.clientY };
        svg.setPointerCapture(ev.pointerId);
        var p = toGraph(ev); dragging.fx = p.x; dragging.fy = p.y; reheat(0.4);
      });
    });
    svg.addEventListener('pointerdown', function (ev) {
      if (dragging) return;
      panning = { x: ev.clientX - tf.x, y: ev.clientY - tf.y }; moved = 0; pt0 = { x: ev.clientX, y: ev.clientY };
      svg.classList.add('panning'); svg.setPointerCapture(ev.pointerId);
    });
    svg.addEventListener('pointermove', function (ev) {
      if (pt0) moved = Math.max(moved, Math.abs(ev.clientX - pt0.x) + Math.abs(ev.clientY - pt0.y));
      if (dragging) { var p = toGraph(ev); dragging.fx = p.x; dragging.fy = p.y; if (reduce) { dragging.x = p.x; dragging.y = p.y; draw(); } }
      else if (panning && !mini) { tf.x = ev.clientX - panning.x; tf.y = ev.clientY - panning.y; applyTf(); }
    });
    function end() {
      var d = dragging, wasPan = panning;
      if (d) { d.fx = d.fy = null; dragging = null; if (moved < 5) activate(d); else reheat(0.3); }
      else if (wasPan && moved < 5 && !mini) select(null);
      panning = null; pt0 = null; svg.classList.remove('panning');
    }
    svg.addEventListener('pointerup', end);
    svg.addEventListener('pointercancel', end);

    function zoomAt(f, cx, cy) {
      var nk = Math.min(3, Math.max(0.4, tf.k * f)); f = nk / tf.k;
      tf.x = cx - (cx - tf.x) * f; tf.y = cy - (cy - tf.y) * f; tf.k = nk; applyTf();
    }
    if (opt.wheelZoom) {
      svg.addEventListener('wheel', function (ev) {
        ev.preventDefault(); var r = svg.getBoundingClientRect();
        zoomAt(ev.deltaY < 0 ? 1.12 : 1 / 1.12, ev.clientX - r.left, ev.clientY - r.top);
      }, { passive: false });
    }

    var ctl = {
      setMinW: function (v) { minW = v; buildLinks(); highlight(selId); reheat(0.7); },
      setFilter: function (f) { filt.cats = f.cats !== undefined ? f.cats : filt.cats; filt.tag = f.tag !== undefined ? f.tag : filt.tag; filt.q = f.q !== undefined ? f.q : filt.q; applyFilter(); },
      select: select,
      zoomIn: function () { zoomAt(1.25, W / 2, H / 2); },
      zoomOut: function () { zoomAt(1 / 1.25, W / 2, H / 2); },
      reset: function () { tf = { k: 1, x: 0, y: 0 }; applyTf(); reheat(0.5); },
      repaint: paintColors,
      neighbours: function (id) { return neighbours(id); },
      links: function () { return links; }
    };

    buildLinks(); paintColors(); applyTf();
    for (var s = 0; s < 260; s++) { tick(); alpha = Math.max(0.05, alpha * 0.985); }
    alpha = 0.25; draw();
    if (!reduce) raf = requestAnimationFrame(loop);

    if (window.ResizeObserver) {
      var first = true;
      new ResizeObserver(function () { if (first) { first = false; return; } setSize(); reheat(0.4); }).observe(el);
    }
    document.addEventListener('themechange', paintColors);
    return ctl;
  };
})();
