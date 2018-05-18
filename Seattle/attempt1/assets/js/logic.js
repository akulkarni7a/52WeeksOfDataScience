var crimeSelected = $('input[name=crime]:checked').val();

mapboxgl.accessToken = 'pk.eyJ1IjoiYXNrYWtkYWdyOCIsImEiOiJjamgzbW04MmowNTJlMndueG1tNGU4OGQ1In0.7G4btoI3KCFFq6gPr6MdeA';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/light-v9',
    zoom: 12,
    center: [-122.343161, 47.611673]
});

var layerObj = {
    "carprowl": {
        "id": "askakdagr8.1zgedqin",
        "detail": "carprowl-9q8uqm"
    },
    "robbery": {
        "id": "askakdagr8.527q90rp",
        "detail": "dfrob-5m6vcm"
    }
}


map.on('load', function() {
    console.log('Map Display ' + crimeSelected);

    map.addLayer({
        'id': '3d-buildings',
        'source': 'composite',
        'source-layer': 'building',
        'filter': ['==', 'extrude', 'true'],
        'type': 'fill-extrusion',
        'minzoom': 15,
        'paint': {
            "fill-extrusion-opacity": 0.8,
            'fill-extrusion-color': '#aaa',
            "fill-extrusion-height": 500,
            "fill-extrusion-height-transition": {
                duration: 500,
                delay: 0
            },
        }
    });

    map.addLayer({
        'id': 'shoplifting',
        'type': 'circle',
        'source': {
            type: 'vector',
            url: 'mapbox://askakdagr8.4hwzprpq'
        },
        'source-layer': 'dfshop-7eo2uj',
        'paint': {
            // make circles larger as the user zooms from z12 to z22
            'circle-radius': {
                'base': 1.75,
                'stops': [
                    [12, 2],
                    [22, 180]
                ]
            },
            'circle-color': '#ff7770'
        }
    });

    map.addLayer({
        'id': 'robbery',
        'type': 'circle',
        'source': {
            type: 'vector',
            url: 'mapbox://askakdagr8.527q90rp'
        },
        'source-layer': 'dfrob-5m6vcm',
        'paint': {
            // make circles larger as the user zooms from z12 to z22
            'circle-radius': {
                'base': 1.75,
                'stops': [
                    [12, 2],
                    [22, 180]
                ]
            },
            'circle-color': '#629dfc'
        }
    });

    map.addLayer({
        'id': 'prostitution',
        'type': 'circle',
        'source': {
            type: 'vector',
            url: 'mapbox://askakdagr8.c3exxor3'
        },
        'source-layer': 'dfpros-1g5sm4',
        'paint': {
            // make circles larger as the user zooms from z12 to z22
            'circle-radius': {
                'base': 1.75,
                'stops': [
                    [12, 2],
                    [22, 180]
                ]
            },
            'circle-color': '#a761fc'
        }
    });

    map.addLayer({
        'id': 'narcotics',
        'type': 'circle',
        'source': {
            type: 'vector',
            url: 'mapbox://askakdagr8.2es81wfn'
        },
        'source-layer': 'dfnar-cz7c77',
        'paint': {
            // make circles larger as the user zooms from z12 to z22
            'circle-radius': {
                'base': 1.75,
                'stops': [
                    [12, 2],
                    [22, 180]
                ]
            },
            'circle-color': '#f1ff5e'
        }
    });

    map.addLayer({
        'id': 'burglary',
        'type': 'circle',
        'source': {
            type: 'vector',
            url: 'mapbox://askakdagr8.6sq5673u'
        },
        'source-layer': 'dfburg-2mp4oe',
        'paint': {
            // make circles larger as the user zooms from z12 to z22
            'circle-radius': {
                'base': 1.75,
                'stops': [
                    [12, 2],
                    [22, 180]
                ]
            },
            'circle-color': '#ff93e7'
        }
    });

    map.addLayer({
        'id': 'autotheft',
        'type': 'circle',
        'source': {
            type: 'vector',
            url: 'mapbox://askakdagr8.8txxjotz'
        },
        'source-layer': 'dfauto-75ozrd',
        'paint': {
            // make circles larger as the user zooms from z12 to z22
            'circle-radius': {
                'base': 1.75,
                'stops': [
                    [12, 2],
                    [22, 180]
                ]
            },
            'circle-color': '#ff0f0f'
        }
    });

    map.addLayer({
        'id': 'homicide',
        'type': 'circle',
        'source': {
            type: 'vector',
            url: 'mapbox://askakdagr8.6ez8zen8'
        },
        'source-layer': 'dfhom-4acjnw',
        'paint': {
            // make circles larger as the user zooms from z12 to z22
            'circle-radius': {
                'base': 1.75,
                'stops': [
                    [12, 2],
                    [22, 180]
                ]
            },
            'circle-color': '#7c7c7c'
        }
    });

    map.addLayer({
        'id': 'assault',
        'type': 'circle',
        'source': {
            type: 'vector',
            url: 'mapbox://askakdagr8.doaizs7e'
        },
        'source-layer': 'dfass-al518o',
        'paint': {
            // make circles larger as the user zooms from z12 to z22
            'circle-radius': {
                'base': 1.75,
                'stops': [
                    [12, 2],
                    [22, 180]
                ]
            },
            'circle-color': '#3de800'
        }
    });

    map.addLayer({
        'id': 'arrest',
        'type': 'circle',
        'source': {
            type: 'vector',
            url: 'mapbox://askakdagr8.1xjowwjl'
        },
        'source-layer': 'dfarrest-74359f',
        'paint': {
            // make circles larger as the user zooms from z12 to z22
            'circle-radius': {
                'base': 1.75,
                'stops': [
                    [12, 2],
                    [22, 180]
                ]
            },
            'circle-color': '#eaa22e'
        }
    });

    map.addLayer({
        'id': 'carprowl',
        'type': 'circle',
        'source': {
            type: 'vector',
            url: 'mapbox://askakdagr8.1zgedqin'
        },
        'source-layer': 'carprowl-9q8uqm',
        'paint': {
            // make circles larger as the user zooms from z12 to z22
            'circle-radius': {
                'base': 1.75,
                'stops': [
                    [12, 2],
                    [22, 180]
                ]
            },
            'circle-color': '#28ffc5'
        }
    });

    map.setLayoutProperty("shoplifting", "visibility", "visible");
    map.setLayoutProperty("robbery", "visibility", "none");
    map.setLayoutProperty("prostitution", "visibility", "none");
    map.setLayoutProperty("narcotics", "visibility", "none");
    map.setLayoutProperty("burglary", "visibility", "none");
    map.setLayoutProperty("autotheft", "visibility", "none");
    map.setLayoutProperty("homicide", "visibility", "none");
    map.setLayoutProperty("assault", "visibility", "none");
    map.setLayoutProperty("arrest", "visibility", "none");
    map.setLayoutProperty("carprowl", "visibility", "none");

    $("#crimeFilter").on('change', function(event) {
        crimeSelected = $('input[name=crime]:checked').val();
        console.log(crimeSelected);
        if (crimeSelected == "shoplifting") {
            map.setLayoutProperty("shoplifting", "visibility", "visible");
            map.setLayoutProperty("robbery", "visibility", "none");
            map.setLayoutProperty("prostitution", "visibility", "none");
            map.setLayoutProperty("narcotics", "visibility", "none");
            map.setLayoutProperty("burglary", "visibility", "none");
            map.setLayoutProperty("autotheft", "visibility", "none");
            map.setLayoutProperty("homicide", "visibility", "none");
            map.setLayoutProperty("assault", "visibility", "none");
            map.setLayoutProperty("arrest", "visibility", "none");
            map.setLayoutProperty("carprowl", "visibility", "none");
        }
        if (crimeSelected == "robbery") {
            map.setLayoutProperty("shoplifting", "visibility", "none");
            map.setLayoutProperty("robbery", "visibility", "visible");
            map.setLayoutProperty("prostitution", "visibility", "none");
            map.setLayoutProperty("narcotics", "visibility", "none");
            map.setLayoutProperty("burglary", "visibility", "none");
            map.setLayoutProperty("autotheft", "visibility", "none");
            map.setLayoutProperty("homicide", "visibility", "none");
            map.setLayoutProperty("assault", "visibility", "none");
            map.setLayoutProperty("arrest", "visibility", "none");
            map.setLayoutProperty("carprowl", "visibility", "none");
        }
        if (crimeSelected == "prostitution") {
            map.setLayoutProperty("shoplifting", "visibility", "none");
            map.setLayoutProperty("robbery", "visibility", "none");
            map.setLayoutProperty("prostitution", "visibility", "visible");
            map.setLayoutProperty("narcotics", "visibility", "none");
            map.setLayoutProperty("burglary", "visibility", "none");
            map.setLayoutProperty("autotheft", "visibility", "none");
            map.setLayoutProperty("homicide", "visibility", "none");
            map.setLayoutProperty("assault", "visibility", "none");
            map.setLayoutProperty("arrest", "visibility", "none");
            map.setLayoutProperty("carprowl", "visibility", "none");
        }
        if (crimeSelected == "narcotics") {
            map.setLayoutProperty("shoplifting", "visibility", "none");
            map.setLayoutProperty("robbery", "visibility", "none");
            map.setLayoutProperty("prostitution", "visibility", "none");
            map.setLayoutProperty("narcotics", "visibility", "visible");
            map.setLayoutProperty("burglary", "visibility", "none");
            map.setLayoutProperty("autotheft", "visibility", "none");
            map.setLayoutProperty("homicide", "visibility", "none");
            map.setLayoutProperty("assault", "visibility", "none");
            map.setLayoutProperty("arrest", "visibility", "none");
            map.setLayoutProperty("carprowl", "visibility", "none");
        }
        if (crimeSelected == "burglary") {
            map.setLayoutProperty("shoplifting", "visibility", "none");
            map.setLayoutProperty("robbery", "visibility", "none");
            map.setLayoutProperty("prostitution", "visibility", "none");
            map.setLayoutProperty("narcotics", "visibility", "none");
            map.setLayoutProperty("burglary", "visibility", "visible");
            map.setLayoutProperty("autotheft", "visibility", "none");
            map.setLayoutProperty("homicide", "visibility", "none");
            map.setLayoutProperty("assault", "visibility", "none");
            map.setLayoutProperty("arrest", "visibility", "none");
            map.setLayoutProperty("carprowl", "visibility", "none");
        }
        if (crimeSelected == "autotheft") {
            map.setLayoutProperty("shoplifting", "visibility", "none");
            map.setLayoutProperty("robbery", "visibility", "none");
            map.setLayoutProperty("prostitution", "visibility", "none");
            map.setLayoutProperty("narcotics", "visibility", "none");
            map.setLayoutProperty("burglary", "visibility", "none");
            map.setLayoutProperty("autotheft", "visibility", "visible");
            map.setLayoutProperty("homicide", "visibility", "none");
            map.setLayoutProperty("assault", "visibility", "none");
            map.setLayoutProperty("arrest", "visibility", "none");
            map.setLayoutProperty("carprowl", "visibility", "none");
        }
        if (crimeSelected == "homicide") {
            map.setLayoutProperty("shoplifting", "visibility", "none");
            map.setLayoutProperty("robbery", "visibility", "none");
            map.setLayoutProperty("prostitution", "visibility", "none");
            map.setLayoutProperty("narcotics", "visibility", "none");
            map.setLayoutProperty("burglary", "visibility", "none");
            map.setLayoutProperty("autotheft", "visibility", "none");
            map.setLayoutProperty("homicide", "visibility", "visible");
            map.setLayoutProperty("assault", "visibility", "none");
            map.setLayoutProperty("arrest", "visibility", "none");
            map.setLayoutProperty("carprowl", "visibility", "none");
        }
        if (crimeSelected == "assault") {
            map.setLayoutProperty("shoplifting", "visibility", "none");
            map.setLayoutProperty("robbery", "visibility", "none");
            map.setLayoutProperty("prostitution", "visibility", "none");
            map.setLayoutProperty("narcotics", "visibility", "none");
            map.setLayoutProperty("burglary", "visibility", "none");
            map.setLayoutProperty("autotheft", "visibility", "none");
            map.setLayoutProperty("homicide", "visibility", "none");
            map.setLayoutProperty("assault", "visibility", "visible");
            map.setLayoutProperty("arrest", "visibility", "none");
            map.setLayoutProperty("carprowl", "visibility", "none");
        }
        if (crimeSelected == "arrest") {
            map.setLayoutProperty("shoplifting", "visibility", "none");
            map.setLayoutProperty("robbery", "visibility", "none");
            map.setLayoutProperty("prostitution", "visibility", "none");
            map.setLayoutProperty("narcotics", "visibility", "none");
            map.setLayoutProperty("burglary", "visibility", "none");
            map.setLayoutProperty("autotheft", "visibility", "none");
            map.setLayoutProperty("homicide", "visibility", "none");
            map.setLayoutProperty("assault", "visibility", "none");
            map.setLayoutProperty("arrest", "visibility", "visible");
            map.setLayoutProperty("carprowl", "visibility", "none");
        }
        if (crimeSelected == "carprowl") {
            map.setLayoutProperty("shoplifting", "visibility", "none");
            map.setLayoutProperty("robbery", "visibility", "none");
            map.setLayoutProperty("prostitution", "visibility", "none");
            map.setLayoutProperty("narcotics", "visibility", "none");
            map.setLayoutProperty("burglary", "visibility", "none");
            map.setLayoutProperty("autotheft", "visibility", "none");
            map.setLayoutProperty("homicide", "visibility", "none");
            map.setLayoutProperty("assault", "visibility", "none");
            map.setLayoutProperty("arrest", "visibility", "none");
            map.setLayoutProperty("carprowl", "visibility", "visible");
        }
        if (crimeSelected == "all") {
            map.setLayoutProperty("shoplifting", "visibility", "visible");
            map.setLayoutProperty("robbery", "visibility", "visible");
            map.setLayoutProperty("prostitution", "visibility", "visible");
            map.setLayoutProperty("narcotics", "visibility", "visible");
            map.setLayoutProperty("burglary", "visibility", "visible");
            map.setLayoutProperty("autotheft", "visibility", "visible");
            map.setLayoutProperty("homicide", "visibility", "visible");
            map.setLayoutProperty("assault", "visibility", "visible");
            map.setLayoutProperty("arrest", "visibility", "visible");
            map.setLayoutProperty("carprowl", "visibility", "visible");
        }

    });




});