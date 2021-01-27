/*
	root-scanning.js
	Finding root using scanning method
	
	Sparisoma Viridi | https://butiran.github.io/
	
	Execute: node root-scanning.js
	
	20210128
	0500 Start this program.
	0545 Test it and it works.
	0600 Add notes 1 and 2.
	
	Notes
	1. One of the output message is not related to a, x1, x2,
	   x3, which means that if they are changed you must also
		 change the message manually.
	2. The main function is not essential since you can write
	   it directly without it, but it is made so only for
		 flexibilty, e.g you want to experiment with more than
		 one main fucntion. It is easier to opt out a function
		 than put some lines into comments.
*/


// Define a test function
function test_function() {
	var x = arguments[0];
	var a = 0.05;
	var x1 = -1;
	var x2 = 3.45;
	var x3 = 8;
	var y = a*(x-x1)*(x-x2)*(x-x3);
	return y;
}


// Define main function
function main() {
	// Define input
	var f = test_function;
	var xbeg = 3;
	var xend = 5;
	var dx = 1;
	
	// Define default message
	var xroot = "not found";
	
	// Do iteration
	var S0, S;
	var Nstep = 0;
	var x = xbeg;
	while(x <= xend) {
		// Increase Nstep;
		Nstep++;
		
		// Calculate S0 and S
		if(x == xbeg) {
			S0 = Math.sign(f(x));
		} else {
			S = Math.sign(f(x));
		}
		
		// Check S0.S for root
		if(x > xbeg) {
			if(S0 * S < 0) {
				xroot = x - 0.5 * dx;
				break;
			}
		}
		x += dx;
	}
	
	// Display result
	console.log("f(x)  0.05(x+1)(x-3.45)(x-8)");
	console.log("Δx    " + dx);
	console.log("xbeg  " + xbeg);
	console.log("xend  " + xend);
	console.log("Nstep " + Nstep);
	console.log("xroot " + xroot);
}


// Call main function
main();