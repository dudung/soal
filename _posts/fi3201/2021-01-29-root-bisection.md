---
layout: post
author: viridi
title: root bisection
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["fi3201", "root", "bisection"]
date: 2021-01-30 18:13:00 +07
permalink: /fi3201/root-bisection
---
One of the root finding algorithms is bisection method, which applies to any continuous functions that has values with opposite signs in the search range [[1](#ref1)]. It is an iterative method that divides previous internal into two subintervals and then evaluate which subintervals should be used, there the function still has value with opposite signs [[2](#ref2)]. There is a lot of use of similar principle in scientific works [[3](#ref3)].


## swap function
A swap function is a function that exchanges its two arguments value

\begin{equation}
\label{eqn:rb-swap-function}
{\rm swap}(\vec{r}) = (\vec{r} \cdot \hat{y})\hat{x} + (\vec{r} \cdot \hat{x})\hat{y},
\end{equation}

where $\vec{r} = x\hat{x} + y\hat{r}$ is used to store two values, i.e. $x$ and $y$, in single output. If $\vec{r} = 1.5\hat{x} - 7.2\hat{y}$ then ${\rm swap}(\vec{r})$ will produce $-7.2\hat{x} + 1.5\hat{y}$ or simply

\begin{equation}
\label{eqn:rb-swap-function-example}
(1.5, -7,2) \rightarrow (-7.2, 1.5).
\end{equation}

There is a built-in function in C++ standard template libray (STL) [[4](#ref4)] in the form of

```c++
swap(a, b)
```

with `a` and `b` are two mandatory parameters to be swapped. Manually there are some algorithms to perform the swap process without using a temporary variable but using arithmetic or bitwise operation or mixture of them [[5](#ref5)] or other ways [[6](#ref6)]. There is also a clever user defined function for the swap function in MATLAB [[7](#ref7)], while in Python a fine syntax already provided [[8](#ref8)]. We will use this function in designing more readable algorithm for bisection method.


## algorithm
Let us assume that there is a function $f(x)$, which holds for $f(x_{\rm beg}) f(x_{\rm end}) < 0$, when $x \in [x_{\rm beg}, x_{\rm end}]$.

Algorithm <a name="alg:rb-bisection-method-algorithm">1</a> Bisection method. \
`I`: $f(x)$, $x_{\rm beg}$, $x_{\rm end}$, $\epsilon$. \
`O`: $x_{\rm root}$.
1. $n = 1$.
2. $x_n \leftarrow x_{\rm beg}$.
3. $x_{n+1} \leftarrow x_{\rm end}$.
4. $x_{n+2} \leftarrow \frac12 (x_{n+1} + x_n)$.
5. $f(x_{n+1}) f(x_{n+2}) < 0 \Rightarrow \color{blue}{\bf\scriptsize STEP} \ 7$.
6. ${\rm swap}(x_n, x_{n+1})$.
7. $\|f(x_{n+2})\| < \epsilon \Rightarrow \color{blue}{\bf\scriptsize STEP} \ 10$.
8. $n \leftarrow n + 1$.
9. $\Rightarrow \color{blue}{\bf\scriptsize STEP} \ 4$.
10. $x_{\rm root} \leftarrow x_{n+2}$.

A function $f(x)$ as an example will be solved using Alg. <a href="#alg:rs-bisection-method-algorithm">1</a>.


## flowchart
We can also use a flowchart to design how steps of finding root using bisection method instead of using Alg. <a href="#alg:rb-bisection-method-algorithm">1</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/root/root-bisection-flow-chart.png)
<br />
Figure <a name="fig:rb-bisection-method-flow-chart">1</a> Steps in bisection method are described in a flow chart. 
{: refdef}

Number of elements in the flowchart shown in Fig. <a href="#fig:rb-bisection-method-flow-chart">1</a> is more than in the Alg. <a href="#alg:rs-bisection-method-algorithm">1</a> since short expressions in every element are required, e.g. in decision block we use $f_{\rm root} < \epsilon$ instead of $\|f(x_{n+2})\| < \epsilon$ as in the algorithm.


## test function
A function

\begin{equation}
\label{eqn:rb-test-function}
f(x) = 0.025x^3 - 0.2585x^2 + 0.243x + 0.5265 
\end{equation}

is used as test function in implementing the bisection method from the flowchart shown in Fig. <a href="#fig:rb-bisection-method-flow-chart">1</a> or Alg. <a href="#alg:rs-bisection-method-algorithm">1</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/root/root-bisection-1.png)
![..](/assets/img/math/root/root-bisection-2.png)
![..](/assets/img/math/root/root-bisection-3.png)
<br />
Figure <a name="fig:rb-example">2</a> Scanning a root with $x_{\rm beg} = 1$ and $x_{\rm end} = 8$, the points are $x_1 = 8$, $x_2 = 1$, $x_3 = 4.5$ (top), $x_2 = 4.5$, $x_3 = 1$, $x_4 = 2.75$ (middle), and $x_3 = 1$, $x_4 = 2.75$, $x_5 = 1.875$ (bottom). 
{: refdef}

Fig. <a href="#fig:rb-example">2</a> shows that root predictions are $x_1 = 8$, $x_2 = 4.5$, $x_3 = 1$, $x_4 = 2.75$, and  $x_5 = 1.875$. The swap operation changing the order or $x_{n}$ and $x_{n+1}$ will make the order of predictions not in historical order.

```batch
n       x       f(x)
0       8       -1.2734999999999999
1       1       -1.2734999999999999
2       4.5     -1.3365000000000007
3       2.75    -0.240234375
4       1.875   0.23813085937499995
5       2.3125  0.015229736328124854
6       2.53125 -0.109217010498047
7       2.421875        -0.04607417678833026
8       2.3671875       -0.015180088520050261
9       2.33984375      8.689016103746727e-05

f(x)   0.025x^3 - 0.2585x^2 + 0.243x + 0.5265
xbeg  1
xend  8
ε     0.001
Nstep 10
xroot 2.33984375
```

Output of program given above still show the historical orde since it is printed before the wap process and here is

```
[8, 4.5, 1, 1.875, 2.75, 2.53125, 2.421875, 2.3125, 2.3671875, 2.353515625, 2.3466796875, 2.34326171875, 2.341552734375, 2.3406982421875, 2.34027099609375, 2.33984375, 2.340057373046875, 2.3399505615234375, 2.339977264404297, 2.3399906158447266, 2.3400039672851562, 2.3399972915649414, 2.340000629425049]
```

the predictions which has the order as in Fig. <a href="#fig:rb-example">2</a>, where $x_4$ and $x_5$ are still not in the historical order since the $x_6$ has not yet been calculated at that step.


## implementation
The output is designed as follow

```batch
f(x)  0.025x^3 - 0.2585x^2 + 0.243x + 0.5265
xbeg  1
xend  8
ε     0.1
Nstep 6
xroot 2.3125
```

with ome implementations are given here, e.g. in Python, JavaScript, GNU Octave, C++.

### python
Following code `root-bisection.py` has been tested using Python 3.7.7 through Cygwin version 2.873 on Windows 10 Home.

```python
# Import necessary libraries
import numpy as np


# Define a test function
def test_function(x):
	y3 = 0.025 * x * x * x;
	y2 = -0.2585 * x * x;
	y1 = 0.243 * x;
	y0 = 0.5265;
	y = y3 + y2 + y1 + y0;
	return y


# Define input
f = test_function
xbeg = 1
xend = 8
eps = 1E-3
Nstep = 0
maxstep = 40
n = 0

# Define default message and parameter
xroot = "not found"
SHOW_PROGRESS = False

# Do iteration
Nstep = 0
x = []
x.append(xbeg)
x.append(xend)
froot = np.abs(f(x[n+1]))

while n <= maxstep-3 and froot > eps:
	x.append(0.5*(x[n] + x[n+1]))
	
	fn1 = f(x[n+1])
	fn2 = f(x[n+2])
	c = fn1 * fn2
	if c > 0:
		x[n], x[n+1] = x[n+1], x[n]
	
	if SHOW_PROGRESS:
		if n == 0:
			fn = f(x[n])
			print("n\tx\tf(x)")
			print(n, x[n], fn, sep="\t")
			print(n+1, x[n+1], fn1, sep="\t")
		print(n+2, x[n+2], fn2, sep="\t") 
	
	froot = np.abs(fn2)
	if froot < eps:
		xroot = x[n+2]
	
	n += 1

Nstep = n+2

if SHOW_PROGRESS:
	print()

# Display result
print("f(x)   0.025x^3 - 0.2585x^2 + 0.243x + 0.5265");
print("xbeg  ", xbeg, sep="")
print("xend  ", xend, sep="")
print("ε     ", eps, sep="")
print("Nstep ", Nstep, sep="")
print("xroot ", xroot, sep="")
```

Full source code with comments can be accessed [here](https://github.com/butiran/butiran.github.io/blob/master/src/py/fi3201/root/root-bisection.py)

$\epsilon$ | $1$ | $0.1$ | $0.01$ | $10^{-3}$ | $10^{-4}$ | $10^{-5}$ | $10^{-6}$
$N_{\rm step}$ | $4$ | $6$ | $10$ | $10$ | $10$ | $19$ | $23$
$x_{\rm root}$ | $2.75$ | $2.3125$ | $2.33984375$ | $2.33984375$ | $2.33984375$ | $2.3400039672851562$ | $2.340000629425049$

Using $x_{\rm beg} = 1$ and $x_{\rm end} = 8$ we can have results in the previous table.

### javascript
Following code `root-bisection.js` is tested using Node.js v10.1.0 on Windows 10 Home.

```javascript
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
	var eps = 1E-6;
	var Nstep = 0;
	
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
		
		// Get the xroot
		if(froot <= eps) {
			Nstep = n + 2;
			xroot = x[n+2];
		}
		
		// Increase n
		n++;
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
```

Full source code with comments can be accessed [here](https://github.com/butiran/butiran.github.io/blob/master/src/js/fi3201/root/root-bisection.js)

$\epsilon$ | $1$ | $0.1$ | $0.01$ | $10^{-3}$ | $10^{-4}$ | $10^{-5}$ | $10^{-6}$
$N_{\rm step}$ | $4$ | $6$ | $10$ | $10$ | $10$ | $19$ | $23$
$x_{\rm root}$ | $2.75$ | $2.3125$ | $2.33984375$ | $2.33984375$ | $2.33984375$ | $2.3400039672851562$ | $2.340000629425049$

Using $x_{\rm beg} = 1$ and $x_{\rm end} = 8$ we can have results in the previous table.

### octave
Following code `root-bisection.m` is tested using GNU Octave version 5.2.0 through Cygwin version 2.873 on Windows 10 Home.

```m
% Define a swap function according to [2]
function [b, a] = swap(a, b)
endfunction


% Define a function whose root to be found
function y = test_function (x)
y = 0.025 * x**3 - 0.2585 * x**2 + 0.243 * x + 0.5265;
endfunction


% Define input parameters
xbeg = 1;
xend = 8;
eps = 1E-1;
Nstep = 0;

% Create variables for output
xroot = xend;
maxstep = 20;
n = 1;

% Initialize variables
x = [];
x(n) = xbeg;
x(n+1) = xend;
froot = abs(test_function(x(n+1)));

% Do iteration using bisection method
while((froot > eps) && (n < maxstep - 1))
	% Do bisection the search range
	x(n+2) = 0.5 * (x(n+1) + x(n));
	
	% Swap if necessary
	fn1 = test_function(x(n+1));
	fn2 = test_function(x(n+2));
	c = fn2 * fn1;
	if(c > 0)
		[x(n+1), x(n)] = swap(x(n+1), x(n));
	endif
	
	% Caculate absoulte value of the function
	froot = abs(test_function(x(n+2)));
		
	% Get the xroot
	if(froot <= eps)
		Nstep = n + 2 ;
		xroot = x(n+2);
	endif
	
	% Increase n
	n++;
endwhile

% Case of root not found in the search range
if(Nstep == 0)
	str_xroot = "not found";
	Nstep = maxstep;
else
	str_xroot = num2str(xroot);
endif

% Display output
disp(["f(x)  0.025x^3 - 0.2585x^2 + 0.243x + 0.5265"]);
disp(["xbeg  " num2str(xbeg)]);
disp(["xend  " num2str(xend)]);
disp(["ε     " num2str(eps)]);
disp(["Nstep " num2str(Nstep)]);
disp(["xroot " str_xroot]);
```

Full source code with comments can be accessed [here](https://github.com/butiran/butiran.github.io/blob/master/src/m/fi3201/root/root-bisection.m)

$\epsilon$ | $1$ | $0.1$ | $0.01$ | $10^{-3}$ | $10^{-4}$ | $10^{-5}$ | $10^{-6}$
$N_{\rm step}$ | $4$ | $6$ | $10$ | $10$ | $10$ | $19$ | $23$
$x_{\rm root}$ | $2.75$ | $2.3125$ | $2.3398$ | $2.3398$ | $2.3398$ | $2.34$ | $2.34$

Using $x_{\rm beg} = 1$ and $x_{\rm end} = 8$ we can have results in the previous table.

### c++
Following code `root-bisection.cpp` has been tested using g++ (GCC) 10.2.0 through Cygwin version 2.873 on Windows 10 Home.

```c++
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
```

Full source code with comments can be accessed [here](https://github.com/butiran/butiran.github.io/blob/master/src/cpp/fi3201/root/root-bisection.cpp)

$\epsilon$ | $1$ | $0.1$ | $0.01$ | $10^{-3}$ | $10^{-4}$ | $10^{-5}$ | $10^{-6}$
$N_{\rm step}$ | $4$ | $6$ | $10$ | $10$ | $10$ | $19$ | $23$
$x_{\rm root}$ | $2.75$ | $2.3125$ | $2.33984$ | $2.33984$ | $2.33984$ | $2.34$ | $2.34$

Using $x_{\rm beg} = 1$ and $x_{\rm end} = 8$ we can have results in the previous table.


## exercises
1. Comparing the given flowchart in Fig. <a href="#fig:rb-bisection-method-flow-chart">1</a> and algoritm in Alg. <a href="#alg:rs-bisection-method-algorithm">1</a>, which one suits you better? Give your opinion about it.
2. Modify the flowchart in Fig. <a href="#fig:rb-bisection-method-flow-chart">1</a> so that number of elements is the same as in Alg. <a href="#alg:rs-bisection-method-algorithm">1</a>. Is it simpler or more comples compared the given flowchart? Explain in brief.
3. Not as shown in Fig. <a href="#fig:rb-bisection-method-flow-chart">1</a> or Alg. <a href="#alg:rs-bisection-method-algorithm">1</a> the implementation in the given Octave program there is `maxstep` variable. Explain what the use of this variable. And why we require it?
4. Compare the obtained $x_{\rm root}$ using different codes, e.q. `root-bisection.py`, `root-bisection.js`, `root-bisection.m`, `root-bisection.cpp` and discuss about them.
5. Can you design some lines of code that can save the prediction of $x$ as in historical order and in the order after swap process? Explain that in brief.


## references
1. <a name="ref1"></a>Wikipedia contributors, "Bisection method", Wikipedia, The Free Encyclopedia, 12 January 2021, 04:52 UTC, <https://en.wikipedia.org/w/index.php?oldid=999831078> [20210129].
2. <a name="ref2"></a>Eric W. Weisstein, "Bisection" from MathWorld--A Wolfram Web Resource, url <https://mathworld.wolfram.com/Bisection.html> [20210129].
3. <a name="ref3"></a>url <https://www.sciencedirect.com/topics/engineering/bisection-algorithm> [20210129].
4. <a name="ref4"></a>Prateek Sharma 7, "swap() in C++", GeeksforGeeks, 01 May 2019, url <https://www.geeksforgeeks.org/swap-in-cpp/> [20210129].
5. <a name="ref5"></a>GeeksforGeeks contributors (jit_t, mohit kumar 29, Chandan_Kumar, Code_Mech, ujjwalmittal, rathbhupendra, SHUBHAMSINGH10, Rajput-Ji, supershounak2001, yashbeersingh42, divyeshrabadiya07, bunnyram19, divyesh072019), "How to swap two numbers without using a temporary variable?", GeeksforGeeks, 11 Dec 2020, url <https://www.geeksforgeeks.org/swap-two-numbers-without-using-temporary-variable/> [20210129].
6. <a name="ref6"></a>Piyush Kochhar, "10 Ways To Swap Values In JavaScript", codeburst.io, 12 Aug 2020, url <https://codeburst.io/10-ways-to-swap-values-in-javascript-8a1d056352dd> [20210129].
7. <a name="ref7"></a>Jan, "Answer to 'How to swap values of two variables?'", MATLAB Answers, MathWorks, 23 Oct 2017, url <https://www.mathworks.com/matlabcentral/answers/362680-how-to-swap-values-of-two-variables#answer_287217> [20210130].
8. <a name="ref8"></a>eyquem, pauloue, "Answer to 'Is there a standardized method to swap two variables in Python?'", StackOverflow, 22 Jan 2018, url <https://stackoverflow.com/a/14836456> [20210130].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi3201/2021-01-29-root-bisection.md)

{% comment %}
1. Adrio Rivan xn swap xn+1
2. Felix Cahyadi: tanya bisection kelemahannya rentang terlalu besar
3. Bunga Edenia: 18001: perihal kuliah hari Jumat
4 Khalda Alifia: gunakan ketiga bahasa C++, JS, Python?
{% endcomment %}
