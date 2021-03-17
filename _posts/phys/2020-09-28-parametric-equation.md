---
layout: post
author: viridi
title: parametric equation
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: ["topics"]
date: 2020-09-28 18:12:00 +07
permalink: /physics/parametric-equation
---
A type of equation that employs an independent variable (parameter) is parametric equation [[1](#ref1)]. It provides a convenient way to represent curves and surfaces [[2](#ref2)]. Equations of this type are commonly used in kinematics, where the trajectory of an object is represented by equations depending on time $t$ as the parameter [[3](#ref3)].


## Equation
As an example we choose a two-dimensional motion, e.g. parabolic motion, circular motion, and motion with [step function velocity](step-function-velocity). Each coordinate, $x$ and $y$, will have an independent function

\begin{equation}
\label{eqn:pe-x=f(t)}
x = f(t)
\end{equation}

and

\begin{equation}
\label{eqn:pe-y=g(t)}
y = g(t),
\end{equation}

where $f(t)$ and $g(t)$ are function of time $t$. In Eqns. \eqref{eqn:pe-x=f(t)} and \eqref{eqn:pe-y=g(t)} $t$ is the variable (parameter) of the parametric equations. Actually, you can define any arbitraty variable as parameter. Eqn. \eqref{eqn:pe-x=f(t)} can be further written as

\begin{equation}
\label{eqn:pe-t=f^-1(x)}
t = f^{-1}(x).
\end{equation}

where $f^{-1}$ is inverse function of $f$, if it exists.  Then by substituting Eqn. \eqref{eqn:pe-t=f^-1(x)} into Eqn. \eqref{eqn:pe-y=g(t)} we will produce a relation

\begin{equation}
\label{eqn:pe-y=y(x)}
y = g\left( f^{-1}(x) \right) \equiv y(x),
\end{equation}

showing $y$ as function of $x$ or $y = y(x)$.


## Parabolic motion
A particle can have a parabolic motion when it perfoms a [uniform linear motion](uniform-linear-motion) in $x$ direction 

\begin{equation}
\label{eqn:pe-pm-x}
x = x_0 + v_{0x}(t - t_0)
\end{equation}

and a [non-uniform linear motion](non-uniform-linear-motion) in $y$ direction,

\begin{equation}
\label{eqn:pe-pm-y}
y = y_0 + v_{0y}(t - t_0) - \frac12 g(t - t_0)^2,
\end{equation}

where gravitation acceleration $g$ is along $y$ direction, to negative. At $t = t_0$, Eqn. \eqref{eqn:pe-pm-x} will give $x = x_0$ and Eqn. \eqref{eqn:pe-pm-y} will give $y = y_0$. Substitution of Eqn. \eqref{eqn:pe-pm-x} to Eqn. \eqref{eqn:pe-pm-y} will produce

\begin{equation}
\label{eqn:pe-pm-y=y(x)}
y = y_0 + \left( \frac{x - x_0}{v_{0x}} \right) v_{0y} - \frac12 g \left( \frac{x - x_0}{v_{0x}} \right)^2,
\end{equation}

the relation between $y$ and $x$.


## Circular motion
In a circular motion a particle is moving along a circular path or a circle. One way to construct such motion is using an oscillation motion in $x$ and $y$ direction, e.g.

\begin{equation}
\label{eqn:pe-cm-x-cos-t}
x = R \cos \omega t + x_c
\end{equation}

and

\begin{equation}
\label{eqn:pe-cm-y-sin-t}
y = R \sin \omega t + y_c,
\end{equation}

where $r$ and $(x_c, y_c)$ are radius and center of the circle, respectively. There is also $\omega$, which is angular velocity. For this case it is not easy to follow the procedure in obtaining Egn. \eqref{eqn:pe-pm-y=y(x)} through invers function. Since we know the relation of

\begin{equation}
\label{eqn:pe-cm-cos2+sin2=1}
\cos^2 \beta +  \sin^2 \beta = 1,
\end{equation}

we can have

\begin{equation}
\label{eqn:pe-cm-x2+y2=R}
(x - x_c)^2 + (y - y_c)^2 = R^2,
\end{equation}

equation of a circle. Eqn. \eqref{eqn:pe-cm-x2+y2=R} is more convenient to use instead of

\begin{equation}
\label{eqn:pe-cm-y=y(x)}
 y = y_c \pm \sqrt{R^2 - (x - x_c)^2},
\end{equation}

which shows $y = y(x)$ explicitly.


## Motion with step function velocity
In this part $x$ and $y$ will be in $\rm m$ and $t$ in $\rm s$. These units will not be written in the function for simplicity.

A motion can have [step function velocity](step-function-velocity) in both $x$ and $y$ directions, e.g.

\begin{equation}
\label{eqn:pe-sfv-x-1}
x = \left\\{
\begin{array}{lc}
t + 1, & 0 \le t \le 4, \newline
2t - 3, & 4 \le t \le 5, \newline
\end{array}
\right.
\end{equation}

and

\begin{equation}
\label{eqn:pe-sfv-y-1}
y = \left\\{
\begin{array}{lc}
1, & 0 \le t \le 2, \newline
t - 1, & 2 \le t \le 4, \newline
3, & 4 \le t \le 5.
\end{array}
\right.
\end{equation}

Since there are three different time intervals, $0 \le t \le 2$, $2 \le t \le 4$, and $4 \le t \le 5$, we must find $y = x$ in those time intervals. Note that Eqn. \eqref{eqn:pe-sfv-x-1} can be also be written in three time intervals similar to time intervals in Eqn. \eqref{eqn:pe-sfv-y-1}. After change the time intervals we can have

\begin{equation}
\label{eqn:pe-sfv-y(x)-1}
y = \left\\{
\begin{array}{lc}
1, & 1 \le x \le 3, \newline
x - 2, & 3 \le x \le 5, \newline
3, & 5 \le x \le 7.
\end{array}
\right.
\end{equation}

Using Eqns. \eqref{eqn:pe-sfv-x-1} and \eqref{eqn:pe-sfv-y-1} following table can be obtained.

$t \ (\rm s)$ | $x \ (\rm m)$ | $y \ (\rm s)$
0 | 1 | 1
1 | 2 | 1
2 | 3 | 1
3 | 4 | 2
4 | 5 | 3
5 | 7 | 3

Confirmation of Eqn. \eqref{eqn:pe-sfv-y(x)-1} can be seen in the second and third columns of previous table.

Another motion, with [step function velocity](step-function-velocity) in both $x$ and $y$ directions, can have following functions

\begin{equation}
\label{eqn:pe-sfv-x-2}
x = \left\\{
\begin{array}{lc}
1 + t, & 0 \le t \le 2, \newline
3, & 2 \le t \le 4, \newline
7 - t, & 4 \le t \le 6, \newline
1, & 6 \le t \le 8
\end{array}
\right.
\end{equation}

and

\begin{equation}
\label{eqn:pe-sfv-y-2}
y = \left\\{
\begin{array}{lc}
1, & 0 \le t \le 2, \newline
t - 1, & 2 \le t \le 4, \newline
3, & 4 \le t \le 6, \newline
9 - t, & 6 \le t \le 8.
\end{array}
\right.
\end{equation}

For this type of motion it is not possible, as far as I know, to obtained simple form of $y = y(x)$. It is because in this type of motion we can not make a map from $x$ to $y$, where a map is a special function that corresponds exactly one value of $x$ to one value of $y$ [[4](#ref4)].


## Exercises
1. Eqn. \eqref{eqn:pe-pm-x} will give $x = x_0$ and Eqn. \eqref{eqn:pe-pm-y} will give $y = y_0$ when $t = t_0$. In the Eqn. \eqref{eqn:pe-pm-y=y(x)} we can not find $t$, can you still show that it still holds for $y = y_0$ when $x = x_0$? Show how you do that. Does Eqn. \eqref{eqn:pe-pm-y=y(x)} always hold for every $y$ and $x$ at time $t$? 
2. Derive Eqn. \eqref{eqn:pe-cm-x2+y2=R} using Eqns. \eqref{eqn:pe-cm-x-cos-t}, \eqref{eqn:pe-cm-y-sin-t}, and \eqref{eqn:pe-cm-cos2+sin2=1}.
3. How you can introduce $x_0$ and $y_0$ for $t = t_0$ in Eqns. \eqref{eqn:pe-cm-x-cos-t} and \eqref{eqn:pe-cm-y-sin-t}? Explain in brief.
4. Draw graph $x-t$ for Eqn. \eqref{eqn:pe-sfv-x-1}, $y-t$ for Eqn. \eqref{eqn:pe-sfv-y-1}, and $y-x$ for Eqn. \eqref{eqn:pe-sfv-y(x)-1}.
5. Draw the trajectory specified by Eqns. \eqref{eqn:pe-sfv-x-2} and \eqref{eqn:pe-sfv-y-2}.


## References
1. <a name="ref1"></a>Meltem Ucal, Erik Gregersen, Thinley Kalsang Bhutia, "Parametric equation", Encyclopædia Britannica, 14 Sep 2015, url <https://www.britannica.com/science/parametric-equation> [20200928].
2. <a name="ref2"></a>Eric W. Weisstein, "Parametric Equations", from MathWorld--A Wolfram Web Resource, url <https://mathworld.wolfram.com/ParametricEquations.html> [20200928].
3. <a name="ref3"></a>Wikipedia contributors, "Parametric equation", Wikipedia, The Free Encyclopedia, 16 Aug 2020, 19:10 UTC, <https://en.wikipedia.org/w/index.php?oldid=973351978> [20200928].
4. <a name="ref4"></a>Wikipedia contributors, "Map (mathematics)", Wikipedia, The Free Encyclopedia, 26 May 2020, 18:22 UTC, <https://en.wikipedia.org/w/index.php?oldid=959005370> [20200929].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-09-28-parametric-equation.md)
