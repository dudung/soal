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
A type of equation that employs an independent variable (parameter) is parametric equation [[1](#ref1)]. It provides a convenient way to represent curves and surfaces [[2](#ref2)]. Equations of this type are commonly used in kinematics, where the trajectory of an object is represented by equations depending on time as the parameter [[3](#ref3)].


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


## Exercises
1. Eqn. \eqref{eqn:pe-pm-x} will give $x = x_0$ and Eqn. \eqref{eqn:pe-pm-y} will give $y = y_0$ when $t = t_0$. In the Eqn. \eqref{eqn:pe-pm-y=y(x)} we can not find $t$, can you still show that it still holds for $y = y_0$ when $x = x_0$? Show how you do that. Does Eqn. \eqref{eqn:pe-pm-y=y(x)} always hold for every $y$ and $x$ at time $t$? 


## References
1. <a name="ref1"></a>Meltem Ucal, Erik Gregersen, Thinley Kalsang Bhutia, "Parametric equation", Encyclopædia Britannica, 14 Sep 2015, url <https://www.britannica.com/science/parametric-equation> [20200928].
2. <a name="ref2"></a>Eric W. Weisstein, "Parametric Equations", from MathWorld--A Wolfram Web Resource, url <https://mathworld.wolfram.com/ParametricEquations.html> [20200928].
3. <a name="ref3"></a>Wikipedia contributors, "Parametric equation", Wikipedia, The Free Encyclopedia, 16 Aug 2020, 19:10 UTC, <https://en.wikipedia.org/w/index.php?oldid=973351978> [20200928].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-09-28-parametric-equation.md)
