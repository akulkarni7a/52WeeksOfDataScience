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
        'id': 'all',
        'type': 'circle',
        'source': {
            type: 'vector',
            url: 'mapbox://askakdagr8.9eh927tk'
        },
        'source-layer': 'output-3xxq3l',
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

    map.setFilter('all', ['==', 'Event Clearance Group', 'SHOPLIFTING'])
    map.setPaintProperty('all', 'circle-color', '#faafee');

    $("#crimeFilter").on('change', function(event) {
        crimeSelected = $('input[name=crime]:checked').val();
        console.log(crimeSelected);
        if (crimeSelected == "shoplifting") {
            map.setFilter('all', ['==', 'Event Clearance Group', 'SHOPLIFTING']);
            map.setPaintProperty('all', 'circle-color', '#faafee');
        }
        if (crimeSelected == "robbery") {
            map.setFilter('all', ['==', 'Event Clearance Group', 'ROBBERY']);
            map.setPaintProperty("all", "circle-color", "#f48341");
        }
        if (crimeSelected == "prostitution") {
            map.setFilter('all', ['==', 'Event Clearance Group', 'PROSTITUTION'])
            map.setPaintProperty("all", "circle-color", "#f4c141");
        }
        if (crimeSelected == "narcotics") {
            map.setFilter('all', ['==', 'Event Clearance Group', 'NARCOTICS COMPLAINTS'])
            map.setPaintProperty("all", "circle-color", "#e5f441");
        }
        if (crimeSelected == "burglary") {
            map.setFilter('all', ['==', 'Event Clearance Group', 'BURGLARY'])
            map.setPaintProperty("all", "circle-color", "#82f441");
        }
        if (crimeSelected == "autotheft") {
            map.setFilter('all', ['==', 'Event Clearance Group', 'AUTO THEFTS'])
            map.setPaintProperty("all", "circle-color", "#41f48b");
        }
        if (crimeSelected == "homicide") {
            map.setFilter('all', ['==', 'Event Clearance Group', 'HOMICIDE'])
            map.setPaintProperty("all", "circle-color", "#41f4d9");
        }
        if (crimeSelected == "assault") {
            map.setFilter('all', ['==', 'Event Clearance Group', 'ASSAULTS'])
            map.setPaintProperty("all", "circle-color", "#42b6ff");
        }
        if (crimeSelected == "arrest") {
            map.setFilter('all', ['==', 'Event Clearance Group', 'ARREST'])
            map.setPaintProperty("all", "circle-color", "#4151ff");
        }
        if (crimeSelected == "carprowl") {
            map.setFilter('all', ['==', 'Event Clearance Group', 'CAR PROWL'])
            map.setPaintProperty("all", "circle-color", "#a43dff");
        }

    });


    $("#year").on('change', function(event) {
        var year = $('#year').val();
        console.log(year);

        if (year == "2009") {
            var previousFilter = map.getFilter('all');
            var columns = previousFilter[1];
            var critera = previousFilter[2];
            map.setFilter('all', ['==', 'Year', 2009]&&['==', columns, critera])
            // map.setFilter('all',previousFilter)
            $("#yearAppend").text("2009")
        }
        if (year == "2010") {
            var previousFilter = map.getFilter('all');
            var columns = previousFilter[1];
            var critera = previousFilter[2];
            map.setFilter('all', ['==', 'Year', 2010]&&['==', columns, critera])
            // map.setFilter('all',previousFilter)
            $("#yearAppend").text("2010")
        }
        if (year == "2011") {
            var previousFilter = map.getFilter('all');
            var columns = previousFilter[1];
            var critera = previousFilter[2];
            map.setFilter('all', ['==', 'Year', 2011]&&['==', columns, critera])

            // map.setFilter('all',previousFilter)
            $("#yearAppend").text("2011")
        }

        if (year == "2012") {
            var previousFilter = map.getFilter('all');
            var columns = previousFilter[1];
            var critera = previousFilter[2];
            map.setFilter('all', ['==', 'Year', 2012]&&['==', columns, critera])
            // map.setFilter('all',previousFilter)
            $("#yearAppend").text("2012")
        }
        if (year == "2013") {
            var previousFilter = map.getFilter('all');
            var columns = previousFilter[1];
            var critera = previousFilter[2];
            map.setFilter('all', ['==', 'Year', 2013]&&['==', columns, critera])
            // map.setFilter('all',previousFilter)
            $("#yearAppend").text("2013")
        }
        if (year == "2014") {
            var previousFilter = map.getFilter('all');
            var columns = previousFilter[1];
            var critera = previousFilter[2];
            map.setFilter('all', ['==', 'Year', 2014]&&['==', columns, critera])
            // map.setFilter('all',previousFilter)
            $("#yearAppend").text("2014")
        }
        if (year == "2015") {
            var previousFilter = map.getFilter('all');
            var columns = previousFilter[1];
            var critera = previousFilter[2];
            map.setFilter('all', ['==', 'Year', 2015]&&['==', columns, critera])
            // map.setFilter('all',previousFilter)
            $("#yearAppend").text("2015")
        }
        if (year == "2016") {
            var previousFilter = map.getFilter('all');
            var columns = previousFilter[1];
            var critera = previousFilter[2];
            map.setFilter('all', ['==', 'Year', 2016]&&['==', columns, critera])
            // map.setFilter('all',previousFilter)
            $("#yearAppend").text("2016")
        }
        if (year == "2017") {
            var previousFilter = map.getFilter('all');
            var columns = previousFilter[1];
            var critera = previousFilter[2];
            map.setFilter('all', ['==', 'Year', 2017]&&['==', columns, critera])
            // map.setFilter('all',previousFilter)
            $("#yearAppend").text("2017")
        }
        

    })

    $("#month").on('change', function(event) {
        var month = $('#month').val();
        console.log(month);

        if (month == "1") {
            console.log("Entered")
            map.setFilter('all', ['==', 'Month', 1])
            $("#monthAppend").text("January")
        }
        if (month == "2") {
            console.log("Entered")
            map.setFilter('all', ['==', 'Month', 2])
            $("#monthAppend").text("February")
        }
        if (month == "3") {
            console.log("Entered")
            map.setFilter('all', ['==', 'Month', 3])
            $("#monthAppend").text("March")
        }
        if (month == "4") {
            console.log("Entered")
            map.setFilter('all', ['==', 'Month', 4])
            $("#monthAppend").text("April")
        }
        if (month == "5") {
            console.log("Entered")
            map.setFilter('all', ['==', 'Month', 5])
            $("#monthAppend").text("May")
        }
        if (month == "6") {
            console.log("Entered")
            map.setFilter('all', ['==', 'Month', 6])
            $("#monthAppend").text("June")
        }
        if (month == "7") {
            console.log("Entered")
            map.setFilter('all', ['==', 'Month', 7])
            $("#monthAppend").text("July")
        }
        if (month == "8") {
            console.log("Entered")
            map.setFilter('all', ['==', 'Month', 8])
            $("#monthAppend").text("August")
        }
        if (month == "9") {
            console.log("Entered")
            map.setFilter('all', ['==', 'Month', 9])
            $("#monthAppend").text("September")
        }
        if (month == "10") {
            console.log("Entered")
            map.setFilter('all', ['==', 'Month', 10])
            $("#monthAppend").text("October")
        }
        if (month == "11") {
            console.log("Entered")
            map.setFilter('all', ['==', 'Month', 11])
            $("#monthAppend").text("November")
        }
        if (month == "12") {
            console.log("Entered")
            map.setFilter('all', ['==', 'Month', 12])
            $("#monthAppend").text("December")
        }
    })

    $("#layerButton").on("click", function(event) {
        console.log(map.getFilter("all"));
    })




});