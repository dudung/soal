---
layout: post
author: viridi
title: work-energy theorem
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: ["tutorial"]
date: 2020-10-13 04:46:00 +07
permalink: /physics/work-energy-theorem
---
Here we will discuss about work-kinetic energy theorem [[1](#ref1)] and how it helps to solve a problem in easier way compared to the use of dynamics and work concepts together.


## Kinetic energy
A particle with mass $m$ and moving with velocity $\vec{v}$ will have kinetic energy in the form of

\begin{equation}
\label{eqn:wket-kinetic-energy}
K = \frac12 m (\vec{v} \cdot \vec{v}) = \frac12 m v^2.
\end{equation}

The last term in Eqn. \eqref{eqn:wket-kinetic-energy} is more common then its preceeding term, which is showing the application of [two vectors dot product](vector#dot-product). Kinetic energy has the unit of $\rm J$ or joule.


## Work
In general work done by an object applyingg force $\vec{F}$ that can be varied with small displacement $d\vec{s}$ is

\begin{equation}
\label{eqn:wket-work-integral}
W = \int \vec{F} \cdot d\vec{s},
\end{equation}

which is presented in form of force-displacement path integral using calculus [[2](#ref2)]. Eqn. \eqref{eqn:wket-work-integral} seems complicated and not practical since it is a general form, where $\vec{F} = \vec{F}(\vec{s})$. We will discuss some special cases of it.

### Force with constant magnitude
If we deal with a force with constant magnitude or $\vec{F} \ne \vec{F}(\vec{s})$ then Eqn. \eqref{eqn:wket-work-integral} will be simplified into

\begin{equation}
\label{eqn:wket-work-integral-force-constant-magnitude
}
W = \vec{F} \cdot\int d\vec{s} = \vec{F} \cdot \vec{s}.
\end{equation}

The vector $\vec{F}$ can be moved outside of integral since it is not function of $\vec{s}$. We still have dot operation in Eqn. \eqref{eqn:wket-work-integral-force-constant-magnitude
} since the force can still have variation in its direction even its magnitude is constant or $\|\vec{F}\| = F_0$, where $F_0$ is a constant value.


## Excersices
1. Find the kinetic energy of an object with mass $0.5 \ \rm kg$ and moving with velocity $2 \ \rm m/s$.
2. A particle is moving with velocty $\vec{v} = (12 \hat{i} + 3 \hat{j} + 4 \hat{j}) \ \rm m/s$. If it has mass of 2 kg, calculate its kinetic energy.


## References
1. <a name="ref1"></a>-, "Work-Energy Theorem", in Boundless Physics, Lumen Learning, url <https://courses.lumenlearning.com/boundless-physics/chapter/work-energy-theorem/> [20201013].
2. <a name="ref2"></a>Glenn Elert, "Work", The Physics Hypertextbook, 2020, url <https://physics.info/work/> [20201013].
 
+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/tutorial/2020-10-13-work-energy-theorem.md)
