/*
	greenpot.js
	Simulation of a green sea port using system dynamics
	
	Sparisom Viridi | gs _HjSaE0AAAAJ
	Suprijadi       | gs MJJnvxUAAAAJ
	
	20201106
	0344 Use greenport as template.
	0516 Still do the layout.
	0641 Create Growable class.
*/


// Define something that can grow linearly
class Growable {
	constructor(state, max, rate) {
		this.state = arguments[0];
		this.max = arguments[1];
		this.rate = arguments[2];
	}
	
	setState() {
		this.state = arguments[0];
	}
	
	setMax() {
		this.max = arguments[0];
	}
	
	setRate() {
		this.rate = arguments[0];
	}
	
	grow() {
		var dt = arguments[0];
		var newState = this.state + this.rate * dt;
		if(newState <= this.max) {
			this.state = newState;
		}
	}
}


// Define spherical cell Cell
class Cell {
	constructor() {
		this.D = new Growable(1, 10, 0.1);
		this.m = 1;
		this.q = 0;
		this.r = new Vect3();
		this.v = new Vect3();
	}
};


// Define global variables
var blue;
var ta, tw, th, tah;
var div;
var can, cw, ch;
var proc, Tproc, tbeg, tend, dt, t;
var cell;

// Initialize visual elements
function initElements() {
	// Create canvas
	can = document.createElement("canvas");
	can.style.float = "left";
	can.style.width = cw + "px";
	can.style.height = ch + "px";
	can.style.border = blue + " 1px solid";
	
	// Create div
	div = document.createElement("div");
	div.style.float = "left";
	div.style.width = dw + "px";
	div.style.height = dh + "px";
	
	// Create textarea
	tah = document.createElement("textarea");
	tah.style.width = tw + "px";
	tah.style.height = "16px";
	tah.style.background = blue;
	tah.style.color = "#fff";
	tah.disabled = true;
	
	ta = document.createElement("textarea");
	ta.style.overflowY = "scroll";
	ta.style.width = tw + "px";
	ta.style.height = th + "px";
	ta.style.border = blue + " 1px solid";
	ta.disabled = true;

	document.body.append(div);
		div.append(tah);
		div.append(ta);
	document.body.appendChild(can);
}


// Resize textarea according to window inner size
function resize() {
	// When textarea is the only element
	var dw = 20;
	var dh = 2 * 26;
	tah.style.width = (window.innerWidth - dw) + "px";
	ta.style.width = (window.innerWidth - dw) + "px";
	ta.style.height = (window.innerHeight - dh) + "px";
}


// Initialize parameters
function initParams() {
	// Set elements (c, t, d) width and height
	cw = 400;
	ch = 400;
	tw = 400;
	th = ch - 30;
	dw = tw + 6;
	dh = ch;

	// Set blue color
	blue = "#"
		+ (079).toString(16)
		+ (129).toString(16)
		+ (189).toString(16);

	// Set time parameters
	tbeg = 0;
	tend = 10;
	dt = 1;
	t = tbeg;
	
	// Set interval parameter
	Tproc = 10;
	
	// Initialize variables and parameters
	cell = [];
	var first = new Cell();
	cell.push(first);
}


// Start simulation
function start() {
	proc = setInterval(simulate, Tproc);
}


// Stop simulation
function stop() {
	clearInterval(proc);
}


// Add line to textrea
function tout() {
	var ta = arguments[0];
	var line = arguments[1];
	ta.value += line;
	ta.scrollTop = ta.scrollHeight;
}


// Add label and value
function addValue() {
	l.push(arguments[0]);
	x.push(arguments[1]);
}


// Simulate
function simulate() {
	// Initialize all variables and coefficient
	if(t == tbeg) {

		var header =
			"TIME  " +
			"";
			
		tout(tah, header);
		tout(ta, header + "\n");
	}
	
	// Display variables on textarea
	tout(ta,
		("0000" + t).slice(-4) + "  " +
		"\n"
	);
	
	// Stop simulation when tend is reached
	if(t >= tend) {
		stop();
	} else {
		t += dt;
	}
}


// Define main function
function main() {
	initParams();
	initElements();
	start();
}


// Execute program
main();
