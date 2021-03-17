/*
	root-bisection.js
	Finding root using bisection method
	
	Sparisoma Viridi | https://butiran.github.io/
	
	Execute: node root-bisection.js
	
	20210130
	1113 Start this program from Octave code.
	1152 Test it and ok, add some comments.
	1209 Run for eps from 1 to 1E-6, and ok.
	
	References
	1. Brian Genisio, "Answer to 'javascript function to swap
	   two variables'", StackOverflow, 10 May 2016 20:42, url
	   <https://stackoverflow.com/a/37148611> [20210130]
*/


// Define test function
function test_function() {
	var x = arguments[0];
	var y3 = 0.025 * x * x * x;
	var y2 = -0.2585 * x * x;
	var y1 = 0.243 * x;
	var y0 = 0.5265;
	var y = y3 + y2 + y1 + y0;
	return y;
}


// Define main function
function main() {
	// Define input parameters
	var xbeg = 1;
	var xend = 8;
	var eps = 1E-0;
	var Nstep = 0;
	var SHOW_PROGRESS = false;
	
	// Create variables for output
	var f = test_function;
	var xroot = xend;
	var maxstep = 40;
	var n = 0;
	
	// Initialize variables
	var x = [];
	x.push(xbeg);
	x.push(xend);
	var froot = Math.abs(f(x[n+1]));
	
	// Do iteration using bisection method
	while((froot > eps) && (n < maxstep - 1)) {
		// Do bisection the search range
		x[n+2] = 0.5 * (x[n+1] + x[n]);
		
		// Swap if necessary
		fn1 = f(x[n+1]);
		fn2 = f(x[n+2]);
		c = fn2 * fn1;
		if(c > 0) {
			[x[n+1], x[n]] = [x[n], x[n+1]];
		}
		
		// Caculate absoulte value of the function
		froot = Math.abs(f(x[n+2]));
		
		// Display the progress
		if(SHOW_PROGRESS) {
			if(n == 1) {
				console.log("n\tx\tf(x)");
				var frootn = f(x[n]);
				var frootn1 = f(x[n+1]);
				console.log(n + "\t" + x[n] + "\t" + frootn);
				console.log((n+1) + "\t" + x[n+1] + "\t" + frootn1);
			}
			var frootn2 = f(x[n+2]);
			console.log((n+2) + "\t" + x[n+2] + "\t" + frootn2);
		}
		
		// Get the xroot
		if(froot <= eps) {
			Nstep = n + 2;
			xroot = x[n+2];
		}
		
		// Increase n
		n++;
	}
	if(SHOW_PROGRESS) {
		console.log("");
	}
	
	// Case of root not found in the search range
	if(Nstep == 0) {
		xroot = "not found";
		Nstep = maxstep;
	}	
	
	// Display output
	console.log("f(x)  0.025x^3 - 0.2585x^2 + 0.243x + 0.5265");
	console.log("xbeg  " + xbeg);
	console.log("xend  " + xend);
	console.log("ε     " + eps);
	console.log("Nstep " + Nstep);
	console.log("xroot " + xroot);
}


// Call main function
main();