mapboxgl.accessToken = 'pk.eyJ1IjoiYXNrYWtkYWdyOCIsImEiOiJjanN4ZjB3bG8wcnZlNGFxajVuNWpoanFpIn0.kSd_OxnClSA-DRAsIS4O5Q'; // replace this with your access token
var counter = 0;
var start_viz = {
    0: {
        zoom: 10,
        center: [-122.502104, 37.723089],
        bearing: 0,
        pitch: 0,
        title: 'San Francisco',
        text: `<div>
		    I moved to the Bay Area a few months ago and, for a brief moment, contemplated the thought of living in the city and commuting to the South Bay. 
		    <br>
		    <br>
		    <i>“It’d be the best of both worlds,”</i> I thought. 
		    <br>
		    <br>
		    I quickly changed my mind when I discovered that the one way commute would range from an hour and a half to two hours.
		    <br>
		    <br>
		    Still, I know so many folks that willingly made that tradeoff. It got me thinking of of a visualization I saw about a year ago.
			</div>`
    },
    1: {
        zoom: 12,
        center: [-122.425420, 37.777321],
        bearing: 12.80,
        pitch: 60,
        title: 'San Francisco',
        text: `<div>
		    <br>
		    <br>
		    About a year ago, I saw <a href="https://manpopex.us/">this</a>visualization on Reddit. I was captivated and was determined to replicate it. This would lead me down a wild goose chase across the internet culminating in <a href="#">this</a> write up.
		    <br>
		    <br>
		    Feel free to read that article to see how the visualization was constructed. But for now, let's explore California!
		</div>`
    },
    2:{
    	zoom: 12,
        center: [-122.424635, 37.803721],
        bearing: 93.60,
        pitch: 60,
        title: 'San Francisco',
        text:`<div>
			This is San Francisco.
			<br>
			<br>
			A city marked by innovation and pushing the status quo. A city known for it's "Move Fast and Break Things" motto. A city that's made millionaires and robbed people of their homes overnight.
			<br>
			<br>
			Outside of the bustle of the city, sleepy neighborhoods like Presido and Sunset reside in the background.
		</div>`
    },
    3:{
    	zoom: 12,
        center: [-122.269158, 37.889749],
        bearing: 43.25,
        pitch: 60,
        title: 'University of California - Berkeley',
        text:`<div>
			Just on the other side of the bay, is the University of Califonia - Berkeley.
			<br>
			<br>
			The East Bay is not as dense as San Francisco is but there are pockets of high density.
		</div>`
    },
    4:{
    	zoom: 12,
        center: [-122.223524, 37.790083],
        bearing: 8.80,
        pitch: 33.00,
        title: 'Mercy Retirement & Care Center',
        text:`<div>
			This, for example, is the Mercy Retirement & Care Center in Oakland.
		</div>`
    },
    5:{
    	zoom: 12,
        center: [-122.508447, 37.703982],
        bearing: -68.99,
        pitch: 50.50,
        title: 'San Francisco State University',
        text:`<div>
        	Large spikes such as this one often suggest university dorm rooms.
            <br>
            <br>
            This, for example, is the San Francisco State University.
        	</div>
        `
    },
    6:{
    	zoom: 13.18,
        center: [-122.482874, 37.930357],
        bearing: -116.17,
        pitch: 60.00,
        title: 'San Quentin State Prison',
        text:`<div>
            Other large spikes could indicate a prison.
       	</div>
        `
    },
    7:{
    	zoom: 12,
        center: [-122.383296, 37.778991],
        bearing: -141.93,
        pitch: 49.00,
        title: 'San Francisco',
        text:`
        <div>
        This is where our tour ends. Feel free to explore the map for any other interesting takeaways.</div>
        <br>
        <br>
        <div>You can click <a href="#">here</a> to learn about how I built this map.</div>
        `
    }
};

var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/askakdagr8/cjt2fe0c61rt31fowlugvand4', // replace this with your style URL
    center: start_viz[counter].center,
    zoom: start_viz[counter].zoom,
    pitch: start_viz[counter].pitch,
    bearing: start_viz[counter].bearing
});

$("#title").text(start_viz[counter]["title"]);
$("#text").html(start_viz[counter]["text"])




$("#nextBtn").on("click", function(event) {
    counter++;
    map.flyTo({
        center: start_viz[counter]["center"],
        zoom: start_viz[counter]["zoom"],
        bearing: start_viz[counter]["bearing"],
        pitch: start_viz[counter]["pitch"],
        speed: 0.2
    });
    $("#title").text(start_viz[counter]["title"]);
	$("#text").html(start_viz[counter]["text"]);
});

$("#backBtn").on("click", function(event) {
    counter--;
    map.flyTo({
        center: start_viz[counter]["center"],
        zoom: start_viz[counter]["zoom"],
        bearing: start_viz[counter]["bearing"],
        pitch: start_viz[counter]["pitch"],
        speed: 0.2
    });
    $("#title").text(start_viz[counter]["title"]);
	$("#text").html(start_viz[counter]["text"]);
});
