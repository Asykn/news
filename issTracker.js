//Latitude & Longitude
const iss_api = 'https://api.wheretheiss.at/v1/satellites/25544'
    async function getISS() {
        const response = await fetch(iss_api);
        const data = await response.json();
        const { latitude, longitude } = data;

        marker.setLatLng( [ latitude, longitude ]);
        map.setView([ latitude, longitude ], 2);

        document.getElementById('lat').textContent = latitude.toFixed(3);
        document.getElementById('lon').textContent = longitude.toFixed(3);
    }

    getISS();

setInterval(getISS, 600);

//Sizing map
const map = L.map('ISSMap').setView([0, 0], 2);
const marker = L.marker( [0, 0]).addTo(map);

const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';
const tileURL = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
const tiles = L.tileLayer(tileURL,{ attribution });
tiles.addTo(map);