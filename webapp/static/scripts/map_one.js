ymaps.ready(init);

function init() {
    var el = document.getElementById('map_one');
    var center_lat = el.getAttribute("data-center-lat");
    var center_long = el.getAttribute("data-center-long");
    var lat = el.getAttribute("data-lat");
    var long = el.getAttribute("data-long");
    var current_zoom = el.getAttribute("data-zoom");
    var event_name = el.getAttribute("data-event-name");
    var event_url = el.getAttribute("data-event-url");
    var tags = el.getAttribute("data-tags");
       
    var myMap = new ymaps.Map("map_one", {
            center: [center_lat, center_long],
            zoom: current_zoom
        }, {
            searchControlProvider: 'yandex#search'
        }),
        myGeoObject = new ymaps.GeoObject({
            geometry: {
                type: "Point",
                coordinates: [lat, long]
            },
            properties: {
                balloonContent: '<a href="https://learn.python.ru/">Learn Python</a>',
                hintContent: tags
            }
        }, {
            preset: 'islands#blueEducationCircleIcon',
            draggable: false
        });
        
    myMap.geoObjects.add(myGeoObject);

    // myPlacemark = new ymaps.Placemark([55.704783, 37.778847], {
    //     balloonContent: '<a href="https://learn.python.ru/">Learn Python</a>'
    // }, {
    //     preset: 'islands#blueHomeCircleIcon'
    // });

    // myMap.geoObjects.add(myPlacemark);
}
