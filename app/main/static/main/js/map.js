const data = {
    cities: [
        {
            id: 0,
            name: "Mocква",
            x: 55.7,
            y: 37.6,
        },
        {
            id: 1,
            name: "Санкт-Петербург",
            x: 59.57,
            y: 30.19,
        },
        {
            id: 2,
            name: "Екатеринбург",
            x: 56.5,
            y: 60.35,
        }
    ]
}

async function initMap() {
    ymaps.ready( async () => {
        const map_elem = document.getElementsByClassName('map-view')[0];
        const map_wrapper = document.querySelector('.page.map .map-view');

        map_elem.style.width = `${map_wrapper.clientWidth}`;
        map_elem.style.height = `${map_wrapper.clientHeight}`;

        const map = new ymaps.Map(map_elem, {
            center: [58, 37],
            zoom: 3,
            type: 'yandex#map',
            controls: []
        });
        const result = await fetch('/api/cities');

        const data = (await result.json()).data;
        for (const city of data) {
            const myGeoObject = new ymaps.Placemark([city.x, city.y],
                {
                    iconContent: city.name,
                },
                {
                    iconLayout: 'default#imageWithContent',
                    iconImageHref: '/static/main/img/star.png',
                    iconImageSize: [40, 60],
                    iconImageOffset: [-20, -50],
                    iconShape: {
                        type: 'Circle',
                        coordinates: [0, -20],
                        radius: 30
                    },
                    iconContentLayout: ymaps.templateLayoutFactory.createClass(
                        '<h3 style="color: #121212; margin: 0; font-family: \'Cascadia Code SemiBold\', sans-serif;">$[properties.iconContent]</h3>'
                    ),
                    iconContentOffset: [25, -5],
                    balloonCloseButton: false,
                    hideIconOnBalloonOpen: false
            });
            myGeoObject.events.add('click', (event) => {
                window.open(`/${city.id}`, '_current');
            })

            map.geoObjects.add(myGeoObject);
        }
    });
}

initMap().then()
