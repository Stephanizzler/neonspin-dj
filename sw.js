/* SoundLab DJ offline support: the app shell is cached so the installed app opens without a connection.
   The page itself is fetched network-first, so new versions arrive as soon as you're online. */
const CACHE='soundlab-v22';
const CORE=['./','./index.html','./manifest.webmanifest','./icons/jog-icon-192.png','./icons/jog-icon-512.png','./icons/jog-apple-touch-icon.png','./icons/jog-favicon.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{
  const r=e.request;if(r.method!=='GET')return;const u=new URL(r.url);
  const save=res=>{if(res&&res.ok){const cp=res.clone();caches.open(CACHE).then(c=>c.put(r,cp))}return res};
  if(u.origin===location.origin){e.respondWith(fetch(r,{cache:'no-cache'}).then(save).catch(()=>caches.match(r).then(m=>m||caches.match('./index.html'))));return}
  if(/(^|\.)fonts\.(googleapis|gstatic)\.com$/.test(u.hostname))e.respondWith(caches.match(r).then(m=>m||fetch(r).then(save)));
});
