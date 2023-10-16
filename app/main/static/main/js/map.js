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
            center: [55.7, 47.6],
            zoom: 5,
            type: 'yandex#map',
            controls: []
        });
        const result = await fetch('/api/cities');

        const data = (await result.json()).data;
        for (const city of data) {
            const myGeoObject = new ymaps.Placemark([city.x, city.y],
                {
                    iconCaption: city.name,
                },
                {
                    balloonCloseButton: false,
                    hideIconOnBalloonOpen: false
                }
            );
            myGeoObject.events.add('click', (event) => {
                window.open(`/${city.id}`, '_current');
            })

            map.geoObjects.add(myGeoObject);
        }
    });
}

initMap().then()