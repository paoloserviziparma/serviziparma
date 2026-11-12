/* Sistemi Parma – script del sito (nessuna dipendenza, nessun cookie) */
(function () {
  'use strict';
  var doc = document.documentElement;
  doc.classList.add('js');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var isMobile = function () { return window.matchMedia('(max-width: 768px)').matches; };

  /* ---------- Menu mobile ---------- */
  var header = document.querySelector('.site-header');
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('nav');
  function closeMenu() {
    if (!toggle) return;
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Apri il menu');
    nav.classList.remove('is-open');
  }
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', open ? 'false' : 'true');
      toggle.setAttribute('aria-label', open ? 'Apri il menu' : 'Chiudi il menu');
      nav.classList.toggle('is-open', !open);
      if (!open && header) header.classList.remove('is-hidden');
    });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) closeMenu(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeMenu(); });
  }

  /* ---------- Header che sparisce scorrendo giù e ricompare su ---------- */
  var lastY = window.scrollY, ticking = false;
  function onScroll() {
    var y = window.scrollY;
    if (header) {
      var menuOpen = toggle && toggle.getAttribute('aria-expanded') === 'true';
      if (y < 80 || menuOpen) header.classList.remove('is-hidden');
      else if (y > lastY + 4) header.classList.add('is-hidden');
      else if (y < lastY - 4) header.classList.remove('is-hidden');
    }
    lastY = y;
    parallax();
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { window.requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });
  if (header) header.addEventListener('focusin', function () { header.classList.remove('is-hidden'); });

  /* ---------- Parallax leggero (dimezzato su mobile) ---------- */
  var pEls = Array.prototype.slice.call(document.querySelectorAll('[data-parallax]'));
  function parallax() {
    if (reduce || !pEls.length) return;
    var vh = window.innerHeight, k = isMobile() ? 0.5 : 1;
    pEls.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.bottom < -200 || r.top > vh + 200) return;
      var speed = parseFloat(el.getAttribute('data-parallax')) || 0.1;
      var offset = (r.top + r.height / 2 - vh / 2) * -speed * k;
      el.style.transform = 'translate3d(0,' + offset.toFixed(1) + 'px,0)';
    });
  }
  parallax();

  /* ---------- Titoli parola per parola ---------- */
  var splits = document.querySelectorAll('.js-split');
  Array.prototype.forEach.call(splits, function (el) {
    if (reduce) return;
    var words = el.textContent.trim().split(/\s+/);
    el.setAttribute('aria-label', el.textContent.trim());
    el.textContent = '';
    words.forEach(function (w, i) {
      var s = document.createElement('span');
      s.className = 'w';
      s.setAttribute('aria-hidden', 'true');
      s.style.transitionDelay = (i * 0.06).toFixed(2) + 's';
      s.textContent = w;
      el.appendChild(s);
      if (i < words.length - 1) el.appendChild(document.createTextNode(' '));
    });
    el.classList.add('split-words');
  });

  /* ---------- Comparsa allo scroll (IntersectionObserver) ---------- */
  var targets = document.querySelectorAll('.reveal, .split-words');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    Array.prototype.forEach.call(targets, function (t) { io.observe(t); });
  } else {
    Array.prototype.forEach.call(targets, function (t) { t.classList.add('is-in'); });
  }

  /* ---------- Finestra video (si carica solo al clic) ---------- */
  var modal, lastFocus;
  function openVideo(src, title) {
    lastFocus = document.activeElement;
    modal = document.createElement('div');
    modal.className = 'modal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.setAttribute('aria-label', title || 'Video');
    var frame;
    if (/youtube(-nocookie)?\.com|youtu\.be/.test(src)) {
      var id = (src.match(/(?:embed\/|v=|youtu\.be\/)([\w-]{6,})/) || [])[1];
      frame = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="' + (title || 'Video') + '" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>';
    } else if (/vimeo\.com/.test(src)) {
      var vid = (src.match(/vimeo\.com\/(?:video\/)?(\d+)/) || [])[1];
      frame = '<iframe src="https://player.vimeo.com/video/' + vid + '?autoplay=1&dnt=1" title="' + (title || 'Video') + '" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>';
    } else {
      frame = '<video src="' + src + '" controls autoplay playsinline></video>';
    }
    modal.innerHTML = '<div class="modal__box"><button type="button" class="modal__close" aria-label="Chiudi il video">&times;</button><div class="modal__frame">' + frame + '</div></div>';
    document.body.appendChild(modal);
    document.body.classList.add('modal-open');
    var btn = modal.querySelector('.modal__close');
    btn.focus();
    btn.addEventListener('click', closeVideo);
    modal.addEventListener('click', function (e) { if (e.target === modal) closeVideo(); });
  }
  function closeVideo() {
    if (!modal) return;
    modal.remove(); modal = null;
    document.body.classList.remove('modal-open');
    if (lastFocus) lastFocus.focus();
  }
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeVideo(); });
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-video]');
    if (!b) return;
    e.preventDefault();
    openVideo(b.getAttribute('data-video'), b.getAttribute('data-title'));
  });

  /* ---------- Eventbrite: lo script esterno si carica solo al clic ---------- */
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-eventbrite]');
    if (!b) return;
    e.preventDefault();
    var id = b.getAttribute('data-eventbrite');
    var start = function () {
      window.EBWidgets.createWidget({ widgetType: 'checkout', eventId: id, modal: true, modalTriggerElementId: b.id });
      b.click();
    };
    if (window.EBWidgets) { return; }
    var s = document.createElement('script');
    s.src = 'https://www.eventbrite.it/static/widgets/eb_widgets.js';
    s.onload = start;
    s.onerror = function () { window.location.href = 'https://www.eventbrite.it/e/' + id; };
    document.head.appendChild(s);
  });

  /* ---------- Precompilazione moduli da URL ---------- */
  var params = new URLSearchParams(window.location.search);
  var map = { prodotto: 'prodotto', corso: 'corso', nota: 'messaggio' };
  Object.keys(map).forEach(function (k) {
    var v = params.get(k);
    if (!v) return;
    var el = document.querySelector('form [name="' + map[k] + '"]');
    if (!el) return;
    if (el.tagName === 'SELECT') {
      var found = Array.prototype.some.call(el.options, function (o) { if (o.value === v) { o.selected = true; return true; } return false; });
      if (!found) { var o = new Option(v, v, true, true); el.add(o); }
    } else if (!el.value) { el.value = v; }
  });

  /* ---------- Selettore "Quale software fa per te?" ---------- */
  var sel = document.getElementById('selettore-form');
  if (sel) {
    var needs = {
      studio: [['contabilita', 'Contabilità, fiscale e bilanci'], ['paghe', 'Paghe e personale'], ['organizzazione', 'Organizzare lo studio']],
      azienda: [['contabilita', 'Contabilità, vendite e magazzino'], ['processi', 'Processi completi: logistica, produzione, analitica'], ['commercialista', 'Lavoro insieme al mio commercialista'], ['paghe', 'Paghe e personale']],
      ditta: [['fatture', 'Fatture elettroniche'], ['commercialista', 'Lavoro insieme al mio commercialista']]
    };
    /* I prodotti e gli indirizzi arrivano dalla pagina: così restano corretti
       anche nelle anteprime servite in una sottocartella (percorsi relativi). */
    var dati = document.getElementById('sel-prodotti');
    var products = dati ? JSON.parse(dati.textContent) : {};
    var urlContatti = sel.getAttribute('data-url-contatti') || '/contatti/';
    var needBox = document.getElementById('sel-bisogno');
    var out = { name: document.getElementById('sel-nome'), desc: document.getElementById('sel-desc'), cta: document.getElementById('sel-cta'), more: document.getElementById('sel-more') };
    function val(n) { var c = sel.querySelector('input[name="' + n + '"]:checked'); return c ? c.value : ''; }
    function renderNeeds() {
      var who = val('chi') || 'studio';
      var current = val('bisogno');
      needBox.innerHTML = '';
      needs[who].forEach(function (n, i) {
        var l = document.createElement('label'); l.className = 'chip';
        var checked = current ? current === n[0] : i === 0;
        l.innerHTML = '<input type="radio" name="bisogno" value="' + n[0] + '"' + (checked ? ' checked' : '') + '><span>' + n[1] + '</span>';
        needBox.appendChild(l);
      });
      if (!sel.querySelector('input[name="bisogno"]:checked')) needBox.querySelector('input').checked = true;
    }
    function update() {
      var key = val('chi') + '-' + val('bisogno');
      var p = products[key] || products['studio-contabilita'];
      var cloud = val('dove') === 'cloud';
      var name = p[0] + (cloud ? ' in cloud' : '');
      out.name.textContent = name;
      out.desc.textContent = p[2] + (cloud ? ' Con Sistemi in Rete lo usi dal web, senza server in ufficio.' : '');
      var extra = (document.getElementById('sel-settore').value || '').trim();
      var utenti = (document.getElementById('sel-utenti').value || '').trim();
      var nota = 'Vorrei una demo di ' + name + '.' + (extra ? ' Settore/attività: ' + extra + '.' : '') + (utenti ? ' Utenti previsti: ' + utenti + '.' : '');
      var optName = { 'PROFIS': 'Profis', 'STUDIO': 'Studio', 'JOB': 'Job', 'SPRING': 'Spring', 'eSOLVER': 'eSolver', 'PROFIS AZ': 'Profis AZ', 'QUADRA': 'Quadra' }[p[0]] || p[0];
      out.cta.href = urlContatti + (urlContatti.indexOf('?') > -1 ? '&' : '?') + 'prodotto=' + encodeURIComponent(optName) + '&nota=' + encodeURIComponent(nota) + '#modulo';
      out.cta.textContent = 'Richiedi una demo di ' + p[0];
      out.more.href = p[1];
    }
    sel.addEventListener('change', function (e) {
      if (e.target.name === 'chi') renderNeeds();
      update();
    });
    sel.addEventListener('input', function (e) { if (e.target.type === 'text' || e.target.type === 'number') update(); });
    renderNeeds(); update();
  }

  /* ---------- Anno nel footer ---------- */
  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
})();
