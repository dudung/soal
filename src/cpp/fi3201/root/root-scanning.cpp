/*
	root-scanning.js
	Finding root using scanning method
	
	Sparisoma Viridi | https://butiran.github.io/
	
	Compile: g++ root-scanning.cpp -o root-scanning
	Execute: root-scanning
	
	20210128
	0616 Start this program, copy comments from js file.
	0627 Add reference for sign function, test it, ok.
	0637 Pause can not reference a function as in JS.
	0706 Continue from JS example.
	0714 Test it for found and not found, and ok.
	0716 Add notes 1 and 2.
	
	References
	1. Mark Byers, "Answer to 'Is there a standard sign
	   function (signum, sgn) in C/C++?'", StackOverflow,
		 14 Dec 2009 22:3-0, url
		 https://stackoverflow.com/a/1903975 [20210128].
	
	Notes
	1. One of the output message is still static and does not
	   depend on the given parameters. Remember to change it
		 when you change the parameters.
	2. A not_found = -2021 is defined for a state when root
	   can not be found in the given range of x.
*/

// Include necessary libraries
#include <iostream>

using namespace std;

// Define some functions
double sign(double);
double test_function(double);

int main(int argc, char *argv[]) {
	// Define input
	double xbeg = 2;
	double xend = 5;
	double dx = 1;
	
	// Define default value
	double not_found = -2021;
	double xroot = not_found;
	
	// Do iteration
	double S0, S;
	int Nstep = 0;
	double x = xbeg;
	while(x <= xend) {
		// Increase Nstep;
		Nstep++;
		
		// Calculate S0 and S
		double fx = test_function(x);
		if(x == xbeg) {
			S0 = sign(fx);
		} else {
			S = sign(fx);
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
	cout << "f(x)  0.05(x+1)(x-3.45)(x-8)" << endl;
	cout << "Δx    " << dx << endl;
	cout << "xbeg  " << xbeg << endl;
	cout << "xend  " << xend << endl;
	cout << "Nstep " << Nstep << endl;
	if(xroot == not_found) {
		cout << "xroot not found" << endl;
	} else {
		cout << "xroot " << xroot << endl;
	}
	
	return 0;
}


// Implement sign function from [1]
double sign(double x) {
	return (x < 0) ? -1 : ((x > 0) ? 1 : 0);
}


// Define test function
double test_function(double x) {
	double a = 0.05;
	double x1 = -1;
	double x2 = 3.45;
	double x3 = 8;
	double y = a*(x-x1)*(x-x2)*(x-x3);
	return y;
}
