var map = L.map('divMap').setView([-18.9188, -48.2762], 10);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var poligonoCoordenadas = [];
var selecionaCoordenadas = [];
var distanciaCoordenadas = L.marker();

fetch('/static/Posicoes.json')
    .then(response => response.json())
    .then(jsonData => {
        jsonData.data.forEach(point => {

            var latlng = [parseFloat(point.latitude), parseFloat(point.longitude)];


            L.marker(latlng).addTo(map).bindPopup( point.date_time);

            poligonoCoordenadas.push(latlng);
        });

        L.polygon(poligonoCoordenadas, {color:'blue'}).addTo(map);
    })
    .catch(error => console.error('Erro ao carregar o arquivo JSON:', error));


