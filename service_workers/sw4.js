self.addEventListener('push', function(event) {
    console.log("Mensajito");
    const titulo = "Mensaje desde otro lugar";
    let optiones = {
        body: event.data.text()
    };
    event.waitUntil(self.registration.showNotification(titulo, opciones));
});