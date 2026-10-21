/* రాయ్ విద్యార్థి యాప్ – Service Worker (ఆఫ్లైన్ పనిచేయడానికి) */
const VER = 'rai-vidyarthi-v3';
const SHELL = ['./', './index.html', './manifest.webmanifest', './icon-96.png', './icon-192.png', './icon-512.png', './icon-maskable-512.png', './apple-touch-icon.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(VER).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VER).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  // సింక్, Analytics – ఎప్పుడూ నెట్‌వర్క్ నుండే
  if (url.pathname.endsWith('/config.json')) return;
  if (/script\.google(usercontent)?\.com|firestore\.googleapis|identitytoolkit|securetoken|google-analytics|googletagmanager/.test(url.host)) return;
  // యాప్ పేజీ: ముందు నెట్‌వర్క్ (కొత్త వెర్షన్ కోసం), లేకపోతే కాష్
  if (req.mode === 'navigate' || (url.origin === location.origin && /\/(index\.html)?$/.test(url.pathname))) {
    e.respondWith(fetch(req).then(r => { const cp = r.clone(); caches.open(VER).then(c => c.put('./index.html', cp)); return r; })
      .catch(() => caches.match('./index.html')));
    return;
  }
  // ఐకాన్లు, ఫాంట్లు, Firebase లైబ్రరీ: ముందు కాష్
  if (url.origin === location.origin || /fonts\.(googleapis|gstatic)\.com|www\.gstatic\.com/.test(url.host)) {
    e.respondWith(caches.match(req).then(hit => hit || fetch(req).then(r => {
      if (r.ok || r.type === 'opaque') { const cp = r.clone(); caches.open(VER).then(c => c.put(req, cp)); }
      return r;
    })));
  }
});
// నోటిఫికేషన్ నొక్కితే యాప్ తెరుచుకోవాలి
self.addEventListener('notificationclick', e => {
  e.notification.close();
  e.waitUntil(self.clients.matchAll({type: 'window', includeUncontrolled: true}).then(cs => {
    for (const c of cs) { if ('focus' in c) return c.focus(); }
    return self.clients.openWindow('./');
  }));
});
