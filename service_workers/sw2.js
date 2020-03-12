self.addEventListener("fetch", e => {
  e.respondWith(
    fetch(e.request)
      .then(respuesta => {
        console.log("Todo bien" + e.request.url);
        //return fetch("libros.jpg");
        if (e.request.url.includes("rita-segato")) {
          return fetch("libros.gif");
        }
        return respuesta;
      })
      .catch(e => {
        return caches.match("brb.html");
      })
  );
});

self.addEventListener("install", e => {
  e.waitUntil(
    caches.open("mitilichero").then(cache => {
      return cache.add("brb.html");
    })
  );
});
