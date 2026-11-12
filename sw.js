/* రాయ్ విద్యార్థి యాప్ – Service Worker (ఆఫ్లైన్ పనిచేయడానికి) */
const VER = 'rai-vidyarthi-v11';
// 'raay-offline' = యాప్‌లోని “📥 ఆఫ్‌లైన్ డౌన్‌లోడ్” సేవ్ చేసిన ఫైళ్లు – అప్‌డేట్‌లో తొలగించం
const SHELL = ['./', './index.html', './manifest.webmanifest', './icon-96.png', './icon-192.png', './icon-512.png', './icon-maskable-512.png', './apple-touch-icon.png'];
const BASE = new URL('./', self.location).pathname;

self.addEventListener('install', e => {
  e.waitUntil(caches.open(VER).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VER && k !== 'raay-offline').map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
function keep(req, r) {
  if (r && r.status === 200) { const cp = r.clone(); caches.open(VER).then(c => c.put(req, cp)).catch(() => {}); }
  return r;
}
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  // సింక్, GitHub లిస్ట్, config – ఎప్పుడూ నెట్‌వర్క్ నుండే
  if (url.pathname.endsWith('/config.json') || /script\.google(usercontent)?\.com|api\.github\.com|firestore\.googleapis|identitytoolkit|securetoken|drive\.google\.com|docs\.google\.com/.test(url.host)) return;
  const same = url.origin === location.origin;
  // యాప్ పేజీ: సేవ్ అయిన కాపీ వెంటనే (వేగంగా తెరుచుకోవడానికి) + వెనుక కొత్త వెర్షన్ తెచ్చి, మారితే యాప్‌కు 'newver' చెబుతాం
  if (same && (url.pathname === BASE || url.pathname === BASE + 'index.html')) {
    const tag = r => r ? (r.headers.get('etag') || r.headers.get('last-modified') || r.headers.get('content-length') || '') : '';
    const hit = caches.match('./index.html');
    const net = fetch(req).then(async r => {
      if (r.status !== 200) return r;
      const old = await hit, cp = r.clone(), c = await caches.open(VER);
      await c.put('./index.html', cp);
      if (old && tag(old) !== tag(r)) (await self.clients.matchAll({type: 'window', includeUncontrolled: true})).forEach(w => w.postMessage({t: 'newver'}));
      return r;
    });
    e.waitUntil(net.catch(() => {}));
    e.respondWith(hit.then(h => h || net).catch(() => net));
    return;
  }
  // పాఠం నోట్స్ (notes-3.js …): ముందు నెట్‌వర్క్ (కొత్త నోట్స్ వెంటనే), లేకపోతే కాష్ (ఆఫ్లైన్)
  if (/\.mp4$/i.test(url.pathname)) return;  // వీడియో: నేరుగా నెట్‌వర్క్ (కాష్ చేయం)
  if (same && (/\/(notes|answers|ssc)-\d+(-[a-z0-9]+)?\.js$/.test(url.pathname) || /\/help\.js$/.test(url.pathname))) {
    e.respondWith(fetch(req, {cache: 'no-cache'}).then(r => keep(req, r)).catch(() => caches.match(req, {ignoreSearch: true})));
    return;
  }
  // HTML టూల్స్: ముందు నెట్‌వర్క్ (కొత్త వెర్షన్), లేకపోతే కాష్
  if (same && (req.mode === 'navigate' || /\.html?$/i.test(url.pathname))) {
    e.respondWith(fetch(req).then(r => keep(req, r)).catch(() => caches.match(req)));
    return;
  }
  // పుస్తకాలు (PDF), ఐకాన్లు, ఫాంట్లు, pdf.js: ముందు కాష్ (ఒకసారి తెరిస్తే ఆఫ్లైన్‌లో)
  if (same || /fonts\.(googleapis|gstatic)\.com|www\.gstatic\.com|cdnjs\.cloudflare\.com|cdn\.jsdelivr\.net/.test(url.host)) {
    e.respondWith(caches.match(req).then(hit => hit || fetch(req).then(r => (r.status === 200 || r.type === 'opaque') ? keep(req, r) : r)));
  }
});
self.addEventListener('notificationclick', e => {
  e.notification.close();
  e.waitUntil(self.clients.matchAll({type: 'window', includeUncontrolled: true}).then(cs => {
    for (const c of cs) { if ('focus' in c) return c.focus(); }
    return self.clients.openWindow('./');
  }));
});
