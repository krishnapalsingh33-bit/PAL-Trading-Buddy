(() => {
  'use strict';

  const STYLE_ID = 'tdt-v21-premium-style';
  const HEATMAP_ID = 'tdt-v21-heatmap';
  const RED = '#8f1d22';

  const css = `
    :root{
      --v21-accent:#8f1d22;
      --v21-accent-2:#b3353b;
      --v21-accent-soft:#faeeee;
      --v21-line:#e3ded7;
      --v21-soft:#faf9f6;
      --v21-shadow:0 14px 36px rgba(0,0,0,.055);
    }
    html{scroll-behavior:smooth}
    body{transition:background-color .25s ease,color .25s ease}
    .side{box-shadow:14px 0 40px rgba(0,0,0,.09);z-index:3}
    .brand .logo{box-shadow:0 7px 20px rgba(255,255,255,.10);transition:transform .25s ease,box-shadow .25s ease}
    .brand .logo:hover{transform:translateY(-2px) rotate(-2deg);box-shadow:0 12px 30px rgba(255,255,255,.16)}
    .nav button{transition:background .2s ease,color .2s ease,transform .2s ease,box-shadow .2s ease}
    .nav button:hover{transform:translateX(2px)}
    .main{animation:v21PageIn .38s cubic-bezier(.2,.8,.2,1) both}
    @keyframes v21PageIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
    .card,.stat,.day,.trade,.btn,.row{transition:transform .22s ease,box-shadow .22s ease,border-color .22s ease,background-color .22s ease}
    .card:hover,.stat:hover{transform:translateY(-2px);box-shadow:var(--v21-shadow)}
    .trade:hover{border-color:#d1c9bf;box-shadow:0 10px 28px rgba(0,0,0,.045)}
    .day:hover{transform:translateY(-1px);box-shadow:0 10px 24px rgba(0,0,0,.05)}
    .btn:hover{transform:translateY(-1px)}
    .btn.primary{box-shadow:0 7px 18px rgba(143,29,34,.16)}
    .btn.primary:hover{box-shadow:0 10px 24px rgba(143,29,34,.23)}
    .stat b{transition:color .2s ease,transform .2s ease}.stat:hover b{color:var(--v21-accent);transform:translateY(-1px)}
    .ring{overflow:visible;box-shadow:0 12px 28px rgba(143,29,34,.08);animation:v21RingFloat 4.8s ease-in-out infinite}
    .ring:before{content:"";position:absolute;inset:-10px;border-radius:50%;background:conic-gradient(var(--v21-accent) calc(var(--v21-score,0)*1%),#ece9e4 0);-webkit-mask:radial-gradient(farthest-side,transparent calc(100% - 10px),#000 0);mask:radial-gradient(farthest-side,transparent calc(100% - 10px),#000 0);filter:drop-shadow(0 3px 8px rgba(143,29,34,.15));transition:background .7s cubic-bezier(.2,.8,.2,1)}
    .ring:after{display:none}
    @keyframes v21RingFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-2px)}}
    .v21-kicker{display:inline-flex;align-items:center;gap:7px;font-size:8px;font-weight:900;letter-spacing:.12em;text-transform:uppercase;color:#77736e;margin-bottom:7px}
    .v21-kicker:before{content:"";width:7px;height:7px;border-radius:50%;background:var(--v21-accent);box-shadow:0 0 0 4px var(--v21-accent-soft)}
    .v21-heat-card{margin-top:14px;padding:17px;background:rgba(255,255,255,.96);border:1px solid var(--v21-line);border-radius:16px;box-shadow:0 12px 30px rgba(0,0,0,.05);backdrop-filter:blur(8px)}
    .v21-heat-head{display:flex;justify-content:space-between;align-items:flex-end;gap:10px;margin-bottom:13px}
    .v21-heat-head strong{font-size:13px}.v21-heat-head span{font-size:9px;color:#77736e}
    .v21-heat-wrap{overflow:auto;padding-bottom:2px}.v21-heat-grid{display:grid;grid-auto-flow:column;grid-template-rows:repeat(7,12px);grid-auto-columns:12px;gap:4px;min-width:max-content}
    .v21-heat-cell{width:12px;height:12px;border-radius:3px;background:#ece9e4;box-shadow:inset 0 0 0 1px rgba(0,0,0,.025);transition:transform .15s ease,filter .15s ease}
    .v21-heat-cell:hover{transform:scale(1.4);filter:brightness(.96)}
    .v21-heat-cell[data-level="1"]{background:#f1ddde}.v21-heat-cell[data-level="2"]{background:#ddaeb1}.v21-heat-cell[data-level="3"]{background:#bd6e73}.v21-heat-cell[data-level="4"]{background:#8f1d22}
    .v21-heat-legend{display:flex;align-items:center;gap:5px;margin-top:10px;font-size:8px;color:#77736e}.v21-heat-legend .v21-heat-cell{display:inline-block}
    .v21-metric-strip{display:grid;grid-template-columns:repeat(3,1fr);gap:9px;margin-top:10px}.v21-metric{padding:10px;border:1px solid #ece9e4;border-radius:10px;background:var(--v21-soft)}.v21-metric small{display:block;font-size:8px;text-transform:uppercase;letter-spacing:.07em;color:#77736e}.v21-metric b{display:block;font-size:14px;margin-top:4px}
    .v21-review-strip{display:grid;grid-template-columns:repeat(3,1fr);gap:9px;margin-top:14px}.v21-review-card{padding:12px;border:1px solid #ece9e4;border-radius:11px;background:linear-gradient(135deg,#fff,#faf9f6)}.v21-review-card small{font-size:8px;color:#77736e;text-transform:uppercase;letter-spacing:.07em}.v21-review-card b{display:block;font-size:18px;margin-top:5px}.v21-bar{margin-top:7px;height:6px;background:#ece9e4;border-radius:99px;overflow:hidden}.v21-bar span{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--v21-accent),var(--v21-accent-2));border-radius:99px;transition:width .75s cubic-bezier(.2,.8,.2,1)}
    .v21-ripple{position:relative;overflow:hidden}.v21-ripple-wave{position:absolute;border-radius:50%;transform:scale(0);background:rgba(255,255,255,.42);animation:v21Ripple .55s ease-out;pointer-events:none}.btn:not(.primary) .v21-ripple-wave{background:rgba(0,0,0,.08)}@keyframes v21Ripple{to{transform:scale(3.5);opacity:0}}
    .toast{animation:v21Toast .24s cubic-bezier(.2,.8,.2,1) both}@keyframes v21Toast{from{opacity:0;transform:translateY(8px) scale(.98)}to{opacity:1;transform:none}}
    .modal.on .modalbox{animation:v21Modal .28s cubic-bezier(.2,.8,.2,1) both}@keyframes v21Modal{from{opacity:0;transform:translateY(10px) scale(.985)}to{opacity:1;transform:none}}
    .day.today{box-shadow:0 0 0 1px var(--v21-accent),0 0 0 5px rgba(143,29,34,.05),0 10px 24px rgba(143,29,34,.08)}
    .section-glow{position:relative}.section-glow:after{content:"";position:absolute;inset:auto 10% -20px 10%;height:40px;background:rgba(143,29,34,.05);filter:blur(20px);pointer-events:none}
    @media(max-width:760px){.v21-metric-strip,.v21-review-strip{grid-template-columns:1fr}.v21-heat-grid{grid-template-rows:repeat(7,11px);grid-auto-columns:11px}.v21-heat-cell{width:11px;height:11px}}
    @media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}.v21-ripple-wave{display:none}}
  `;

  const safe = v => String(v ?? '').replace(/[&<>\"']/g, m => ({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}[m]));

  function injectStyle() {
    if (document.getElementById(STYLE_ID)) return;
    const style = document.createElement('style');
    style.id = STYLE_ID;
    style.textContent = css;
    document.head.appendChild(style);
  }

  function withButtons() {
    document.querySelectorAll('.btn').forEach(button => {
      if (button.dataset.v21Ripple) return;
      button.dataset.v21Ripple = '1';
      button.classList.add('v21-ripple');
      button.addEventListener('click', e => {
        if (window.matchMedia?.('(prefers-reduced-motion: reduce)').matches) return;
        const rect = button.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const wave = document.createElement('span');
        wave.className = 'v21-ripple-wave';
        wave.style.width = `${size}px`; wave.style.height = `${size}px`;
        wave.style.left = `${e.clientX - rect.left - size / 2}px`;
        wave.style.top = `${e.clientY - rect.top - size / 2}px`;
        button.appendChild(wave);
        setTimeout(() => wave.remove(), 650);
      });
    });
  }

  function readJournal() {
    if (window.tdt?.db?.load) return window.tdt.db.load().catch(() => ({version:2,days:{}}));
    try { return Promise.resolve(JSON.parse(localStorage.getItem('tdt_v2_local_fallback') || '{"days":{}}')); }
    catch (_) { return Promise.resolve({version:2,days:{}}); }
  }

  function tradesOf(day) {
    return ['london','newyork'].flatMap(s => Array.isArray(day?.sessions?.[s]?.trades) ? day.sessions[s].trades : []);
  }

  function disciplineLevel(day) {
    const trades = tradesOf(day);
    if (!trades.length) return 0;
    const average = trades.reduce((sum, trade) => sum + Math.min(10, Array.isArray(trade.checks) ? trade.checks.length : 0), 0) / trades.length;
    return Math.min(4, Math.max(0, Math.round(average / 2.5)));
  }

  function buildHeatmap(journal) {
    const dash = document.getElementById('dash');
    if (!dash) return;
    document.getElementById(HEATMAP_ID)?.remove();
    const days = journal?.days && typeof journal.days === 'object' ? journal.days : {};
    const today = new Date();
    const start = new Date(today);
    start.setDate(today.getDate() - 181);
    const cells = [];
    for (const cursor = new Date(start); cursor <= today; cursor.setDate(cursor.getDate() + 1)) {
      const key = cursor.toISOString().slice(0,10);
      const level = disciplineLevel(days[key]);
      cells.push(`<span class="v21-heat-cell" data-level="${level}" title="${safe(key)} • discipline ${level}/4"></span>`);
    }
    const allDays = Object.keys(days);
    const allTrades = allDays.flatMap(key => tradesOf(days[key]));
    const activeDays = allDays.filter(key => tradesOf(days[key]).length > 0).length;
    const card = document.createElement('section');
    card.id = HEATMAP_ID;
    card.className = 'v21-heat-card fade';
    card.innerHTML = `
      <div class="v21-heat-head">
        <div><div class="v21-kicker">Discipline history</div><strong>Execution heatmap</strong></div>
        <span>Last 6 months</span>
      </div>
      <div class="v21-heat-wrap"><div class="v21-heat-grid">${cells.join('')}</div></div>
      <div class="v21-heat-legend"><span>Less</span><span class="v21-heat-cell"></span><span class="v21-heat-cell" data-level="1"></span><span class="v21-heat-cell" data-level="2"></span><span class="v21-heat-cell" data-level="3"></span><span class="v21-heat-cell" data-level="4"></span><span>More</span></div>
      <div class="v21-metric-strip"><div class="v21-metric"><small>Journal days</small><b>${allDays.length}</b></div><div class="v21-metric"><small>Active days</small><b>${activeDays}</b></div><div class="v21-metric"><small>Total trades</small><b>${allTrades.length}</b></div></div>`;
    dash.appendChild(card);
  }

  function animateScore() {
    const ring = document.querySelector('.score .ring');
    const label = ring?.querySelector('b');
    if (!ring || !label) return;
    const score = Number((label.textContent || '0').replace('%','')) || 0;
    ring.style.setProperty('--v21-score', score);
    if (label.dataset.v21Counted === String(score)) return;
    label.dataset.v21Counted = String(score);
    const reduce = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
    if (reduce) return;
    const start = performance.now(), duration = 700, target = score;
    const tick = now => {
      const p = Math.min(1, (now - start) / duration);
      const eased = 1 - Math.pow(1 - p, 3);
      label.textContent = `${Math.round(target * eased)}%`;
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }

  function addReviewBars(journal) {
    const review = document.getElementById('review');
    if (!review || review.dataset.v21Review === '1') return;
    const days = journal?.days && typeof journal.days === 'object' ? journal.days : {};
    const trades = Object.values(days).flatMap(tradesOf);
    const wins = trades.filter(t => String(t.result).toLowerCase() === 'win').length;
    const losses = trades.filter(t => String(t.result).toLowerCase() === 'loss').length;
    const disciplined = trades.filter(t => (Array.isArray(t.checks) ? t.checks.length : 0) >= 5).length;
    const totalClosed = wins + losses;
    const card = document.createElement('div');
    card.className = 'card v21-review-strip fade';
    card.innerHTML = `<div class="v21-review-card"><small>Win rate</small><b>${totalClosed ? Math.round(wins / totalClosed * 100) : 0}%</b><div class="v21-bar"><span style="width:${totalClosed ? Math.round(wins / totalClosed * 100) : 0}%"></span></div></div><div class="v21-review-card"><small>Checklist discipline</small><b>${trades.length ? Math.round(disciplined / trades.length * 100) : 0}%</b><div class="v21-bar"><span style="width:${trades.length ? Math.round(disciplined / trades.length * 100) : 0}%"></span></div></div><div class="v21-review-card"><small>Average R / trade</small><b>${trades.length ? (trades.reduce((n,t)=>n+(Number(t.r)||0),0)/trades.length).toFixed(2) : '0.00'}</b><div class="v21-bar"><span style="width:${Math.min(100,Math.max(0,50+(trades.length ? trades.reduce((n,t)=>n+(Number(t.r)||0),0)/trades.length*20 : 0)))}%"></span></div></div>`;
    review.appendChild(card);
    review.dataset.v21Review = '1';
  }

  function updateDashboard() {
    animateScore();
    withButtons();
    const promise = readJournal();
    promise.then(journal => buildHeatmap(journal)).catch(() => {});
  }

  function updateReview() {
    const review = document.getElementById('review');
    if (!review) return;
    review.dataset.v21Review = '0';
    readJournal().then(addReviewBars).catch(() => {});
  }

  function patchNavigation() {
    document.querySelectorAll('.nav button').forEach(button => {
      if (button.dataset.v21Nav) return;
      button.dataset.v21Nav = '1';
      button.addEventListener('click', () => {
        requestAnimationFrame(() => {
          const active = document.querySelector('.view.on');
          if (active) { active.classList.remove('v21-view-enter'); void active.offsetWidth; active.classList.add('v21-view-enter'); }
          withButtons();
          updateDashboard();
          updateReview();
        });
      });
    });
  }

  function patchMutation() {
    const nodes = ['dash','month','review','settings'].map(id => document.getElementById(id)).filter(Boolean);
    nodes.forEach(node => {
      const observer = new MutationObserver(() => {
        withButtons();
        patchNavigation();
        if (node.id === 'dash' && node.classList.contains('on')) updateDashboard();
        if (node.id === 'review' && node.classList.contains('on')) updateReview();
      });
      observer.observe(node, {childList:true,subtree:true});
    });
  }

  function boot() {
    injectStyle();
    withButtons();
    patchNavigation();
    patchMutation();
    updateDashboard();
    updateReview();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot, {once:true});
  else boot();
})();
