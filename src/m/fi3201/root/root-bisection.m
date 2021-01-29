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
% 


% Define a function whose root to be found
function y = test_function (x)
y = 2 * x;
endfunction

% Define input
xbeg = 2;
xend = 4;
xroot = test_function(xbeg + xend);


disp(["xbeg  " num2str(xbeg)]);
disp(["xend  " num2str(xend)]);
disp(["xroot " num2str(xroot)]);
