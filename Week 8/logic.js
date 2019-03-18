
mapboxgl.accessToken = 'pk.eyJ1IjoicGV0ZXJxbGl1IiwiYSI6ImpvZmV0UEEifQ._D4bRmVcGfJvo1wjuOpA1g';

var map = new mapboxgl.Map({
    container: 'map', // container id
    style: 'mapbox://styles/peterqliu/ciug032my008f2ipm1z1rf15q', //stylesheet location
    center: [-122.4232292175293,37.784282779035216], // starting position
    hash: false,
    zoom: 12, // starting zoom
    minZoom: 12,
    maxZoom:16,
      attributionControl: {
      position: 'bottom-left'
    }
});

var minimap = new mapboxgl.Map({
    container: 'minimap', // container id
    style: 'mapbox://styles/peterqliu/ciug032my008f2ipm1z1rf15q', //stylesheet location
    center: [-96.34406, 42], // starting position
    interactive: false,
    hash: false,
    zoom: 1.5
});

// legend
var scale = new mapboxgl.Map({
  container: 'scale', // container id
    style: 'mapbox://styles/peterqliu/ciug08i80007t2inwzocmwno1', //stylesheet location
  center: [0,0], // starting position
  pitch:30,
  hash: false,
  zoom: 12, // starting zoom
});
var km = 0.006383179578579702;
var halfKm = 0.004495196886323735;
var tinySquare = 

// set up legend
  {
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "properties": {
          "pkm2":16000
        },
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [0, halfKm],
              [halfKm,0],
              [0,-halfKm],
              [-halfKm,0],
              [0, halfKm]
            ]
          ]
        }
      }
    ]
  };

  scale.on('load', function(){
    scale.addSource('square', {"type": "geojson", "data": tinySquare})
    .addLayer({
        'id':'extrusions',
        'type':'fill',
        'source':'square',
        'paint':{
          'fill-color':'#eee',
          'fill-extrude-base':0,
          'fill-extrude-height':{"stops": [[0,10],[1450000,20000]], "property": "pkm2", "base": 1},
          'fill-opacity':0.75
        },
        'paint.tilted':{
          'fill-opacity':0.9
        }
    })
  })

// set up minimap

  var greatPlaces = {
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "properties": {
          "city": "San Francisco",
          "scale": 2500000
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            -122.4232292175293,
            37.784282779035216
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "city": "Los Angeles",
          "scale": 2500000
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            -118.28636169433594,
            34.04412546508576
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "city": "Seattle",
          "scale": 2900000
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            -122.33327865600585,
            47.60651025683697
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "city": "New Orleans",
          "scale": 3500000
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            -90.10042190551758,
            29.946159058399612
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "city": "Chicago",
          "scale": 2300000
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            -87.6240348815918,
            41.87531293759582
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "city": "Philadelphia",
          "scale": 1750000
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            -75.1626205444336,
            39.95370120254379
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "city": "New York",
          "scale": 50000
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            -73.99772644042969,
            40.72228267283148
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "city": "Atlanta",
          "scale": 3300000
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            -84.39079284667969,
            33.74910736130734
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "city": "Portland",
          "scale": 3200000
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            -122.67179489135742,
            45.522104713562825
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "city": "Denver",
          "scale": 3200000
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            -104.99565124511719,
            39.74428621972816
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "city": "Minneapolis",
          "scale": 3200000
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            -93.26637268066406,
            44.969656023708175
          ]
        }
      },
      {
        "type": "Feature",
        "properties": {
          "city": "Miami",
          "scale": 2800000
        },
        "geometry": {
          "type": "Point",
          "coordinates": [
            -80.19624710083008,
            25.773846629676616
          ]
        }
      }
    ]
  }

  greatPlaces.features.forEach(function(city, index){
    // create the popup
    var popup = new mapboxgl.Popup({closeButton:false})
        .setText(city.properties.city);

    // create DOM element for the marker
    var el = document.createElement('div');
    el.className = 'marker';
    el.id = 'city'+index;
    // create the marker
    new mapboxgl.Marker(el)
        .setLngLat(city.geometry.coordinates)
        //.setPopup(popup) // sets a popup on this marker
        .addTo(minimap);

    document.getElementById('city'+index).setAttribute('onclick', 'jumpToCity('+index+')')
  })

  function jumpToCity(index){
    var city = greatPlaces.features[index];
    document.querySelector('#slider').value = city.properties.scale;
    map.jumpTo({center:city.geometry.coordinates});
    setScale(city.properties.scale)
  }

  // minimap flyTo interactivity
  minimap.on('mouseup', function(e){
    var coords = (minimap.unproject(e.point))
    map.jumpTo({center:coords})
  })

  // add geocoder
  map.addControl(
    new mapboxgl.Geocoder(
      {'container':document.querySelector('.geocoder'), 'placeholder': 'Explore any US city...', 'country':'us'
      }
    )
  );

  //bind slider to scale-adjusting function
  document.querySelector('#slider')
    .addEventListener('change', function(){
      setScale(parseInt(this.value))
    })

  //oft-used DOM elements
  var tooltip = document.querySelector('#tooltip');
  var blockCount = document.querySelector('#blockcount');
  var blockDensity = document.querySelector('#blockdensity');
  var mapObj = document.querySelector('#map');
  var canvas = document.querySelector('.mapboxgl-canvas-container.mapboxgl-interactive');
  // app state
  var currentBlock; //block id of current block to throttle geocoder
  var inspector = 'block';  //inspector mode (block, radius, none)

  var emptyGeojson = {
    "type": "FeatureCollection",
    "features": []
  };
  map.on('load', function(){

    //set up data sources
    map.addSource('population', {
      'type':'vector',
      'url':'mapbox://peterqliu.d0vin3el'
    })
    .addSource('highlight', {
      'type':'geojson',
      'data': emptyGeojson
    })
    .addSource('radiusHighlight', {
      'type':'geojson',
      'data': emptyGeojson
    })


    //set up data layers
    map
    .addLayer({
      'id':'fills',
      'type':'fill',
      'filter':['all', ['<', 'pkm2', 300000]],
      'source':'population',
      'source-layer':'outgeojson',
      'paint':{
        'fill-color':{"stops": [[0,'#160e23'],[14500,'#00617f'], [145000,'#55e9ff']], "property": "pkm2", "base": 1},
        'fill-opacity':1
      },
      'paint.tilted':{
      }
    }, 'water')

    .addLayer({
    	'id':'extrusions',
      'type':'fill',
      'filter':['all', ['>', 'p', 1], ['<', 'pkm2', 300000]],
      'source':'population',
      'source-layer':'outgeojson',
      'paint':{
        'fill-color':{"stops": [[0,'#160e23'],[14500,'#00617f'], [1450000,'#55e9ff']], "property": "pkm2", "base": 1},
        'fill-extrude-base':0,
        'fill-extrude-height':{"stops": [[0,0],[1450000,20000]], "property": "pkm2", "base": 1},
        //'fill-opacity-transition': {'duration':1000},
        'fill-opacity':0
      },
      'paint.tilted':{
        'fill-opacity':1
      }
    }, 'airport-label')
    .addLayer({
      'id':'radiusHighlight',
      'type':'fill',
      'filter':['all', ['<', 'pkm2', 300000]],
      'source':'radiusHighlight',
      'paint':{
        'fill-extrude-height':{"stops": [[0,0],[1450000,0]], "property": "pkm2", "base": 1},
        'fill-color':{"stops": [[0,'#e53e0e'], [145000,'#f1f075']], "property": "pkm2", "base": 1},
        'fill-opacity':1
      },
      'paint.tilted':{
        'fill-extrude-height':{"stops": [[0,10],[1450000,20000]], "property": "pkm2", "base": 1}
      }
    }, 'water')
    .addLayer({
      'id':'highlighted_fill',
      'type':'line',
      'source':'highlight',
      'paint':{
        'line-color':'orange'
      },
      'paint.tilted':{
        'line-opacity':0
      }
    })
    .addLayer({
      'id':'highlighted_extrusion',
      'type':'fill',
      'source':'highlight',
      'paint':{
        'fill-color':'orange',
        'fill-extrude-base': 0,
        'fill-extrude-height':{"stops": [[0,10],[1450000,20000]], "property": "pkm2", "base": 1},
        'fill-opacity': 0
      },
      'paint.tilted':{
        'fill-opacity':0.5
      }
    }, 'airport-label')

    // sync map to legend

    map
      .on('rotate', function(){
        scale
          .setBearing(map.getBearing())
      })
      .on('zoom', function(){
        var multiplier = map.getZoom()-12;
        document.querySelector('#people').innerHTML = Math.ceil(4000*Math.pow(1/8, multiplier));
      })
      .on('move', function(){
        scale
          .setPitch(map.getPitch()*0.7) //fudge factor to get it to look right on the lower-left corner
      })

    // map tooltip functionality
    map
    .on('mousemove', function(e){


      if (inspector === 'block'){
        var features = map.queryRenderedFeatures(e.point, { layers: ["fills"] });
        var ft = features[0];

        var showTooltip = ft && ft.properties.p>0 && e.originalEvent.which===0;

        if (showTooltip){
          mapObj.classList = 'inspector'

          tooltip.style.transform = 'translateX('+e.point.x+'px) translateY('+e.point.y+'px)'
          blockCount.innerHTML = ft.properties.p
          blockDensity.innerHTML = ft.properties.pkm2;

          map.getSource('highlight').setData(ft)
          canvas.style.cursor = 'mapboxgl-canvas-container mapboxgl-interactive inspector'

          if (ft.properties.id !== currentBlock){
            var coord = ft.geometry.coordinates[0][0];
            var queryURL = 'https://api.mapbox.com/geocoding/v5/mapbox.places/'+coord+'.json?access_token=pk.eyJ1IjoicGV0ZXJxbGl1IiwiYSI6ImpvZmV0UEEifQ._D4bRmVcGfJvo1wjuOpA1g'
            mapboxgl.util.getJSON(queryURL, function(err, resp){
              currentBlock = ft.properties.id;
              var address = resp.features[0].address+' '+resp.features[0].text;
              document.querySelector('#address').innerHTML = 'Near '+ address.replace('undefined ', '');
            })
          }
        }

        else {
          map.getSource('highlight').setData(emptyGeojson)
          mapObj.classList = ''
        }
      }

      if (inspector === 'radius'){
        mapObj.classList = 'inspector'

        var pt = map.unproject(e.point)
        //var circle = (drawCircle([pt.lng, pt.lat],0.5));
        //map.getSource('highlight').setData(circle)
        updateBlocks(pt, 0.5)
          tooltip.style.transform = 'translateX('+e.point.x+'px) translateY('+e.point.y+'px)'

      }

    })
    .on('mouseout', function(){
      map.getSource('radiusHighlight').setData(emptyGeojson)
      map.getSource('highlight').setData(emptyGeojson)
    })
    setScale(2500000)
  })

  // map tilt functionality
  function tilt(eh){
    var state = !eh ? {pitch:0, klass:['']} : {pitch:50, klass:['tilted']}

    document.querySelector('#legends').className = 'pin-bottomright scale '+state.klass[0]
    map
      .easeTo({pitch: state.pitch})
      .setClasses(state.klass)

    scale.fire('resize');
  }

  // adjust scale
  function setScale(max){
    max = 3950000-max;
    document.querySelector('#max').innerHTML = max+'+';
    scale
      .setPaintProperty('extrusions', 'fill-extrude-height',{"stops": [[0,10],[max,20000]], "property": "pkm2", "base": 1})
    map.setPaintProperty('fills', 'fill-color',{"stops": [[0,'#160e23'],[max*0.02,'#00617f'], [max*0.1,'#55e9ff']], "property": "pkm2", "base": 1})
    .setPaintProperty('extrusions', 'fill-color',{"stops": [[0,'#160e23'],[max*0.02,'#00617f'], [max*0.1,'#55e9ff']], "property": "pkm2", "base": 1})
    .setPaintProperty('extrusions', 'fill-extrude-height',{"stops": [[0,10],[max,20000]], "property": "pkm2", "base": 1})
    .setPaintProperty('highlighted_extrusion', 'fill-extrude-height',{"stops": [[0,10],[max,20000]], "property": "pkm2", "base": 1})
  }

  // show/hide labels
  function toggleLabels(truthiness){
    var visibility = truthiness ? 'visible' : 'none'
    map.style.stylesheet.layers.forEach(function(layer){
      if (layer.type === 'symbol') map.setLayoutProperty(layer.id, 'visibility', visibility)
    })
  }

  // show/hide roads
  function toggleRoads(truthiness){
    var visibility = truthiness ? 'visible' : 'none'
    map.style.stylesheet.layers.forEach(function(layer){
      if (layer.type === 'line') map.setLayoutProperty(layer.id, 'visibility', visibility)
    })
  }

  function setInspector(mode){
    inspector = mode;
    var klass = mode === 'none' ? '' : 'inspector'
    mapObj.classList = klass;

    if (mode === 'none') {
      map.getSource('radiusHighlight').setData(emptyGeojson)
      map.getSource('highlight').setData(emptyGeojson)
    }
    if (mode === 'radius') document.querySelector('#address').innerHTML = 'Within 500 meters of here'
  }

  function pointBuffer (pt, radius, units, resolution) {
    var ring = []
    var resMultiple = 360/resolution;
    for(var i  = 0; i < resolution; i++) {
      var spoke = turf.destination(pt, radius, i*resMultiple, units);
      ring.push(spoke.geometry.coordinates);
    }
    if((ring[0][0] !== ring[ring.length-1][0]) && (ring[0][1] != ring[ring.length-1][1])) {
      ring.push([ring[0][0], ring[0][1]]);
    }
    return turf.polygon([ring])
  }

  function drawCircle(center,radius){
    var pt = turf.point(center);
    var circle = pointBuffer(pt, radius, 'kilometers', 22)
    circle.properties.bbox = turf.bbox(circle)
    circle.properties.pkm2 = 0;
    return circle
  }

  function drawRadiusCircle(){
    var edgeX = turf.destination(turf.point([lnglat.lng, lnglat.lat]), radius, 90, 'kilometers');
    var pixelRadius = (map.project(edgeX.geometry.coordinates).x-map.project(lnglat).x);

    radiusCircle
      .style({width: 2*pixelRadius+'px', height: 2*pixelRadius+'px'})
  }

  function updateBlocks(lnglat, radius){
    var circle = drawCircle([lnglat.lng, lnglat.lat], radius)

    //calculate extent of circle
    var circleExtent = turf.bbox(circle);
    var nw = map.project([circleExtent[0],circleExtent[1]]);
    var se = map.project([circleExtent[2],circleExtent[3]]);
    nw = [nw.x, nw.y];
    se = [se.x, se.y];

    //get blocks within the circle's extent
    var geometryOutput = map.queryRenderedFeatures([nw,se],{ layers: ['fills'] });

    var intersectedBlocks = [];
    var totalPop = 0;

    var ruler = cheapRuler(lnglat.lat, 'meters');
    geometryOutput.forEach(function(poly){
      var density = poly.properties.pkm2;
      try {

        var poly = turf.polygon(poly.geometry.coordinates);
        poly.properties.bbox = turf.bbox(poly);

        //calculate intersect only if it collides at all
        var intersect = turf.intersect(poly, circle)
        intersect.properties.pkm2 = density;

        //if there is an intersect,
        if (intersect !== undefined) {
          // add intersected geometry to featurecollection
          intersectedBlocks.push(intersect)

          //add intersected population to the total
          var blockPop = ruler.area(poly.geometry.coordinates)*density;
          totalPop+= blockPop
        }
      } 

      catch(e) {return;}
    });

    blockCount.innerHTML = parseInt(totalPop);
    blockDensity.innerHTML = parseInt(totalPop/0.79);
    map.getSource('radiusHighlight')
      .setData(turf.featureCollection(intersectedBlocks));
  }
