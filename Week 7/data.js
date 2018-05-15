mapboxgl.accessToken = "pk.eyJ1IjoiYXNrYWtkYWdyOCIsImEiOiJjamgzbW04MmowNTJlMndueG1tNGU4OGQ1In0.7G4btoI3KCFFq6gPr6MdeA"

var map = new mapboxgl.Map({
 container: 'map',
 style: 'mapbox://styles/mwidener/ciuvowcno00ee2js5wibckxv3',
 center: [-79.388924,43.645],
 zoom: 14,
 minZoom: 13, //restrict map zoom - buildings not visible beyond 13
 maxZoom: 20,
 pitch: 60, //tilt camera
 bearing: 17.5 //adjust angle we're looking (17.5 degrees from north)
});

var features=[];

var layers = [
 //Color Height threshold Label
 ['#ffffcc', 15, '0-15 Meters'],
 ['#ffeda0', 30, '15-30 Meters'],
 ['#fed976', 50, '30-50 Meters'],
 ['#feb24c', 100, '50-100 Meters'],
 ['#fd8d3c', 200, '100-200 Meters'],
 ['#fc4e2a', 300, '200-300 Meters'],
 ['#e31a1c', 400, '300-400 Meters'],
 ['#bd0026', 500, '400-500 Meters']
];

//create a popup object and give it some properties. we'll generate/overwrite a new popup each time we click.
var popup = null;

map.on('style.load', function(){
 var legend = document.getElementById('legend'); //get the legend from the HTML document
 map.addSource('building_source', {
 'url': 'vector',
 'url': 'mapbox://mwidener.1ayxbus1' //location of 3d building data
 });

 layers.forEach(function(layer, i){
 map.addLayer({
 'id': 'building_layer-' + i,
 'type': 'fill',
 'source': 'building_source',
 'paint': {
 'fill-color': layer[0],
 'fill-opacity': 0.6,
 'fill-extrude-height': { //grab the height from the 'EleZ' attribute from building data
 'type': 'identity',
 'property': 'EleZ'
 },
 'fill-extrude-base': 0
 },
 'source-layer': 'Archive-bcz1gm' //source layer of 3d building data on mapbox studio
 });
 // Build out legends
 //***********//
 var item = document.createElement('div');//each layer gets a 'row' - this isn't in the legend yet, we do this later
 var key = document.createElement('span');//add a 'key' to the row. A key will be the color circle
 var value = document.createElement('span');//add a value variable to the 'row' in the legend

 key.className = 'legend-key'; //the key will take on the shape and style properties defined here, in the HTML
 key.style.backgroundColor = layer[0]; // the background color is retreived from teh layers array

 value.id = 'legend-value-' + i; //give the value variable an id that we can access and change

 item.appendChild(key); //add the key (color cirlce) to the legend row
 item.appendChild(value);//add the value to the legend row

 legend.appendChild(item); // Add row to the legend

 });

 layers.forEach(function(layer, i) {
 var filters = ['all',['<=', 'EleZ', layer[1]]];
 if (i !== 0) filters.push(['>', 'EleZ', layers[i - 1][1]]);
 map.setFilter('building_layer-' + i, filters);
 document.getElementById('legend-value-' + i).textContent = layer[2];//.toLocaleString(); //as we iterate through the layers
 //get the correct row, and add the appropriate text //get the correct row, and add the appropriate text
 });
});

//create an array that has the name of all layers created above
var all_added_layers = []
layers.forEach(function(layer,i){
 all_added_layers.push('building_layer-'+i);
})

map.on('mousemove', function(e){
 features = map.queryRenderedFeatures(e.point, {all_added_layers}); //get features that are in building layers
 if (features.length > 0){
 console.log(features[0].id);
 //use the following code to change the cursor to a pointer ('pointer') instead of the default ('')
 map.getCanvas().style.cursor = (features[0].properties.EleZ != null) ? 'pointer' : '';
 }
 //if there are no provinces under our mouse, then change the cursor back to the default
 else {
 map.getCanvas().style.cursor = '';
 }
});

//an event where when there is a mouse click, send the event data (represented by e) to a function that does something
map.on('click', function(e) {
 popup = new mapboxgl.Popup({
 closeButton: true,
 closeOnClick: true
 });

 //get the spatial features where your mouse is currently located. note we use the pixel location (e.point) and not lat/lon here.
 //also specify the feature we want to pay attention to - 'provinces_base'
 var features = map.queryRenderedFeatures(e.point, {layers: all_added_layers});
 if (features.length > 0 && features[0].properties.EleZ != null){ //if there is a feature in our features array then proceed. otherwise, we don't have anything to work with
 //center at click locations
 map.panTo(e.lngLat, {'duration': 1000});
 //set the location of our popup to the lnglat of our click (note we use e.lnglat here and NOT e.point)
 popup.setLngLat(e.lngLat);
 //give the popup content
 popup.setHTML(
 '<center>The height of this building is approximately: <b>' + Math.round(features[0].properties.EleZ) + '</b> meters.'
 );
 //finally add the popup to the map
 popup.addTo(map);
 }

 //if there are no features that we're interested in, reset the filter for provinces_hover and remove any popup.
 else{
 //map.setFilter('provinces_hover',['==','PRVNAME','']);
 popup.remove();
 }

});
