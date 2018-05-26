var crimeSelected = $('input[name=crime]:checked').val();
var yearSelected = 2010;
var monthSelected = 1;
var dayofweekSelected = "Monday";
var columns;
var criteria;


mapboxgl.accessToken = 'pk.eyJ1IjoiYXNrYWtkYWdyOCIsImEiOiJjamgzbW04MmowNTJlMndueG1tNGU4OGQ1In0.7G4btoI3KCFFq6gPr6MdeA';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/light-v9',
    // maxZoom: 15,
    minZoom: 12,
    pitch: 60.0,
    bearing: 20.35,
    center: [-122.343161, 47.611673]
});


map.on('load', function() {
    console.log('Map Display ' + crimeSelected);

    map.addLayer({
        'id': 'total',
        'type': 'circle',
        'source': {
            type: 'vector',
            url: 'mapbox://askakdagr8.9tklrr8g'
        },
        'source-layer': 'GroupedOutput-9i6ink',
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



    map.setFilter('total', [
        "all", ['==', 'Event Clearance Group', 'SHOPLIFTING'],
        ["==", "Day of Week", "Monday"],
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
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            map.setPaintProperty('total', 'circle-color', '#faafee');
        }
        if (crimeSelected == "ROBBERY") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            map.setPaintProperty("total", "circle-color", "#f48341");
        }
        if (crimeSelected == "PROSTITUTION") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            map.setPaintProperty("total", "circle-color", "#f4c141");
        }
        if (crimeSelected == "NARCOTICS COMPLAINTS") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            map.setPaintProperty("total", "circle-color", "#e5f441");
        }
        if (crimeSelected == "BURGLARY") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            map.setPaintProperty("total", "circle-color", "#82f441");
        }
        if (crimeSelected == "AUTO THEFTS") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            map.setPaintProperty("total", "circle-color", "#41f48b");
        }
        if (crimeSelected == "HOMICIDE") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            map.setPaintProperty("total", "circle-color", "#41f4d9");
        }
        if (crimeSelected == "ASSAULTS") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            map.setPaintProperty("total", "circle-color", "#42b6ff");
        }
        if (crimeSelected == "ARREST") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            map.setPaintProperty("total", "circle-color", "#4151ff");
        }
        if (crimeSelected == "CAR PROWL") {
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            map.setPaintProperty("total", "circle-color", "#a43dff");
        }

    });





    $("#month").on('change', function(event) {
        var month = $('#month').val();
        console.log(month);

        if (month == "1") {
            monthSelected = 1;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            $("#monthAppend").text("January")
        }
        if (month == "2") {
            monthSelected = 2;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            $("#monthAppend").text("February")
        }
        if (month == "3") {
            monthSelected = 3;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            $("#monthAppend").text("March")
        }
        if (month == "4") {
            monthSelected = 4;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            $("#monthAppend").text("April")
        }
        if (month == "5") {
            monthSelected = 5;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            $("#monthAppend").text("May")
        }
        if (month == "6") {
            monthSelected = 6;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            $("#monthAppend").text("June")
        }
        if (month == "7") {
            monthSelected = 7;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            $("#monthAppend").text("July")
        }
        if (month == "8") {
            monthSelected = 8;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            $("#monthAppend").text("August")
        }
        if (month == "9") {
            monthSelected = 9;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            $("#monthAppend").text("September")
        }
        if (month == "10") {
            monthSelected = 10;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            $("#monthAppend").text("October")
        }
        if (month == "11") {
            monthSelected = 11;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            $("#monthAppend").text("November")
        }
        if (month == "12") {
            monthSelected = 12;
            setfilter(["==", "Event Clearance Group", crimeSelected], ["==", "Day of Week", dayofweekSelected], ["==", "Month", monthSelected])
            $("#monthAppend").text("December")
        }
    })

    $("#layerButton").on("click", function(event) {
        console.log(map.getFilter("total"));
    })




});