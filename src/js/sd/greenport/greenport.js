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
var proc, Tproc, tmin, tmax, dt, t;


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
	tmin = 0;
	tmax = 12 * 20;
	dt = 1;
	t = tmin;
	
	Tproc = 100;
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


// Simulate
function simulate() {
	tout(t + "\n");
	
	if(t >= tmax) {
		stop();
	} else {
		t += dt;
	}
}


// Define main function
function main() {
	initElements();
	initParams();
}


// Execute program
main();
