/*
	greenpot.js
	Simulation of a green sea port using system dynamics
	
	Sparisom Viridi | gs _HjSaE0AAAAJ
	Tatang Suheri | gs Rjv0zt0AAAAJ
	
	20201029
	0827 Start to code.
	0946 Able to resize textarea while window.
	1008 Try to show time stamp.
*/


// Define global variables
var ta, dw, dh;
var proc, Tproc, tbeg, tend, dt, t;
var l, x, a, b, c;


// Initialize visual elements
function initElements() {
	// Create textarea
	dw = 20;
	dh = 26;
	ta = document.createElement("textarea");
	ta.style.overflowY = "scroll";
	ta.style.width = (window.innerWidth - dw) + "px";
	ta.style.height = (window.innerHeight - dh) + "px";
	document.body.appendChild(ta);
	
	// Add listener for resize event
	window.addEventListener("resize", resize);
}


// Resize textarea according to window inner size
function resize() {
	ta.style.width = (window.innerWidth - dw) + "px";
	ta.style.height = (window.innerHeight - dh) + "px";
}


// Initialize parameters
function initParams() {
	// Set time parameters
	tbeg = 0;
	tend = 12 * 1;
	dt = 1;
	t = tbeg;
	
	// Set interval parameter
	Tproc = 10;
	
	// Initialize variables and parameters
	l = [];
	x = [];
	a = [];
	b = [];
	c = [];
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
	var line = arguments[0];
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
		
		GTEC = 1.0;
		GDPP = 1000;
		GDPU = 1000;
		PCTC = 100;
		
		c_TRAD_GDPU = 0.001;
		c_PDEM_TRAD = 1;
		c_PCTX_PDEM = 1;
		c_GDPP_PCTX = 1;
		c_GDPU_GDPP = 0.05;
	
		c_ENEO_GDPP = 0.2;
		c_ENEO_GTEC = 0.1;
		c_WASD_GDPP = 0.2;
		c_WASD_GTEC = 0.1;
		c_WATO_GDPP = 0.2;
		c_WATO_GTEC = 0.1;
		
		c_PPRE_PDEM = 1;
		c_GDPU_PPRE = 20;
		
		c_PINV_GDPU = 0.01;
		c_PCTC_PINV = 0.1;
		
		tout(
			"TIME  GDPP   GDPU   ENEO   WASD   WATO "
			+ "\n"
		);
	} else {
	}
		
	// Green Technology
	ENEO = c_ENEO_GDPP * GDPP - c_ENEO_GTEC * GTEC;
	WASD = c_WASD_GDPP * GDPP - c_WASD_GTEC * GTEC;
	WATO = c_WATO_GDPP * GDPP - c_WATO_GTEC * GTEC;
	
	// Port
	TRAD = c_TRAD_GDPU * GDPU;
	PDEM = c_PDEM_TRAD * TRAD;
	PCTX = c_PCTX_PDEM * PDEM;
	
	PPRE = c_PPRE_PDEM * PDEM / PCTC;
	
	PINV = c_PINV_GDPU * GDPU;
	PCTC = PCTC + c_PCTC_PINV * PINV;
	
	// GDP
	GDPP = GDPP + c_GDPP_PCTX * PCTX;
	GDPU = GDPU + c_GDPU_GDPP * GDPP - c_GDPU_PPRE * PPRE;
	
	
	// Display variables on textarea
	tout(
		("0000" + t).slice(-4) + "  " +
		("0000" + Math.round(GDPP)).slice(-5) + "  " +
		("0000" + Math.round(GDPU)).slice(-5) + "  " +
		("0000" + Math.round(PCTC)).slice(-5) + "\n"
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
	initElements();
	initParams();
	start();
}


// Execute program
main();
