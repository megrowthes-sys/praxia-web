(function(){
  // Panels can be customised per page via window.PRAXIA_DECK_PANELS BEFORE this script loads.
  // If not provided, the landing defaults are used.
  var DEFAULT_PANELS = [
    { id: 'panel-bienvenida',  label: 'Bienvenida',   num: '00' },
    { id: 'panel-metodo',      label: 'Método',       num: '01' },
    { id: 'panel-paraquien',   label: 'Para quién',   num: '02' },
    { id: 'panel-capsulas',    label: 'Cápsulas',     num: '03' },
    { id: 'panel-fundadora',   label: 'Fundadora',    num: '04' },
    { id: 'panel-casos',       label: 'Casos',        num: '05' },
    { id: 'panel-faq',         label: 'FAQ',          num: '06' },
    { id: 'panel-contacto',    label: 'Contacto',     num: '07' }
  ];
  var DEFAULT_ANCHOR_MAP = {
    'metodo': 'panel-metodo', 'idea': 'panel-paraquien', 'capsulas': 'panel-capsulas',
    'fundadora': 'panel-fundadora', 'casos': 'panel-casos', 'contacto': 'panel-contacto'
  };
  var PANELS = (window.PRAXIA_DECK_PANELS && window.PRAXIA_DECK_PANELS.length) ? window.PRAXIA_DECK_PANELS : DEFAULT_PANELS;
  var ANCHOR_MAP = window.PRAXIA_DECK_ANCHOR_MAP || DEFAULT_ANCHOR_MAP;

  function ready(fn){ if (document.readyState !== 'loading') fn(); else document.addEventListener('DOMContentLoaded', fn); }

  // Optional config: cta on the header (label + href). Default = booking link.
  var CTA = window.PRAXIA_DECK_CTA || { label: 'Reservar diagnóstico', href: '#contacto' };
  // Optional brand link (default: index.html). For the deck home button.
  var HOME_HREF = window.PRAXIA_DECK_HOME || 'index.html';
  function injectHeader(){
    if (document.querySelector('.deck-header')) return; // page already provides one
    var hdr = document.createElement('header');
    hdr.className = 'deck-header';
    hdr.setAttribute('role', 'navigation');
    hdr.setAttribute('aria-label', 'Secciones de la página');
    // We add an empty #praxia-header-actions slot so praxia-i18n.js can drop
    // its ES/EN switcher there (it queries that id and falls back otherwise).
    hdr.innerHTML =
      '<div class="deck-header-inner">' +
        '<a href="' + HOME_HREF + '" class="deck-brand" aria-label="Praxia Atelier · inicio" data-deck-home>' +
          '<div class="mark"><span>P</span></div>' +
          '<div class="name-stack">' +
            '<div class="name">Praxia Atelier</div>' +
            '<div class="tagline">Ecosystem architecture</div>' +
          '</div>' +
        '</a>' +
        '<nav class="deck-stepper" id="deckStepper" aria-label="Navegación por secciones"></nav>' +
        '<div id="praxia-header-actions" class="deck-actions">' +
          '<a href="' + CTA.href + '" class="deck-cta">' + CTA.label + '</a>' +
        '</div>' +
      '</div>';
    document.body.insertBefore(hdr, document.body.firstChild);

    var prev = document.createElement('button');
    prev.className = 'deck-nav-btn prev'; prev.id = 'deckPrev';
    prev.setAttribute('aria-label', 'Sección anterior');
    prev.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>';
    document.body.appendChild(prev);

    var next = document.createElement('button');
    next.className = 'deck-nav-btn next'; next.id = 'deckNext';
    next.setAttribute('aria-label', 'Sección siguiente');
    next.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>';
    document.body.appendChild(next);

    var prog = document.createElement('div');
    prog.className = 'deck-progress'; prog.id = 'deckProgress';
    prog.setAttribute('aria-live', 'polite');
    prog.textContent = '1 / ' + PANELS.length;
    document.body.appendChild(prog);
  }

  // The header height changes on mobile when chips wrap to several lines.
  // We measure it after layout and expose it as --actual-header-h so the
  // deck panel below docks tightly underneath, with no gap or overlap.
  function syncHeaderHeight(){
    var hdr = document.querySelector('.deck-header');
    if (!hdr) return;
    var h = hdr.getBoundingClientRect().height;
    document.documentElement.style.setProperty('--actual-header-h', h + 'px');
    document.body.setAttribute('data-header-h', String(Math.round(h)));
  }

  function wrapDeck(){
    if (document.querySelector('.praxia-deck')) return;
    // Find the first and last data-panel section to determine where to wrap
    var sections = document.querySelectorAll('section[data-panel], section[data-panel-continue]');
    if (!sections.length) return;
    var first = sections[0];
    var last = sections[sections.length - 1];
    var shell = document.createElement('div');
    shell.className = 'praxia-deck-shell';
    var deck = document.createElement('main');
    deck.className = 'praxia-deck';
    deck.id = 'praxiaDeck';
    first.parentNode.insertBefore(shell, first);
    shell.appendChild(deck);
    // Move all sections (and any data-panel-continue between them) into the deck
    var node = first;
    while (node) {
      var nxt = node.nextElementSibling;
      if (node.matches && node.matches('section[data-panel], section[data-panel-continue]')) {
        deck.appendChild(node);
      }
      if (node === last) break;
      node = nxt;
    }
  }

  ready(function(){
    document.body.classList.add('deck-mode');
    injectHeader();
    wrapDeck();
    // Sync header height now and on resize/orientation change so the panel
    // below docks correctly when the chip stepper wraps to multiple lines.
    syncHeaderHeight();
    window.addEventListener('resize', syncHeaderHeight);
    window.addEventListener('orientationchange', function(){ setTimeout(syncHeaderHeight, 80); });
    // Re-measure when i18n switches language (chip widths change).
    document.addEventListener('praxia:i18n-applied', function(){ setTimeout(syncHeaderHeight, 30); });

    // For each main panel, append the following [data-panel-continue] sections inside it
    PANELS.forEach(function(p){
      var el = document.querySelector('section[data-panel="'+p.id+'"]');
      if (!el) return;
      var node = el.nextElementSibling;
      while (node && node.matches && node.matches('section[data-panel-continue]')) {
        var next = node.nextElementSibling;
        // Move continuation into the main panel
        node.style.display = 'block';
        el.appendChild(node);
        node = next;
      }
    });

    // Also handle the case where panel-paraquien (idea) and panel-paraquien2 (para quién) exist,
    // and panel-paraquien2 should be merged into panel-paraquien for cleanliness.
    var pq2 = document.querySelector('section[data-panel="panel-paraquien2"]');
    var pq1 = document.querySelector('section[data-panel="panel-paraquien"]');
    if (pq2 && pq1) {
      // Move panel-paraquien2 content into panel-paraquien as a continuation
      pq2.removeAttribute('data-panel');
      pq2.setAttribute('data-merged-into', 'panel-paraquien');
      pq2.style.display = 'block';
      pq1.appendChild(pq2);
    }

    // Build stepper
    // Each PANELS entry can be:
    //   { id, label, num }            -> internal panel
    //   { href, label, num, external? } -> link to another page (no num is fine)
    var stepper = document.getElementById('deckStepper');
    var INTERNAL_PANELS = []; // panels that exist as data-panel sections in this page
    PANELS.forEach(function(p){
      if (p.id) INTERNAL_PANELS.push(p);
    });
    PANELS.forEach(function(p, idx){
      // External link chip
      if (p.href) {
        var a = document.createElement('a');
        a.className = 'deck-chip deck-chip-link';
        a.href = p.href;
        if (p.external) { a.target = '_blank'; a.rel = 'noopener'; }
        a.setAttribute('aria-label', (p.num ? p.num + ' ' : '') + p.label);
        a.innerHTML = (p.num ? '<span class="num">' + p.num + '</span>' : '') + '<span>' + p.label + '</span>';
        if (p.dataI18n) a.setAttribute('data-i18n', p.dataI18n);
        stepper.appendChild(a);
        return;
      }
      // Internal panel chip
      var btn = document.createElement('button');
      btn.className = 'deck-chip';
      btn.type = 'button';
      btn.setAttribute('data-target', p.id);
      btn.setAttribute('aria-label', (p.num ? p.num + ' ' : '') + p.label);
      btn.innerHTML = (p.num ? '<span class="num">' + p.num + '</span>' : '') + '<span>' + p.label + '</span>';
      if (p.dataI18n) btn.setAttribute('data-i18n', p.dataI18n);
      btn.addEventListener('click', function(){
        var internalIdx = INTERNAL_PANELS.findIndex(function(x){ return x.id === p.id; });
        if (internalIdx >= 0) goTo(internalIdx);
      });
      stepper.appendChild(btn);
    });

    // After injecting chips, ask the i18n script (if loaded) to re-translate
    // the page so the chip labels and the CTA pick up the current language.
    function refreshI18n(){
      if (window.PraxiaI18n && typeof window.PraxiaI18n.refresh === 'function') {
        try { window.PraxiaI18n.refresh(); } catch(e){}
      }
    }
    // i18n may load slightly after deck. Try now, and again on a microtask
    // tick and once more after a short delay to cover any race condition.
    refreshI18n();
    setTimeout(refreshI18n, 0);
    setTimeout(refreshI18n, 200);

    var current = 0;
    var prevBtn = document.getElementById('deckPrev');
    var nextBtn = document.getElementById('deckNext');
    var progress = document.getElementById('deckProgress');

    function goTo(idx){
      if (idx < 0 || idx >= INTERNAL_PANELS.length) return;
      current = idx;
      INTERNAL_PANELS.forEach(function(p, i){
        var sec = document.querySelector('section[data-panel="'+p.id+'"]');
        if (!sec) return;
        if (i === idx) {
          sec.classList.add('is-active');
          sec.scrollTop = 0;
        } else {
          sec.classList.remove('is-active');
        }
      });
      // Update chips: highlight only internal-panel chip matching the active panel id
      var activeId = INTERNAL_PANELS[idx].id;
      var allChips = stepper.querySelectorAll('.deck-chip');
      var activeChip = null;
      Array.prototype.forEach.call(allChips, function(c){
        var isMatch = (c.getAttribute('data-target') === activeId);
        c.classList.toggle('is-active', isMatch);
        if (isMatch) activeChip = c;
      });
      if (activeChip && activeChip.scrollIntoView) {
        try { activeChip.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' }); } catch(e){}
      }
      // Progress + nav
      if (progress) progress.textContent = (idx + 1) + ' / ' + INTERNAL_PANELS.length;
      if (prevBtn) prevBtn.disabled = (idx === 0);
      if (nextBtn) nextBtn.disabled = (idx === INTERNAL_PANELS.length - 1);
      try { history.replaceState(null, '', '#' + activeId); } catch(e){}
    }

    prevBtn.addEventListener('click', function(){ goTo(current - 1); });
    nextBtn.addEventListener('click', function(){ goTo(current + 1); });

    // Keyboard navigation
    document.addEventListener('keydown', function(e){
      if (e.target && (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.isContentEditable)) return;
      if (e.key === 'ArrowRight') { goTo(current + 1); }
      else if (e.key === 'ArrowLeft') { goTo(current - 1); }
    });

    // Swipe support for mobile
    var touchStartX = 0, touchStartY = 0, touchActive = false;
    document.addEventListener('touchstart', function(e){
      if (!e.touches.length) return;
      touchStartX = e.touches[0].clientX;
      touchStartY = e.touches[0].clientY;
      touchActive = true;
    }, { passive: true });
    document.addEventListener('touchend', function(e){
      if (!touchActive) return;
      touchActive = false;
      var t = e.changedTouches[0];
      var dx = t.clientX - touchStartX;
      var dy = t.clientY - touchStartY;
      if (Math.abs(dx) > 60 && Math.abs(dx) > Math.abs(dy) * 1.5) {
        if (dx < 0) goTo(current + 1);
        else goTo(current - 1);
      }
    }, { passive: true });

    // Intercept anchor clicks within page (a[href^="#"]) to navigate panels
    document.addEventListener('click', function(e){
      var a = e.target.closest && e.target.closest('a[href^="#"]');
      if (!a) return;
      var hash = a.getAttribute('href');
      if (hash === '#' || hash === '#top') {
        e.preventDefault();
        goTo(0);
        return;
      }
      var targetId = hash.slice(1);
      var panelId = ANCHOR_MAP[targetId] || targetId;
      var panelIdx = -1;
      INTERNAL_PANELS.forEach(function(p, i){ if (p.id === panelId) panelIdx = i; });
      if (panelIdx >= 0) {
        e.preventDefault();
        goTo(panelIdx);
      }
    });

    // Brand click → home. On the home page (index.html or '/'), always jump
    // to the first panel and clear any hash, no matter what the user clicked
    // before. On other pages, let the browser navigate to index.html normally.
    var brand = document.querySelector('[data-deck-home]');
    if (brand) brand.addEventListener('click', function(e){
      var pathname = location.pathname.split('/').pop();
      var onHome = (pathname === '' || pathname === 'index.html');
      if (onHome) {
        e.preventDefault();
        try { history.replaceState(null, '', location.pathname); } catch(err){}
        goTo(0);
      }
      // else: anchor href ("index.html") triggers a normal navigation
    });

    // The ES/EN switcher is injected by praxia-i18n.js into #praxia-header-actions.
    // No extra wiring is needed here.

    // Initial panel from hash if any
    var initial = 0;
    if (location.hash) {
      var h = location.hash.slice(1);
      var pid = ANCHOR_MAP[h] || h;
      INTERNAL_PANELS.forEach(function(p, i){ if (p.id === pid) initial = i; });
    }
    goTo(initial);
  });
})();
