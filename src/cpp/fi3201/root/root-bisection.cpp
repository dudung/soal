/*
	root-bisection.js
	Finding root using bisection method
	
	Sparisoma Viridi | https://butiran.github.io/
	
	Compile: g++ root-bisection.cpp -o root-bisection
	Execute: root-bisection
	
	20210130
	1213 Start from root-scanning.cpp, root-bisection.js codes.
	1233 Continue to modify, lunch.
	1313 After lunch.
*/

// Include necessary libraries
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

// Define some functions
double test_function(double);

int main(int argc, char *argv[]) {
	// Define input
	double xbeg = 1;
	double xend = 8;
	double eps = 1E-6;
	int Nstep = 0;
	bool SHOW_PROGRESS = false;
	
	// Define default value
	double not_found = -2021;
	double xroot = not_found;
	
	// Create variables for output
	int maxstep = 40;
	int n = 0;
	
	// Initialize variables
	vector<double> x;
	x.push_back(xbeg);
	x.push_back(xend);
	double froot = fabs(test_function(x[n+1]));
	
	while((froot > eps) && (n < maxstep)) {
		// Do bisection the search range
		x.push_back(0.5 * (x[n+1] + x[n]));
		
		// Swap if necessary
		double fn1 = test_function(x[n+1]);
		double fn2 = test_function(x[n+2]);
		double c = fn2 * fn1;
		if(c > 0) {
			swap(x[n+1], x[n]);
		}
		
		cout << n << "\t" << x[n+2] << "\t" << fn2 << endl;
		
		// Caculate absoulte value of the function
		froot = fabs(test_function(x[n+2]));
		
		if(froot < eps) {
			xroot = x[n+2];
		}
		
		// Increase n
		n++;
	}
	Nstep = n;
	
	// Display result
	cout << "f(x)  ";
	cout << "0.025x^3 - 0.2585x^2 + 0.243x + 0.5265" << endl;
	cout << "xbeg  " << xbeg << endl;
	cout << "xend  " << xend << endl;
	cout << "ε     " << eps << endl;
	cout << "Nstep " << Nstep << endl;
	if(xroot == not_found) {
		cout << "xroot not found" << endl;
	} else {
		cout << "xroot " << xroot << endl;
	}
	
	cout << x.size() << endl;
	
	return 0;
}


// Define test function
double test_function(double x) {
	double y3 = 0.025 * x * x * x;
	double y2 = -0.2585 * x * x;
	double y1 = 0.243 * x;
	double y0 = 0.5265;
	double y = y3 + y2 + y1 + y0;
	return y;
}


/*
// Define main function
function main() {
	// Define input parameters
	var xbeg = 1;
	var xend = 8;
	var eps = 1E-6;
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
*/