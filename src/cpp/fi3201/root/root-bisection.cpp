/*
	root-bisection.cpp
	Finding root using bisection method
	
	Sparisoma Viridi | https://butiran.github.io/
	
	Compile: g++ root-bisection.cpp -o root-bisection
	Execute: root-bisection
	
	20210130
	1213 Start from root-scanning.cpp, root-bisection.js codes.
	1233 Continue to modify, lunch.
	1313 After lunch, use vector, and ok.
	1617 Continue to use SHOW_PROGRESS.
	1636 Test for all four conditions, ok.
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
		
		// Display the progress
		if(SHOW_PROGRESS) {
			if(n == 0) {
				double fn = test_function(x[n]);
				cout << "n\tx\tf(x)" << endl;
				cout << (n) << "\t";
				cout << x[n] << "\t";
				cout << fn << endl;
				cout << (n+1) << "\t";
				cout << x[n+1] << "\t";
				cout << fn1 << endl;
			}
			cout << (n+2) << "\t" << x[n+2] << "\t" << fn2 << endl;
		}
		
		// Caculate absoulte value of the function
		froot = fabs(test_function(x[n+2]));
		
		if(froot < eps) {
			xroot = x[n+2];
		}
		
		// Increase n
		n++;
	}
	Nstep = n + 2;
	
	if(SHOW_PROGRESS) {
		cout << endl;
	}
	
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
