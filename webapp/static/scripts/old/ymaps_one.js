ymaps.ready(init);
function init() {
    var myMap = new ymaps.Map("map", {
        center: [55.704783, 37.778847],
        zoom: 13
    }, {
    searchControlProvider: 'yandex#search'
    }),

    // Создаем геообъект с типом геометрии "Точка" с помощью GeoObject.
    myGeoObject = new ymaps.GeoObject({
    // Описание геометрии.
    geometry: {
        type: "Point",
        coordinates: [55.704783, 37.778847]
    },
    // Свойства.
    properties: {
        // Контент метки.
        iconContent: 'Learn Python',
        hintContent: 'Impact Hub'
    }
    }, {
    // Опции.
    // Иконка метки будет растягиваться под размер ее содержимого.
    preset: 'islands#blackStretchyIcon',
    // Метку можно перемещать.
    draggable: false
    });
    
    myMap.geoObjects.add(myGeoObject);
}