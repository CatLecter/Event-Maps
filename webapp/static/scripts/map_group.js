ymaps.ready(init);

function init() {
    var el = document.getElementById('map_group');
    var center_lat = el.getAttribute("data-center-lat");
    var center_long = el.getAttribute("data-center-long");
    var lat = el.getAttribute("data-lat");
    var long = el.getAttribute("data-long");
    var current_zoom = el.getAttribute("data-zoom");

    var myMap = new ymaps.Map('map_group', {
            center: [center_lat, center_long],
            zoom: current_zoom
        }, {
            searchControlProvider: 'yandex#search'
        }), menu = $('<ul class="menu"></ul>');
    
    for (var i = 0, l = groups.length; i < l; i++) {
        createMenuGroup(groups[i]);
    }

    function createMenuGroup(group) {
        // Пункт меню.
        var menuItem = $('<li><a href="#">' + group.name + '</a></li>'),
            // Коллекция для геообъектов группы.
            collection = new ymaps.GeoObjectCollection(null, {
                preset: group.style
            }),
            // Контейнер для подменю.
            submenu = $('<ul class="submenu"></ul>');
        // Добавляем коллекцию на карту.
        myMap.geoObjects.add(collection);
        // Добавляем подменю.
        menuItem.append(submenu)
            // Добавляем пункт в меню.
            .appendTo(menu)
            // По клику удаляем/добавляем коллекцию на карту и скрываем/отображаем подменю.
            .find('a').bind('click', function() {
                if (collection.getParent()) {
                    myMap.geoObjects.remove(collection);
                    submenu.hide();
                } else {
                    myMap.geoObjects.add(collection);
                    submenu.show();
                }
            });
        for (var j = 0, m = group.items.length; j < m; j++) {
            createSubMenu(group.items[j], collection, submenu);
        }
    }

    function createSubMenu(item, collection, submenu) {
        // Пункт подменю.
        var submenuItem = $('<li><a href="#">' + item.name + '</a></li>'),
            // Создаем метку.
            placemark = new ymaps.Placemark(item.center, {
                balloonContent: item.name
            });
        // Добавляем метку в коллекцию.
        collection.add(placemark);
        // Добавляем пункт в подменю.
        submenuItem.appendTo(submenu)
            // При клике по пункту подменю открываем/закрываем баллун у метки.
            .find('a').bind('click', function() {
                if (!placemark.balloon.isOpen()) {
                    placemark.balloon.open();
                } else {
                    placemark.balloon.close();
                }
                return false;
            });
    }
    // Добавляем меню в тэг BODY.
    menu.appendTo($('body'));
    // Выставляем масштаб карты чтобы были видны все группы.
    myMap.setBounds(myMap.geoObjects.getBounds());
}