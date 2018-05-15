var crimeSelected = $('input[name=crime]:checked').val();

var arrayOfSelected =[crimeSelected];


$("#crimeFilter").on('change', function(event) {
    crimeSelected = $('input[name=crime]:checked').val();
    arrayOfSelected.push(crimeSelected);
    console.log(arrayOfSelected);
    var lastItem = arrayOfSelected[arrayOfSelected.length - 2];
    console.log("Removing "+lastItem);

    map.removeLayer(lastItem);

    map.addLayer({
        'id': crimeSelected,
        'type': 'circle',
        'source': {
            type: 'vector',
            url: 'mapbox://' + layerObj[crimeSelected]["id"]
        },
        'source-layer': layerObj[crimeSelected]["detail"],
        'paint': {
            // make circles larger as the user zooms from z12 to z22
            'circle-radius': {
                'base': 1.75,
                'stops': [
                    [12, 2],
                    [22, 180]
                ]
            },
            'circle-color': '#6ba3ff'
        }
    });



});

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
	console.log('Map Display '+crimeSelected);

	map.addLayer({
        'id': crimeSelected,
        'type': 'circle',
        'source': {
            type: 'vector',
            url: 'mapbox://' + layerObj[crimeSelected]["id"]
        },
        'source-layer': layerObj[crimeSelected]["detail"],
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



});