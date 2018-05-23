var crimeSelected = $('input[name=crime]:checked').val();
var yearSelected = 2010;
var monthSelected = 1;
var columns;
var criteria;


mapboxgl.accessToken = 'pk.eyJ1IjoiYXNrYWtkYWdyOCIsImEiOiJjamgzbW04MmowNTJlMndueG1tNGU4OGQ1In0.7G4btoI3KCFFq6gPr6MdeA';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/light-v9',
    maxZoom: 15,
    minZoom: 12,
    pitch: 60.0,
    bearing: 20.35,
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
        'id': 'total',
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

    // map.setFilter('total', ['==', 'Event Clearance Group', 'SHOPLIFTING'])
    map.setFilter('total', [
        "all", ['==', 'Event Clearance Group', 'SHOPLIFTING'],
        ["==", "Year", 2010],
        ["==", "Month", 1]
    ])
    map.setPaintProperty('total', 'circle-color', '#faafee');

    function setfilter(array1, array2, array3) {
        map.setFilter('total', [
            "all", array1,
            array2, array3
        ])
    }

    $("#crimeFilter").on('change', function(event) {
        crimeSelected = $('input[name=crime]:checked').val();
        console.log(crimeSelected);
        if (crimeSelected == "SHOPLIFTING") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            map.setPaintProperty('total', 'circle-color', '#faafee');
        }
        if (crimeSelected == "ROBBERY") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            map.setPaintProperty("total", "circle-color", "#f48341");
        }
        if (crimeSelected == "PROSTITUTION") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            map.setPaintProperty("total", "circle-color", "#f4c141");
        }
        if (crimeSelected == "NARCOTICS COMPLAINTS") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            map.setPaintProperty("total", "circle-color", "#e5f441");
        }
        if (crimeSelected == "BURGLARY") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            map.setPaintProperty("total", "circle-color", "#82f441");
        }
        if (crimeSelected == "AUTO THEFTS") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            map.setPaintProperty("total", "circle-color", "#41f48b");
        }
        if (crimeSelected == "HOMICIDE") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            map.setPaintProperty("total", "circle-color", "#41f4d9");
        }
        if (crimeSelected == "ASSAULTS") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            map.setPaintProperty("total", "circle-color", "#42b6ff");
        }
        if (crimeSelected == "ARREST") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            map.setPaintProperty("total", "circle-color", "#4151ff");
        }
        if (crimeSelected == "CAR PROWL") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            map.setPaintProperty("total", "circle-color", "#a43dff");
        }

    });




    $("#year").on('change', function(event) {
        var year = $('#year').val();
        console.log(year);

        if (year == "2009") {
            yearSelected = 2009;
            var previousFilter = map.getFilter('total');
            var columns = previousFilter[1];
            var critera = previousFilter[2];
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            // map.setFilter('total',previousFilter)
            $("#yearAppend").text("2009")
        }
        if (year == "2010") {
            yearSelected = 2010;
            var previousFilter = map.getFilter('total');
            var columns = previousFilter[1];
            var critera = previousFilter[2];
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            // map.setFilter('total',previousFilter)
            $("#yearAppend").text("2010")
        }

        if (year == "2011") {
            yearSelected = 2011;
            var previousFilter = map.getFilter('total');
            var columns = previousFilter[1];
            var critera = previousFilter[2];
            console.log(previousFilter);
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            // setfilter(columns,critera)
            // map.setFilter('total',previousFilter)
            $("#yearAppend").text("2011")
        }
        if (year == "2012") {
            yearSelected = 2012;
            var previousFilter = map.getFilter('total');
            var columns = previousFilter[1];
            var critera = previousFilter[2];
            console.log(previousFilter);
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            // setfilter(columns,critera)
            $("#yearAppend").text("2012")
        }
        if (year == "2013") {
            yearSelected = 2013;
            var previousFilter = map.getFilter('total');
            var columns = previousFilter[1];
            var critera = previousFilter[2];
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            // map.setFilter('total',previousFilter)
            $("#yearAppend").text("2013")
        }
        if (year == "2014") {
            yearSelected = 2014;
            var previousFilter = map.getFilter('total');
            var columns = previousFilter[1];
            var critera = previousFilter[2];
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            // map.setFilter('total',previousFilter)
            $("#yearAppend").text("2014")
        }
        if (year == "2015") {
            yearSelected = 2015;
            var previousFilter = map.getFilter('total');
            var columns = previousFilter[1];
            var critera = previousFilter[2];
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            // map.setFilter('total',previousFilter)
            $("#yearAppend").text("2015")
        }
        if (year == "2016") {
            yearSelected = 2016;
            var previousFilter = map.getFilter('total');
            var columns = previousFilter[1];
            var critera = previousFilter[2];
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            // map.setFilter('total',previousFilter)
            $("#yearAppend").text("2016")
        }
        if (year == "2017") {
            yearSelected = 2017;
            var previousFilter = map.getFilter('total');
            var columns = previousFilter[1];
            var critera = previousFilter[2];
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected])
            // map.setFilter('total',previousFilter)
            $("#yearAppend").text("2017")
        }




    })

    $("#month").on('change', function(event) {
        var month = $('#month').val();
        console.log(month);

        if (month == "1") {
            monthSelected = 1;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected]);
            $("#monthAppend").text("January")
        }
        if (month == "2") {
            monthSelected = 2;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected]);
            $("#monthAppend").text("February")
        }
        if (month == "3") {
            monthSelected = 3;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected]);
            $("#monthAppend").text("March")
        }
        if (month == "4") {
            monthSelected = 4;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected]);
            $("#monthAppend").text("April")
        }
        if (month == "5") {
            monthSelected = 5;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected]);
            $("#monthAppend").text("May")
        }
        if (month == "6") {
            monthSelected = 6;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected]);
            $("#monthAppend").text("June")
        }
        if (month == "7") {
            monthSelected = 7;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected]);
            $("#monthAppend").text("July")
        }
        if (month == "8") {
            monthSelected = 8;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected]);
            $("#monthAppend").text("August")
        }
        if (month == "9") {
            monthSelected = 9;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected]);
            $("#monthAppend").text("September")
        }
        if (month == "10") {
            monthSelected = 10;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected]);
            $("#monthAppend").text("October")
        }
        if (month == "11") {
            monthSelected = 11;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected]);
            $("#monthAppend").text("November")
        }
        if (month == "12") {
            monthSelected = 12;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Year", yearSelected], ["==", "Month", monthSelected]);
            $("#monthAppend").text("December")
        }
    })

    $("#layerButton").on("click", function(event) {
        console.log(map.getFilter("total"));
    })




});