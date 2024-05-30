self.addEventListener('install', event => {
  event.waitUntil(
    caches.open('streamlit-pwa').then(cache => {
      return cache.addAll([
        '/',
        '/manifest.json',
        // add other assets that need to be cached
      ]);
    })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});
