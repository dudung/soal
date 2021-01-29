% 
% root-bisection.m
% Find root of a function using bisection method
% 
% Sparisoma Viridi | https://github.com/dudung
% 
% Execute: octave -W root-bisection.m
% 
% 20210130
% 0514 Start learning CLI Cywin for Octave aft-yest-install.
% 0549 Learn disp and num2str using doc <topic>.
% 0600 Learn about function using doc display.
% 0634 Create function for testing, a 3rd oder polynomial.
% 


% Define a function whose root to be found
function y = test_function (x)
y = 0.025 * x**3 - 0.2585 * x**2 + 0.243 * x + 0.5265;
endfunction


% Define input parameters
xbeg = 1;
xend = 8;
eps = 1E-3;

% Create variables for output
xroot = xend;
Nstep = 1;


froot = test_function(xend);

i = 1;
N = 10;
while(i < N)
	disp(i);
	i++;
endwhile

% Display output
disp(["f(x)  0.025x^3 - 0.2585x^2 + 0.243x + 0.5265"]);
disp(["xbeg  " num2str(xbeg)]);
disp(["xend  " num2str(xend)]);
disp(["ε     " num2str(eps)]);
disp(["Nstep " num2str(Nstep)]);
disp(["xroot " num2str(xroot)]);
