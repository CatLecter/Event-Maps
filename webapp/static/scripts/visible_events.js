ymaps.ready(init);

function init () {
    var myMap = new ymaps.Map('events_map', {
            center: [55.76, 37.64],
            zoom: 10
        }, {
            searchControlProvider: 'yandex#search'
        }),
        objectManager = new ymaps.ObjectManager({
            // Мы хотим загружать данные для балуна перед открытием, поэтому
            // запретим автоматически открывать балун по клику.
            // Чтобы метки начали кластеризоваться, выставляем опцию.
            clusterize: true,
            geoObjectOpenBalloonOnClick: false,
            clusterOpenBalloonOnClick: false,
            gridSize: 32,
        });

    myMap.geoObjects.add(objectManager);
    

    // Добавление коллекций объектов.
    /*
    var collection = {
        type: 'FeatureCollection',
        features: [{
            type: 'Feature',
            id: currentId++,
            geometry: {
                type: 'Point',
                coordinates: [24.34, 65.24]
            }
        }, {
            type: 'Feature',
            id: currentId++,
            geometry: {
                type: 'Point',
                coordinates: [25.34, 63.24]
            }
        }
    ]}
    objectManager.add(collection);
    map.geoObjects.add(objectManager);
    */

    $.ajax({
        url: "static/scripts/data.json"
    }).done(function(data) {
            objectManager.add(data);
        });

    // Функция, эмулирующая запрос за данными на сервер.
    function loadBalloonData (objectId) {
        var dataDeferred = ymaps.vow.defer();
        function resolveData () {
            dataDeferred.resolve('Данные балуна');
        }
        window.setTimeout(resolveData, 1000);
        return dataDeferred.promise();
    }

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

    var placemark = new ymaps.Placemark(myMap.getCenter(), {
        // Зададим содержимое заголовка балуна.
        balloonContentHeader: '<a href = "#">Рога и копыта</a><br>' +
            '<span class="description">Сеть кинотеатров</span>',
        // Зададим содержимое основной части балуна.
        balloonContentBody: '<img src="img/cinema.jpg" height="150" width="200"> <br/> ' +
            '<a href="tel:+7-123-456-78-90">+7 (123) 456-78-90</a><br/>' +
            '<b>Ближайшие сеансы</b> <br/> Сеансов нет.',
        // Зададим содержимое нижней части балуна.
        balloonContentFooter: 'Информация предоставлена:<br/>OOO "Рога и копыта"',
        // Зададим содержимое всплывающей подсказки.
        hintContent: 'Рога и копыта'
    });
    // Добавим метку на карту.
    myMap.geoObjects.add(placemark);
    // Откроем балун на метке.
    placemark.balloon.open();
}
