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
	
	References
	1. Mark Byers, "Answer to 'Is there a standard sign
	   function (signum, sgn) in C/C++?'", StackOverflow,
		 14 Dec 2009 22:3-0, url
		 https://stackoverflow.com/a/1903975 [20210128].
*/

// Include necessary libraries
#include <iostream>

using namespace std;

// Define some functions
double sign(double);
double test_function(double);

int main(int argc, char *argv[]) {
	
	
	double fx = test_function(0);
	cout << fx << endl;
	
	
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
