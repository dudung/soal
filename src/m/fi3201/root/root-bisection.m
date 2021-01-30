%	
%	root-bisection.m
%	Find root of a function using bisection method
%	
%	Sparisoma Viridi | https://github.com/dudung
%	
%	Execute: octave -W root-bisection.m
%	
%	20210130
%	0514 Start learning CLI Cywin for Octave aft-yest-install.
%	0549 Learn disp and num2str using doc <topic>.
%	0600 Learn about function using doc display.
%	0634 Create function for testing, a 3rd oder polynomial.
%	0833 Add reference 1.
%	0900 Problem, debug, re-test test_function and ok.
%	0945 Finalize and test the program, and ok.
%	0958 Rewrite with better elseif instead of else if [3].
%	1000 Test for not found and SHOW_PROGRESS, ok.
%	
%	References
%	1. Rody Oldenhuis, "Answer to 'Octave/Matlab: Adding new
%	   elements to a vector'", StackOverflow, 24 Apr 2013, url
%	   https://stackoverflow.com/a/16188096 [20210130].
%	2. Jan, "Answer to 'How to swap values of two variables?'",
%	   MATLAB Answers, MathWorks, 23 Oct 2017, url
%	   https://www.mathworks.com/matlabcentral/answers
%	   /362680-how-to-swap-values-of-two-variables
%	   #answer_287217 [20210130].
%	3. John W. Eaton, "GNU Octave", 2016, url
%	   https://octave.org/doc/v4.0.1/The-if-Statement.html
%	   [20210130].
%	


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
eps = 1E-6;
Nstep = 0;
SHOW_PROGRESS = false;

% Create variables for output
xroot = xend;
maxstep = 40;
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
	
	% Display the progress
	if(SHOW_PROGRESS)
		if(n == 1)
			disp(["n" "\t" "x" "\t" "f(x)"]);
			
			s1 = num2str(n);
			s2 = num2str(x(n));
			s3 = num2str(froot);
			disp([s1 "\t" s2 "\t" s3]);
			
			s1 = num2str(n+1);
			s2 = num2str(x(n+1));
			s3 = num2str(froot);
			disp([s1 "\t" s2 "\t" s3]);
		endif
		s1 = num2str(n+2);
		s2 = num2str(x(n+2));
		s3 = num2str(froot);
		disp([s1 "\t" s2 "\t" s3]);
	endif
	
	% Get the xroot
	if(froot <= eps)
		Nstep = n + 2;
		xroot = x(n+2);
	endif
	
	% Increase n
	n++;
endwhile
if(SHOW_PROGRESS)
	disp("");
endif

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
