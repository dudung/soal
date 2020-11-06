/*
	greenpot.js
	Simulation of a green sea port using system dynamics
	
	Sparisom Viridi | gs _HjSaE0AAAAJ
	Suprijadi       | gs MJJnvxUAAAAJ
	
	20201106
	0344 Use greenport as template.
	0516 Still do the layout.
	0641 Create Growable class.
	0738 Create Color class.
	0900 Finish create Range and Conversion classes.
	0915 Create Process class.
	0946 Process does not work.
	1020 It can work now, using arguments in setInterval.
	1024 Clean all lines of code.
	1034 Set absolute of distance in Conversion.
	1045 Can draw a single growing circular cell.
*/


// Define a process of a function every period
class Process {
	constructor() {
		this.func = arguments[0];
		this.period = arguments[1];
		this.beg = arguments[2];	
		this.end = arguments[3];
		this.inc = arguments[4];
		
		this.cur = this.beg;
	}
	
	setPeriod() {
		this.period = arguments[0];
	}
	
	setFunction() {
		this.func = arguments[0];
	}
	
	setIteration() {
		this.beg = arguments[0];	
		this.end = arguments[1];
		this.inc = arguments[2];	
		
		this.cur = this.beg;
	}
	
	step() {
		this.cur = this.cur + this.inc;
		if(this.cur > this.end) {
			this.cur = this.end;
			this.stop();
		}
	}
	
	start() {
		this.id = setInterval(
			function() {
				arguments[0].func();
				arguments[0].step();
			},
			this.period,
			this
		);
	}
	
	stop() {
		clearInterval(this.id);
	}
	
}


// Define a conversion
class Conversion {
	constructor() {
		this.src = arguments[0];
		this.dest = arguments[1];
	}
	
	setSrc() {
		this.src = arguments[0];
	}
	
	setDest() {
		this.dest = arguments[0];
	}
	
	coordinate() {
		var x = arguments[0];
		
		var min = this.src.min;
		var max = this.src.max;
		
		var MIN = this.dest.min;
		var MAX = this.dest.max;
		
		var X = (x - min) / (max - min);
		X *= (MAX - MIN);
		X += MIN;
		
		return X;
	}
	
	distance() {
		var a = 0;
		var b = a + arguments[0];
		var A = this.coordinate(a);
		var B = this.coordinate(b);
		var L = Math.abs(B - A);
		return L;
	}
}


// Define a range
class Range {
	constructor() {
		this.min = arguments[0];
		this.max = arguments[1];
	}
	
	setMin() {
		this.min = arguments[0];
	}
	
	setMax() {
		this.max = arguments[0];
	}
}


// Define outline and fill colors
class Color {
	constructor() {
		if(arguments.length == 0) {
			this.outline = "#000";
			this.fill = "#fff";
		} else if(arguments.length == 1) {
			this.outline = arguments[0];
			this.fill = "#fff";
		} else if(arguments.length == 2) {
			this.outline = arguments[0];
			this.fill = arguments[1];
		}
	}
	
	setOutline() {
		this.outline = arguments[0];
	}
	
	setFill() {
		this.fill = arguments[0];
	}
}


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
		this.r = new Vect3(50, 50, 0);
		this.v = new Vect3();
		this.c = new Color(blue, "#fff");
	}
};


// Define global variables
var blue;
var ta, tw, th, tah;
var div;
var can, cw, ch;
var proc, Tproc, tbeg, tend, dt, t;
var cell;
var cx, xmin, xmax, XMIN, XMAX;
var cy, ymin, ymax, YMIN, YMAX;


// Initialize parameters
function initParams() {
	// Set elements (c, t, d) width and height
	cw = 400;
	ch = 400;
	tw = 400;
	th = ch - 30;
	dw = tw + 6;
	dh = ch;
	
	// Set conversion parameters for drawing
	var xmin = 0;
	var xmax = 100;
	var rngx = new Range(xmin, xmax);
	var ymin = 0;
	var ymax = 100;
	var rngy = new Range(ymin, ymax);
	var XMIN = 0;
	var XMAX = cw;
	var RNGX = new Range(XMIN, XMAX);
	var YMIN = ch;
	var YMAX = 0;
	var RNGY = new Range(YMIN, YMAX);
	cx = new Conversion(rngx, RNGX);
	cy = new Conversion(rngy, RNGY);
	
	// Set blue color
	blue = "#"
		+ (079).toString(16)
		+ (129).toString(16)
		+ (189).toString(16);

	// Set time parameters and proces
	tbeg = 0;
	tend = 500;
	dt = 1;
	t = tbeg;
	Tproc = 10;
	proc = new Process(simulate, Tproc, tbeg, tend, dt);
	
	// Initialize variables and parameters
	cell = [];
}


// Initialize visual elements
function initElements() {
	// Create canvas
	can = document.createElement("canvas");
	can.style.float = "left";
	can.width = cw;
	can.height = ch;
	can.style.width = can.width + "px";
	can.style.height = can.height + "px";
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


// Add line to textarea
function tout() {
	var ta = arguments[0];
	var line = arguments[1];
	ta.value += line;
	ta.scrollTop = ta.scrollHeight;
}


// Draw a cell on canvas
function draw() {
	var cell = arguments[0];
	
	var x = cell.r.x;
	var y = cell.r.y;
	var r = 0.5 * cell.D.state;
	
	var X = Math.round(cx.coordinate(x));
	var Y = Math.round(cy.coordinate(y));
	var R = Math.round(0.5 * (cx.distance(r) + cy.distance(r)));
	
	var outline = cell.c.outline;
	var fill = cell.c.fill;
	
	var val = {
		on() {
			var can = arguments[0];
			var ctx = can.getContext("2d");
			
			ctx.lineWidth = 2;
			ctx.beginPath();
			
			ctx.strokeStyle = outline;
			ctx.arc(X, Y, R, 0, 2 * Math.PI);
			ctx.stroke();
			
			/*
			ctx.fillStyle = fill;
			ctx.arc(X, Y, R, 0, 2 * Math.PI);
			ctx.fill();
			*/
		}
	};
	
	return val;
}


// Clear canvas and textarea
function clear() {
	var el = arguments[0];
	if(el instanceof HTMLTextAreaElement) {
		el.value = "";
	} else if(el instanceof HTMLCanvasElement) {
		var cx = el.getContext("2d");
		cx.clearRect(0, 0, cw, ch);
	}
}


// Define main function
function main() {
	initParams();
	initElements();
	proc.start();
}


// Execute program
main();


// Perform simulation
function simulate() {
	// Initialize all variables and coefficient
	if(proc.cur == proc.beg) {
		
		var first = new Cell();
		first.r = new Vect3(48, 50, 0);
		cell.push(first);

		var second = new Cell();
		second.r = new Vect3(52, 50, 0);
		cell.push(second);
		
		var header =
			"TIME  " +
			"";
			
		tout(tah, header);
		tout(ta, header + "\n");
	}
	
	
	// Draw cells
	var N = cell.length;
	clear(can);
	for(var i = 0; i < N; i++) {
		draw(cell[i]).on(can);
	}	
	
	// Display variables on textarea
	t = proc.cur;
	tout(ta,
		("0000" + t).slice(-4) + "  " +
		"\n"
	);
		
	// Grow cells
	var N = cell.length;
	for(var i = 0; i < N; i++) {
		cell[i].D.grow(dt);
	}
	
	// Move cells
	var N = cell.length;
	for(var i = 0; i < N; i++) {
		
	}
}
