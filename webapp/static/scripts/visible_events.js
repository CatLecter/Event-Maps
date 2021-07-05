ymaps.ready(init);

function init () {
    var el = document.getElementById('events_map');
    var current_zoom = el.getAttribute("data-zoom");
    var lat = el.getAttribute("data-lat");
    var long = el.getAttribute("data-long");
    var event = el.getAttribute("data-event");

    var myMap = new ymaps.Map('events_map', {
            center: [lat, long],
            zoom: current_zoom
        }, {
            searchControlProvider: 'yandex#search'
        }),
        objectManager = new ymaps.ObjectManager({
            clusterize: true,
            geoObjectOpenBalloonOnClick: false,
            clusterOpenBalloonOnClick: false,
            gridSize: 32,
        });

    myMap.geoObjects.add(objectManager);


    $.ajax({url: event})
     .done(function(data) {
        objectManager.add(data);
    });

    function hasBalloonData (objectId) {
        return objectManager.objects.getById(objectId).properties.balloonContent;
    }

    objectManager.objects.events.add('click', function (e) {
        var objectId = e.get('objectId'),
            obj = objectManager.objects.getById(objectId);
        if (hasBalloonData(objectId)) {
            objectManager.objects.balloon.open(objectId);
        } else {
            obj.properties.balloonContent = "Идет загрузка данных...";
            objectManager.objects.balloon.open(objectId);
            loadBalloonData(objectId).then(function (data) {
                obj.properties.balloonContent = data;
                objectManager.objects.balloon.setData(obj);
            });
        }
    });
}