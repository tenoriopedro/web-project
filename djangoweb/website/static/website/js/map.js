document.addEventListener("DOMContentLoaded", function () {
    const bonsucesso = { lat: -22.86834, lng: -43.26624};
    const saocristovao = { lat: -22.89513, lng: -43.22038};

    const map = L.map("custom-map").setView(bonsucesso, 13);

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: "© OpenStreetMap contributors",
    }).addTo(map);

    const locals = [
        {
            name: "Unidade Bonsucesso",
            coords: bonsucesso,
            link: "https://maps.app.goo.gl/aXQV6qkZCixXbbWj9?g_st=aw",
        },
        {
            name: "Unidade São Cristóvão",
            coords: saocristovao,
            link: "https://maps.app.goo.gl/k9fJibWfiq9GNMH58"
        },
    ];

    locals.forEach(local => {
        const popup = `
      <strong>${local.name}</strong><br/>
      <a href="${local.link}" target="_blank">Ver no Google Maps</a>
    `;
    L.marker([local.coords.lat, local.coords.lng])
      .addTo(map)
      .bindPopup(popup);
    });
});

