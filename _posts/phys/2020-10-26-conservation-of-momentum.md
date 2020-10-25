---
layout: post
author: viridi
title: conservation of momentum
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: ["com"]
date: 2020-10-26 06:17:00 +07
permalink: /physics/conservation-of-momentum
---
Conservation of momentum [[1](#ref1)] is discussed in this post.

## Law
Law of conservation of linear momentum of two particles $1$ and $2$ is

\begin{equation}
\label{eqn:lcm-law-of-conservation-of-momentum}
m _{1i} \vec{v} _{1i} + m _{2i} \vec{v} _{2i} = m _{1f} \vec{v} _{1f} + m _{2f} \vec{v} _{2f},
\end{equation}

where $i$ and $f$ stand for initial dan final condition.


## Derivation
From [center of mass](center-of-mass) implication of 1st Newton's law of motion for system of particles will be in the form of

\begin{equation}
\label{eqn:lcm-dp/dt=F-com}
\frac{d\vec{P}}{dt} = 0,
\end{equation}

where

\begin{equation}
\label{eqn:lcm-total-momentum}
\vec{P} = \vec{p}_1 + \vec{p}_2,
\end{equation}

where Eqn. \eqref{eqn:lcm-dp/dt=F-com} can be rewritten in the form of

\begin{equation}
\label{eqn:lcm-dp/dt=F-com-without-dt}
d\vec{P} = 0
\end{equation}

and can be approximated later with

\begin{equation}
\label{eqn:lcm-dp/dt=F-com-without-dt-approx}
d\vec{P} \approx \Delta\vec{P}.
\end{equation}

Using

\begin{equation}
\label{eqn:lcm-dP}
\Delta\vec{P} = \vec{P}_f - \vec{P}_i
\end{equation}

and

\begin{equation}
\label{eqn:lcm-dP-1}
\Delta\vec{p}_1 = \vec{p} _{1f} - \vec{p} _{1i},
\end{equation}

which also holds for particle $2$, we can have that

\begin{equation}
\label{eqn:lcm-dP-dp}
\Delta\vec{P} = \Delta\vec{p}_1 + \Delta\vec{p}_2.
\end{equation}

Substitute Eqn. \eqref{eqn:lcm-dP-dp} into Eqn. \eqref{eqn:lcm-dp/dt=F-com-without-dt-approx} will give

\begin{equation}
\label{eqn:lcm-dP-dp = 0}
\Delta\vec{p}_1 + \Delta\vec{p}_2 = 0.
\end{equation}

Eqn. \eqref{eqn:lcm-dP-dp = 0} will lead us to Eqn. \eqref{eqn:lcm-law-of-conservation-of-momentum}.


## Exercises
1. Two particles with mass $1 \ {\rm kg}$ and $2 \ {\rm kg}$ move along $x$ direction with initial velocity $4 \ {\rm m/s}$ and $-2 \ {\rm m/s}$. If final velocity of the first particle is $-1 \ {\rm m/s}$ find final velocity of the second particle.
2. Prove that Eqn. \eqref{eqn:lcm-law-of-conservation-of-momentum} can be obtained from Eqn. \eqref{eqn:lcm-dP-dp = 0}.


## References
1. <a name="ref1"></a>Wikipedia contributors, "Conservation of momentum", Wikipedia, The Free Encyclopedia, 6 Sep 2020, 03:59 UTC, <https://en.wikipedia.org/w/index.php?oldid=976965573> [20201026].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-10-26-conservation-of-momentum.md)
