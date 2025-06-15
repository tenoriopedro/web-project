function initMap() {
    const bonsucesso = { lat: -22.86834, lng: -43.26624};
    const saocristovao = { lat: -22.89513, lng: -43.22038};

    const map = new google.maps.Map(document.getElementById("custom-map"), {
        zoom: 13,
        center: bonsucesso,
        mapTypeControl: false,
        fullscreenControl: false,
        streetViewControl: false,
        gestureHandling: "greedy",
    });

    new google.maps.Marker({
        position: bonsucesso,
        map,
        title: "Unidade Bonsucesso",
    });

    new google.maps.Marker({
        position: saocristovao,
        map,
        title: "Unidade São Cristóvão",
    });
}