---
layout: post
author: viridi
title: spring-mass system on horizontal surface
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: ["statics"]
date: 2020-11-15 20:38:00 +07
permalink: /physics/shm-spring-mass-horiz
---
A special type of periodic motion is simple harmonic motion (SHM), where object displacement causes restoring force in opposite direction and always towards the equilibrium position of the object performing SHM [[1](#ref1)]. Pendulum and spring-mass systems are examples of periodic motion  [[2](#ref2)].


## Differential equation
A system performing SHM will have a differential equation in the form of [[3](#ref3)]

\begin{equation}
\label{eqn:shm-diff-eqn}
\frac{d^2 x}{dt^2} + \omega^2 x = 0,
\end{equation}

which give soulution of

\begin{equation}
\label{eqn:shm-diff-eqn-soulution}
x(t) = A \sin (\omega t + \varphi_0).
\end{equation}

From Eqn. \eqref{eqn:shm-diff-eqn-soulution} we can have

\begin{equation}
\label{eqn:shm-diff-eqn-soulution-ddt}
\frac{dx}{dt} = \omega A \cos (\omega t + \varphi_0).
\end{equation}

and

\begin{equation}
\label{eqn:shm-diff-eqn-soulution-d2dtd}
\frac{d^2x}{dt^2} = -\omega^2 A \sin (\omega t + \varphi_0).
\end{equation}

Substitute Eqns. \eqref{eqn:shm-diff-eqn-soulution} and \eqref{eqn:shm-diff-eqn-soulution-d2dtd} to Eqn. \eqref{eqn:shm-diff-eqn} will make left side of the equation zero as the right side.


## References
1. <a name="ref1"></a>Wikipedia contributors, "Simple harmonic motion", Wikipedia, The Free Encyclopedia, 19 Oct 2020, 03:17 UTC, url <https://en.wikipedia.org/w/index.php?oldid=984257153> [20201115].
2. <a name="ref2"></a>Carl R. Nave, "Periodic Motion", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/permot.html> [20201115].
3. <a name="ref3"></a>-, "Simple Harmonic Motion", BYJU'S The Learning App, url <https://byjus.com/jee/simple-harmonic-motion-shm/> [20201115].


+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-11-15-shm-spring-mass-horiz.md)
