(function () {
  'use strict';
  const { categories, products, brands } = window.KDATA;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const main = $('#main');
  const eur = n => n.toLocaleString('el-GR', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' €';
  const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const norm = s => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  const catBy = slug => categories.find(c => c.slug === slug);
  const prodBy = id => products.find(p => p.id === +id);
  const bg = h => `background: linear-gradient(145deg, hsl(${h} 70% 95%), hsl(${h} 60% 88%))`;

  // ---------- persistent state (per-browser only) ----------
  const store = {
    get(k, d) { try { return JSON.parse(localStorage.getItem('kal_' + k)) ?? d; } catch { return d; } },
    set(k, v) { try { localStorage.setItem('kal_' + k, JSON.stringify(v)); } catch { /* storage unavailable */ } }
  };
  let favs = new Set(store.get('favs', []));
  let cart = store.get('cart', []); // [{id, shop, qty}]
  let recent = store.get('recent', []);

  function bump(el, n) {
    el.textContent = n; el.hidden = n === 0;
    el.classList.remove('pop'); void el.offsetWidth; el.classList.add('pop');
  }
  function syncBadges() {
    bump($('#favCount'), favs.size);
    bump($('#cartCount'), cart.reduce((a, c) => a + c.qty, 0));
  }
  function toast(msg) {
    const t = $('#toast'); t.textContent = msg; t.classList.add('is-on');
    clearTimeout(toast.t); toast.t = setTimeout(() => t.classList.remove('is-on'), 2200);
  }

  // ---------- theme ----------
  const savedTheme = store.get('theme', null);
  if (savedTheme) document.documentElement.dataset.theme = savedTheme;
  $('#themeBtn').addEventListener('click', () => {
    const dark = document.documentElement.dataset.theme === 'dark' ||
      (!document.documentElement.dataset.theme && matchMedia('(prefers-color-scheme: dark)').matches);
    document.documentElement.dataset.theme = dark ? 'light' : 'dark';
    store.set('theme', document.documentElement.dataset.theme);
  });

  // ---------- components ----------
  function stars(r, n) {
    const full = Math.round(r);
    return `<span class="stars" aria-label="${r} από 5"><i>${'★'.repeat(full)}${'☆'.repeat(5 - full)}</i>${r.toFixed(1)} (${n.toLocaleString('el-GR')})</span>`;
  }
  function card(p) {
    return `<article class="card">
      ${p.discount ? `<span class="card__disc">-${p.discount}%</span>` : ''}
      <button class="card__fav ${favs.has(p.id) ? 'is-on' : ''}" data-fav="${p.id}" aria-pressed="${favs.has(p.id)}" aria-label="Αγαπημένα">${favs.has(p.id) ? '♥' : '♡'}</button>
      <a href="#/p/${p.id}" class="card__img" style="${bg(p.hue)}" aria-hidden="true" tabindex="-1">${p.icon}</a>
      <a href="#/p/${p.id}" class="card__name">${esc(p.name)}</a>
      ${stars(p.rating, p.reviews)}
      <div class="card__price">
        <div class="from">από</div>
        <div><span class="price">${eur(p.min)}</span>${p.oldPrice ? `<span class="old">${eur(p.oldPrice)}</span>` : ''}</div>
        <div class="shops">σε ${p.shops.length} καταστήματα</div>
        ${p.shops.some(s => s.plus) ? '<span class="plus-tag">✓ Plus δωρεάν μεταφορικά</span>' : ''}
      </div>
    </article>`;
  }
  function row(title, list, link) {
    const id = 'r' + Math.random().toString(36).slice(2, 8);
    return `<section class="section">
      <div class="section__head"><h2>${title}</h2>${link ? `<a href="${link}">Δες όλα ›</a>` : ''}</div>
      <div class="row">
        <button class="car-arrow car-arrow--l" data-scroll="${id}" data-dir="-1" aria-label="Προηγούμενα">‹</button>
        <div class="track" id="${id}">${list.map(card).join('')}</div>
        <button class="car-arrow car-arrow--r" data-scroll="${id}" data-dir="1" aria-label="Επόμενα">›</button>
      </div></section>`;
  }
  function wireRows() {
    $$('.track').forEach(t => {
      const upd = () => {
        const l = $(`[data-scroll="${t.id}"][data-dir="-1"]`), r = $(`[data-scroll="${t.id}"][data-dir="1"]`);
        if (l) l.disabled = t.scrollLeft < 5;
        if (r) r.disabled = t.scrollLeft + t.clientWidth >= t.scrollWidth - 5;
      };
      t.addEventListener('scroll', upd, { passive: true }); upd();
    });
  }

  // ---------- views ----------
  const slidesData = [
    { k: 'Black Friday εβδομάδα', t: 'Έως -50% σε Τεχνολογία', p: 'Χιλιάδες προσφορές από εκατοντάδες καταστήματα.', a: '💻', c: 'linear-gradient(120deg,#1d1d24,#3a2a5c)', l: '#/deals' },
    { k: 'Νέο', t: 'Χειμερινή κουζίνα, ζεστά πιάτα', p: 'Air fryers, μηχανές espresso και σκεύη.', a: '☕', c: 'linear-gradient(120deg,#f68b24,#e2373f)', l: '#/c/home' },
    { k: 'Δώρα Χριστουγέννων', t: 'Ιδέες για όλη την οικογένεια', p: 'LEGO, επιτραπέζια και gadgets κάτω από 50€.', a: '🎁', c: 'linear-gradient(120deg,#0f7b5f,#1a9b55)', l: '#/c/kids' },
    { k: 'kalathi Plus', t: 'Δωρεάν μεταφορικά, όλο τον χρόνο', p: 'Δοκίμασε 30 ημέρες χωρίς χρέωση.', a: '🚚', c: 'linear-gradient(120deg,#4b22c9,#9b6bff)', l: '#/plus' }
  ];
  function home() {
    const deals = products.filter(p => p.discount).sort((a, b) => b.discount - a.discount);
    const popular = [...products].sort((a, b) => b.reviews - a.reviews).slice(0, 12);
    const tech = products.filter(p => p.cat === 'tech');
    const recentList = recent.map(prodBy).filter(Boolean);
    main.innerHTML = `<div class="wrap">
      <div class="hero">
        <div class="carousel" id="car" aria-roledescription="carousel">
          <div class="slides">${slidesData.map((s, i) => `<div class="slide" style="background:${s.c}" aria-label="${i + 1} από ${slidesData.length}">
            <div class="slide__txt"><span class="slide__kicker">${s.k}</span><h3>${s.t}</h3><p>${s.p}</p><a class="btn btn--white" href="${s.l}">Δες τις προσφορές</a></div>
            <span class="slide__art" aria-hidden="true">${s.a}</span></div>`).join('')}</div>
          <button class="car-arrow car-arrow--l" aria-label="Προηγούμενο">‹</button>
          <button class="car-arrow car-arrow--r" aria-label="Επόμενο">›</button>
          <div class="dots">${slidesData.map((_, i) => `<button aria-label="Slide ${i + 1}"></button>`).join('')}</div>
        </div>
        <div class="hero__side">
          <a class="promo promo--plus" href="#/plus"><h4>kalathi Plus</h4><p>Δωρεάν αποστολή & επιστροφή σε εκατομμύρια προϊόντα</p><span class="art">🚚</span></a>
          <a class="promo promo--deal" href="#/deals"><h4>Προσφορές ημέρας</h4><p>Νέες εκπτώσεις κάθε μέρα στις 10:00</p><span class="art">🔥</span></a>
        </div>
      </div>
      <div class="usp">
        <div><span class="ico">🔍</span><span><b>Σύγκρινε τιμές</b>από ${new Set(products.flatMap(p => p.shops.map(s => s.name))).size} καταστήματα</span></div>
        <div><span class="ico">🛡️</span><span><b>Αγορά με ασφάλεια</b>Προστασία αγοραστή</span></div>
        <div><span class="ico">🔔</span><span><b>Ειδοποίηση τιμής</b>Μάθε πότε πέφτει</span></div>
        <div><span class="ico">↩️</span><span><b>Εύκολες επιστροφές</b>Έως 30 ημέρες</span></div>
      </div>
      ${recentList.length ? row('Είδες πρόσφατα', recentList) : ''}
      <section class="section"><div class="section__head"><h2>Δημοφιλείς κατηγορίες</h2></div>
        <div class="cats">${categories.map(c => `<a class="cat" href="#/c/${c.slug}"><div class="cat__ico">${c.icon}</div>${c.name}</a>`).join('')}</div></section>
      ${row('🔥 Κορυφαίες προσφορές', deals, '#/deals')}
      ${row('Δημοφιλή αυτή την εβδομάδα', popular)}
      ${row('Τεχνολογία που ξεχωρίζει', tech, '#/c/tech')}
      <div class="banner"><div><h3>Μην χάσεις καμία πτώση τιμής</h3><p>Πρόσθεσε προϊόντα στις λίστες σου και θα σε ειδοποιήσουμε.</p></div><a href="#/favorites" class="btn">Οι λίστες μου</a></div>
      <section class="section"><div class="section__head"><h2>Δημοφιλή brands</h2></div>
        <div class="brands">${brands.map(b => `<a class="brand" href="#/search?q=${encodeURIComponent(b)}">${b}</a>`).join('')}</div></section>
    </div>`;
    wireCarousel($('#car'));
    wireRows();
  }

  function wireCarousel(el) {
    const slides = $('.slides', el), dots = $$('.dots button', el), n = dots.length;
    let i = 0, timer;
    const go = k => { i = (k + n) % n; slides.style.transform = `translateX(-${i * 100}%)`; dots.forEach((d, j) => d.classList.toggle('is-on', j === i)); };
    const auto = () => { clearInterval(timer); timer = setInterval(() => document.contains(el) ? go(i + 1) : clearInterval(timer), 5000); };
    $('.car-arrow--l', el).onclick = () => { go(i - 1); auto(); };
    $('.car-arrow--r', el).onclick = () => { go(i + 1); auto(); };
    dots.forEach((d, j) => d.onclick = () => { go(j); auto(); });
    let x0 = null;
    el.addEventListener('touchstart', e => x0 = e.touches[0].clientX, { passive: true });
    el.addEventListener('touchend', e => { if (x0 === null) return; const dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 40) { go(i + (dx < 0 ? 1 : -1)); auto(); } x0 = null; });
    el.addEventListener('mouseenter', () => clearInterval(timer));
    el.addEventListener('mouseleave', auto);
    go(0); auto();
  }

  let listState = { sort: 'pop', min: '', max: '', subs: new Set(), plus: false, deal: false };
  function listing(title, base, crumbs) {
    const subsAvail = [...new Set(base.map(p => p.sub))];
    const render = () => {
      let list = base.filter(p =>
        (!listState.subs.size || listState.subs.has(p.sub)) &&
        (!listState.min || p.min >= +listState.min) && (!listState.max || p.min <= +listState.max) &&
        (!listState.plus || p.shops.some(s => s.plus)) && (!listState.deal || p.discount));
      const sorters = { pop: (a, b) => b.reviews - a.reviews, asc: (a, b) => a.min - b.min, desc: (a, b) => b.min - a.min, rating: (a, b) => b.rating - a.rating };
      list.sort(sorters[listState.sort]);
      $('#count').textContent = `${list.length} προϊόντα`;
      $('#grid').innerHTML = list.length ? list.map(card).join('') :
        `<div class="empty" style="grid-column:1/-1"><div>🔎</div><p>Δεν βρέθηκαν προϊόντα με αυτά τα φίλτρα.</p><button class="btn btn--ghost" id="clearF">Καθαρισμός φίλτρων</button></div>`;
      const c = $('#clearF'); if (c) c.onclick = () => { listState = { ...listState, min: '', max: '', subs: new Set(), plus: false, deal: false }; listing(title, base, crumbs); };
    };
    main.innerHTML = `<div class="wrap">
      <div class="crumbs"><a href="#/">Αρχική</a> › ${crumbs}</div>
      <div class="listing">
        <aside class="filters" id="filters" aria-label="Φίλτρα">
          <h4>Τιμή (€)</h4>
          <div class="price-in"><input id="fmin" type="number" inputmode="decimal" placeholder="Από" value="${listState.min}"><input id="fmax" type="number" inputmode="decimal" placeholder="Έως" value="${listState.max}"></div>
          ${subsAvail.length > 1 ? `<h4>Κατηγορία</h4>${subsAvail.map(s => `<label><input type="checkbox" data-sub="${esc(s)}" ${listState.subs.has(s) ? 'checked' : ''}> ${esc(s)}</label>`).join('')}` : ''}
          <h4>Επιλογές</h4>
          <label><input type="checkbox" id="fplus" ${listState.plus ? 'checked' : ''}> Δωρεάν μεταφορικά Plus</label>
          <label><input type="checkbox" id="fdeal" ${listState.deal ? 'checked' : ''}> Μόνο προσφορές</label>
        </aside>
        <div>
          <div class="list-head">
            <h1>${esc(title)}<small id="count"></small></h1>
            <div class="sort" role="group" aria-label="Ταξινόμηση">
              <button class="btn--ghost filter-toggle" id="ftoggle" style="border-radius:20px">⚙ Φίλτρα</button>
              ${[['pop', 'Δημοφιλέστερα'], ['asc', 'Φθηνότερα'], ['desc', 'Ακριβότερα'], ['rating', 'Βαθμολογία']].map(([k, l]) => `<button data-sort="${k}" class="${listState.sort === k ? 'is-on' : ''}">${l}</button>`).join('')}
            </div>
          </div>
          <div class="grid" id="grid"></div>
        </div>
      </div></div>`;
    $$('[data-sort]').forEach(b => b.onclick = () => { listState.sort = b.dataset.sort; $$('[data-sort]').forEach(x => x.classList.toggle('is-on', x === b)); render(); });
    $$('[data-sub]').forEach(b => b.onchange = () => { b.checked ? listState.subs.add(b.dataset.sub) : listState.subs.delete(b.dataset.sub); render(); });
    $('#fmin').oninput = e => { listState.min = e.target.value; render(); };
    $('#fmax').oninput = e => { listState.max = e.target.value; render(); };
    $('#fplus').onchange = e => { listState.plus = e.target.checked; render(); };
    $('#fdeal').onchange = e => { listState.deal = e.target.checked; render(); };
    $('#ftoggle').onclick = () => $('#filters').classList.toggle('is-open');
    render();
  }

  function priceHistory(p) {
    let v = p.min * 1.15; const pts = [];
    for (let i = 0; i < 30; i++) { v = Math.max(p.min * 0.97, v + (Math.sin(i * 1.7 + p.id) * 0.03 - 0.008) * p.min); pts.push(v); }
    pts[29] = p.min;
    const lo = Math.min(...pts), hi = Math.max(...pts), W = 600, H = 150;
    const xy = pts.map((y, i) => [i / 29 * W, H - 10 - (y - lo) / (hi - lo || 1) * (H - 30)]);
    const d = xy.map((q, i) => (i ? 'L' : 'M') + q[0].toFixed(1) + ' ' + q[1].toFixed(1)).join(' ');
    return `<div class="chart"><div class="section__head"><h2 style="font-size:17px">Ιστορικό τιμής (30 ημέρες)</h2><span class="shops">Χαμηλότερη: <b>${eur(lo)}</b></span></div>
      <svg viewBox="0 0 ${W} ${H}" preserveAspectRatio="none" role="img" aria-label="Γράφημα τιμής">
        <defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f68b24" stop-opacity=".3"/><stop offset="1" stop-color="#f68b24" stop-opacity="0"/></linearGradient></defs>
        <path d="${d} L${W} ${H} L0 ${H}Z" fill="url(#g)"/><path d="${d}" fill="none" stroke="#f68b24" stroke-width="2.5" vector-effect="non-scaling-stroke"/>
      </svg></div>`;
  }

  function pdp(id) {
    const p = prodBy(id);
    if (!p) return notFound();
    recent = [p.id, ...recent.filter(x => x !== p.id)].slice(0, 10); store.set('recent', recent);
    const c = catBy(p.cat);
    const best = p.shops[0];
    const related = products.filter(x => x.cat === p.cat && x.id !== p.id);
    main.innerHTML = `<div class="wrap">
      <div class="crumbs"><a href="#/">Αρχική</a> › <a href="#/c/${c.slug}">${c.name}</a> › ${esc(p.sub)}</div>
      <div class="pdp">
        <div class="pdp__img" style="${bg(p.hue)}">${p.icon}</div>
        <div>
          <h1>${esc(p.name)}</h1>
          ${stars(p.rating, p.reviews)}
          <div class="pdp__best">
            <div class="from">Χαμηλότερη τιμή από ${p.shops.length} καταστήματα</div>
            <span class="price">${eur(p.min)}</span>${p.oldPrice ? `<span class="old">${eur(p.oldPrice)}</span>` : ''}
            <div class="shops">στο <b>${esc(best.name)}</b> · ${best.shipping ? 'μεταφορικά ' + eur(best.shipping) : 'δωρεάν μεταφορικά'}</div>
            <div class="pdp__acts">
              <button class="btn" data-add="${p.id}" data-shop="0">🛒 Προσθήκη στο καλάθι</button>
              <button class="btn btn--ghost" data-fav="${p.id}" aria-pressed="${favs.has(p.id)}">${favs.has(p.id) ? '♥ Στις λίστες' : '♡ Αποθήκευση'}</button>
              <button class="btn btn--ghost" data-alert>🔔 Ειδοποίηση τιμής</button>
            </div>
          </div>
          <table class="spec"><tbody>
            <tr><td>Κατηγορία</td><td>${esc(p.sub)}</td></tr>
            <tr><td>Εύρος τιμών</td><td>${eur(p.min)} – ${eur(p.shops[p.shops.length - 1].price)}</td></tr>
            <tr><td>Διαθεσιμότητα</td><td>${best.stock}</td></tr>
            <tr><td>Κωδικός</td><td>KAL-${String(p.id).padStart(6, '0')}</td></tr>
          </tbody></table>
        </div>
      </div>
      <section class="offers section"><div class="section__head"><h2>Σύγκριση τιμών σε ${p.shops.length} καταστήματα</h2></div>
        ${p.shops.map((s, i) => `<div class="offer ${i === 0 ? 'is-best' : ''}">
          <div class="offer__shop"><b>${esc(s.name)}</b><span>★ ${s.rating} · ${s.stock}</span></div>
          <div class="offer__ship">${s.shipping ? 'Μεταφορικά ' + eur(s.shipping) : '<span class="ok">Δωρεάν μεταφορικά</span>'}${s.plus ? '<br><span class="plus-tag">✓ Plus</span>' : ''}</div>
          <div><span class="price">${eur(s.price)}</span><div class="shops">Σύνολο ${eur(s.price + s.shipping)}</div></div>
          <button class="btn ${i === 0 ? '' : 'btn--ghost'}" data-add="${p.id}" data-shop="${i}">Αγορά</button>
        </div>`).join('')}
      </section>
      ${priceHistory(p)}
      ${related.length ? row('Παρόμοια προϊόντα', related, '#/c/' + c.slug) : ''}
    </div>`;
    wireRows();
  }

  function notFound() {
    main.innerHTML = `<div class="wrap"><div class="empty"><div>🧺</div><h2>Η σελίδα δεν βρέθηκε</h2><a class="btn" href="#/">Επιστροφή στην αρχική</a></div></div>`;
  }
  function info(title, body) {
    main.innerHTML = `<div class="wrap"><div class="empty"><div>🚚</div><h2>${title}</h2><p>${body}</p><a class="btn" href="#/">Συνέχεια αγορών</a></div></div>`;
  }

  // ---------- router ----------
  function route() {
    const h = location.hash.slice(1) || '/';
    const [path, qs] = h.split('?');
    const parts = path.split('/').filter(Boolean);
    const params = new URLSearchParams(qs || '');
    closeMega(); closeSuggest(); closeDrawers();
    listState.subs = new Set();
    if (!parts.length) home();
    else if (parts[0] === 'c' && catBy(parts[1])) { const c = catBy(parts[1]); listing(c.name, products.filter(p => p.cat === c.slug), c.name); }
    else if (parts[0] === 'p') pdp(parts[1]);
    else if (parts[0] === 'deals') listing('Προσφορές', products.filter(p => p.discount), 'Προσφορές');
    else if (parts[0] === 'favorites') {
      const list = products.filter(p => favs.has(p.id));
      if (list.length) listing('Οι λίστες μου', list, 'Λίστες');
      else info('Η λίστα σου είναι άδεια', 'Πάτα ♡ σε ένα προϊόν για να το αποθηκεύσεις εδώ.');
    }
    else if (parts[0] === 'search') {
      const q = params.get('q') || ''; $('#q').value = q;
      const nq = norm(q);
      const res = products.filter(p => norm(p.name + ' ' + p.sub + ' ' + catBy(p.cat).name).includes(nq));
      listing(`Αποτελέσματα για «${q}»`, res, 'Αναζήτηση');
    }
    else if (parts[0] === 'plus') info('kalathi Plus', 'Δωρεάν μεταφορικά και επιστροφές σε χιλιάδες προϊόντα. (demo)');
    else notFound();
    if (parts[0] !== 'search') $('#q').value = '';
    window.scrollTo({ top: 0, behavior: 'instant' in window ? 'instant' : 'auto' });
  }
  window.addEventListener('hashchange', route);

  // ---------- global delegated actions ----------
  document.addEventListener('click', e => {
    const fav = e.target.closest('[data-fav]');
    if (fav) {
      e.preventDefault();
      const id = +fav.dataset.fav;
      favs.has(id) ? favs.delete(id) : favs.add(id);
      store.set('favs', [...favs]); syncBadges();
      const on = favs.has(id);
      $$(`[data-fav="${id}"]`).forEach(b => {
        b.setAttribute('aria-pressed', on);
        if (b.classList.contains('card__fav')) { b.classList.toggle('is-on', on); b.textContent = on ? '♥' : '♡'; }
        else b.textContent = on ? '♥ Στις λίστες' : '♡ Αποθήκευση';
      });
      toast(on ? 'Προστέθηκε στις λίστες σου' : 'Αφαιρέθηκε από τις λίστες');
      return;
    }
    const add = e.target.closest('[data-add]');
    if (add) {
      const id = +add.dataset.add, shop = +add.dataset.shop;
      const ex = cart.find(c => c.id === id && c.shop === shop);
      ex ? ex.qty++ : cart.push({ id, shop, qty: 1 });
      store.set('cart', cart); syncBadges(); renderCart();
      toast('Προστέθηκε στο καλάθι ✓');
      return;
    }
    if (e.target.closest('[data-alert]')) { toast('🔔 Θα σε ειδοποιήσουμε όταν πέσει η τιμή (demo)'); return; }
    const sc = e.target.closest('[data-scroll]');
    if (sc) { const t = document.getElementById(sc.dataset.scroll); t.scrollBy({ left: +sc.dataset.dir * t.clientWidth * 0.9 }); return; }
    if (e.target.closest('[data-close]')) { closeDrawers(); $('#loginModal').hidden = true; }
  });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') { closeDrawers(); closeMega(); closeSuggest(); $('#loginModal').hidden = true; }
  });

  // ---------- header: sticky shadow ----------
  const hdr = $('#hdr');
  window.addEventListener('scroll', () => hdr.classList.toggle('is-scrolled', scrollY > 10), { passive: true });

  // ---------- mega menu ----------
  const mega = $('#mega'), catBtn = $('#catBtn');
  $('#megaList').innerHTML = categories.map((c, i) => `<li><a href="#/c/${c.slug}" data-mi="${i}"><span>${c.icon}</span>${c.name}</a></li>`).join('');
  function showPanel(i) {
    const c = categories[i];
    $$('#megaList a').forEach((a, j) => a.classList.toggle('is-active', j === i));
    $('#megaPanel').innerHTML = c.subs.map(([h, items]) => `<div><h4><a href="#/c/${c.slug}">${h}</a></h4>${items.map(s => `<a class="sub" href="#/search?q=${encodeURIComponent(s)}">${s}</a>`).join('')}</div>`).join('');
  }
  function openMega() { mega.hidden = false; catBtn.setAttribute('aria-expanded', 'true'); showPanel(0); }
  function closeMega() { mega.hidden = true; catBtn.setAttribute('aria-expanded', 'false'); }
  catBtn.addEventListener('click', () => mega.hidden ? openMega() : closeMega());
  let megaT;
  catBtn.addEventListener('mouseenter', () => { clearTimeout(megaT); megaT = setTimeout(openMega, 150); });
  catBtn.addEventListener('mouseleave', () => clearTimeout(megaT));
  hdr.addEventListener('mouseleave', () => { clearTimeout(megaT); megaT = setTimeout(closeMega, 250); });
  mega.addEventListener('mouseenter', () => clearTimeout(megaT));
  $('#megaList').addEventListener('mouseover', e => { const a = e.target.closest('[data-mi]'); if (a) showPanel(+a.dataset.mi); });
  $('#megaList').addEventListener('focusin', e => { const a = e.target.closest('[data-mi]'); if (a) showPanel(+a.dataset.mi); });

  // ---------- search with autosuggest ----------
  const q = $('#q'), sug = $('#suggest');
  let active = -1;
  function closeSuggest() { sug.hidden = true; active = -1; }
  function hl(text, term) {
    if (!term) return esc(text);
    const i = norm(text).indexOf(norm(term));
    return i < 0 ? esc(text) : esc(text.slice(0, i)) + '<mark>' + esc(text.slice(i, i + term.length)) + '</mark>' + esc(text.slice(i + term.length));
  }
  function renderSuggest() {
    const term = q.value.trim();
    let html = '';
    if (!term) {
      const pop = ['air fryer', 'ακουστικά', 'smartphone', 'lego', 'πατίνι'];
      html = `<h5>Δημοφιλείς αναζητήσεις</h5>` + pop.map(s => `<a href="#/search?q=${encodeURIComponent(s)}"><span class="s-ico">🔥</span>${s}</a>`).join('');
    } else {
      const nt = norm(term);
      const cats = [];
      categories.forEach(c => c.subs.forEach(([, items]) => items.forEach(s => { if (norm(s).includes(nt) && cats.length < 4) cats.push([s, c]); })));
      const prods = products.filter(p => norm(p.name).includes(nt) || norm(p.sub).includes(nt)).slice(0, 6);
      if (cats.length) html += `<h5>Κατηγορίες</h5>` + cats.map(([s, c]) => `<a href="#/search?q=${encodeURIComponent(s)}"><span class="s-ico">${c.icon}</span><span>${hl(s, term)} <span class="shops">σε ${c.name}</span></span></a>`).join('');
      if (prods.length) html += `<h5>Προϊόντα</h5>` + prods.map(p => `<a href="#/p/${p.id}"><span class="s-ico" style="${bg(p.hue)}">${p.icon}</span><span>${hl(p.name, term)}</span><span class="s-price">${eur(p.min)}</span></a>`).join('');
      html += `<a href="#/search?q=${encodeURIComponent(term)}"><span class="s-ico">🔍</span>Αναζήτηση για «<b>${esc(term)}</b>»</a>`;
    }
    sug.innerHTML = html; sug.hidden = false; active = -1;
  }
  q.addEventListener('focus', renderSuggest);
  q.addEventListener('input', renderSuggest);
  q.addEventListener('keydown', e => {
    const items = $$('a', sug);
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault(); if (sug.hidden) renderSuggest();
      active = (active + (e.key === 'ArrowDown' ? 1 : -1) + items.length) % items.length;
      items.forEach((a, i) => a.classList.toggle('is-active', i === active));
    } else if (e.key === 'Enter' && active >= 0 && items[active]) { e.preventDefault(); location.hash = items[active].getAttribute('href'); q.blur(); }
  });
  document.addEventListener('click', e => { if (!e.target.closest('.search')) closeSuggest(); });
  $('#searchForm').addEventListener('submit', e => {
    e.preventDefault();
    const term = q.value.trim(); if (!term) return;
    location.hash = '#/search?q=' + encodeURIComponent(term); q.blur();
  });

  // ---------- drawers / modal ----------
  function openDrawer(d) { d.classList.add('is-open'); d.setAttribute('aria-hidden', 'false'); document.body.style.overflow = 'hidden'; }
  function closeDrawers() { $$('.drawer').forEach(d => { d.classList.remove('is-open'); d.setAttribute('aria-hidden', 'true'); }); document.body.style.overflow = ''; $('#burger').setAttribute('aria-expanded', 'false'); }
  $('#cartBtn').addEventListener('click', () => { renderCart(); openDrawer($('#cartDrawer')); });
  $('#burger').addEventListener('click', () => { openDrawer($('#navDrawer')); $('#burger').setAttribute('aria-expanded', 'true'); });
  $('#navBody').innerHTML = `<a class="nav-cat" href="#/deals"><span>🔥</span><span>Προσφορές</span></a>` +
    categories.map(c => `<a class="nav-cat" href="#/c/${c.slug}"><span>${c.icon}</span><span>${c.name}</span></a>`).join('') +
    `<a class="nav-cat" href="#/favorites"><span>♡</span><span>Οι λίστες μου</span></a><a class="nav-cat" href="#/plus"><span>🚚</span><span>kalathi Plus</span></a>`;
  $('#loginBtn').addEventListener('click', () => { $('#loginModal').hidden = false; $('#loginModal button').focus(); });
  $('#loginModal').addEventListener('click', e => { if (e.target.id === 'loginModal') e.currentTarget.hidden = true; });

  function renderCart() {
    const body = $('#cartBody'), foot = $('#cartFoot');
    if (!cart.length) { body.innerHTML = `<div class="empty" style="box-shadow:none"><div>🛒</div><p>Το καλάθι σου είναι άδειο.</p></div>`; foot.innerHTML = ''; return; }
    let total = 0;
    body.innerHTML = cart.map((c, i) => {
      const p = prodBy(c.id), s = p.shops[c.shop] || p.shops[0];
      total += s.price * c.qty;
      return `<div class="ci"><div class="ci__img" style="${bg(p.hue)}">${p.icon}</div>
        <div><div class="ci__name">${esc(p.name)}</div><div class="ci__shop">από ${esc(s.name)}</div>
        <div class="qty"><button data-q="${i}" data-d="-1" aria-label="Λιγότερα">−</button><span>${c.qty}</span><button data-q="${i}" data-d="1" aria-label="Περισσότερα">+</button></div></div>
        <b>${eur(s.price * c.qty)}</b></div>`;
    }).join('');
    foot.innerHTML = `<div class="total"><span>Σύνολο</span><span>${eur(total)}</span></div><button class="btn btn--block" id="checkout">Ολοκλήρωση αγοράς</button>`;
    $$('[data-q]', body).forEach(b => b.onclick = () => {
      const c = cart[+b.dataset.q]; c.qty += +b.dataset.d;
      if (c.qty <= 0) cart.splice(+b.dataset.q, 1);
      store.set('cart', cart); syncBadges(); renderCart();
    });
    $('#checkout').onclick = () => toast('Demo: η ολοκλήρωση αγοράς δεν είναι ενεργή');
  }

  syncBadges();
  route();
})();
