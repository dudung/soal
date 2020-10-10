/*
	oo-ui.js
	User Interface for oo in designing some SVG objects
	
	Sparisoma Viridi | https://github.com/dudung
	
	20201010
	1827 Start this file after confused with right directory.
	1838 It must be included first before called.
	1936 Test displaySimpleUI and it works.
	1959 Copy class Conversion from 2020-10-05-oo-scatter-plot.
	2009 Start to design a basic UI.
*/


// Design a basic UI
function displayBasicUI() {
	var div = document.createElement("div");
	div.style.border = "1px solid #ccf";
	div.style.background = "#fafaff";
	
	var taIn = document.createElement("textarea");
	taIn.style.overflowY = "scroll";
	taIn.style.height = "100px";
	
	var taOut = document.createElement("textarea");
	taOut.style.overflowY = "scroll";
	taOut.style.height = "100px";
	
	document.body.append(div);
	div.append(taIn);
	div.append(taOut);
}


// Class of Conversion
class Conversion {
	constructor() {
		this.min = arguments[0];
		this.max = arguments[1];
		this.MIN = arguments[2];
		this.MAX = arguments[3];
	}
	
	// Convert from x in [min, max] to X in [MIN, MAX]
	from() {
		var i = arguments[0];
		var I = (i - this.min) / (this.max - this.min);
		I *= (this.MAX - this.MIN);
		I += this.MIN;
		return I;
	}
};


// Display button than can show message when it is clicked
function displaySimpleUI() {
	var msg = arguments[0];
	var div = document.createElement("div");
	div.style.border = "1px solid #fcc";
	div.style.background = "#fffafa";
	
	var btn = document.createElement("button");
	btn.innerHTML = "Click me!";
	var span = document.createElement("span");
	
	document.body.append(div);
	div.append(btn);
	div.append(span);
	
	btn.addEventListener("click", function() {
		span.innerHTML = "      " + msg;
	});
}


// Display message in console
function displayHelloWorldInConsole() {
	console.log("Hello, World!");
}
