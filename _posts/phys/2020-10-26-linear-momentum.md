---
layout: post
author: viridi
title: linear momentum
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: [""]
date: 2020-10-26 02:14:00 +07
permalink: /physics/linear-momentum
---
Momentum [[1](#ref1)], or more specific linear momentum [[2](#ref2)], will be discussed here.


## Definition
Momentum is defined as product of mass $m$ and velocity $\vec{v}$ as follow

\begin{equation}
\label{eqn:linmom-def}
\vec{p} = m \vec{v},
\end{equation}

which produces a vector quantity with unit of $\rm kg \cdot m \cdot s^{-1}$ in SI unit (the International System of Units) [[3](#ref3)]. Since we are not dealing with negative mass [[4](#ref4)], particle momentum is a vector that has the same direction with particle velocity since it is a product of a positive scalar (mass) with a vector (velocity) as given in Eqn. \eqref{eqn:linmom-def}.


## Relation to net force
Remember net force in Newton's 2nd law of linear motion

\begin{equation}
\label{eqn:linmom-newton-2nd-law}
\sum \vec{F} = m \vec{a}.
\end{equation}

Suppose that $\vec{F}$, an external force (do not confuse with $\sum \vec{F}$), is the only force acted upon the particle, which makes it the net force. Then, Eqn. \eqref{eqn:linmom-newton-2nd-law} will be turned into

\begin{equation}
\label{eqn:linmom-newton-2nd-law-F}
\vec{F} = m \vec{a}.
\end{equation}

Differentiate both side of Eqn. \eqref{eqn:linmom-def} once with respect to time $t$ and we will have

\begin{equation}
\label{eqn:linmom-dp/dt}
\frac{d\vec{p}}{dt} = \frac{d(m \vec{v})}{dt}.
\end{equation}

With product rule or Leibniz rule [[5](#ref5)], Eqn. \eqref{eqn:linmom-dp/dt} will be

\begin{equation}
\label{eqn:linmom-total-differential-mv}
\frac{d(m \vec{v})}{dt} = \left(\frac{dm}{dt}\right)\vec{v} + m\left(\frac{d\vec{v}}{dt}\right).
\end{equation}

If we limit our discussion to constant mass $m$ or $dm/dt = 0$ then Eqn. \eqref{eqn:linmom-total-differential-mv} will be change into

\begin{equation}
\label{eqn:linmom-dp/dt=ma}
\frac{d\vec{p}}{dt} = m\left(\frac{d\vec{v}}{dt}\right) = m \vec{a},
\end{equation}

with kinematics relation between acceleration and velocity, $\vec{a} = d\vec{v}/dt$. Using Eqns. \eqref{eqn:linmom-newton-2nd-law-F} and \eqref{eqn:linmom-dp/dt=ma} we will have

\begin{equation}
\label{eqn:linmom-dp/dt=F}
\frac{d\vec{p}}{dt} = \vec{F},
\end{equation}

which is the relation between momentum $\vec{p}$ and net force $\vec{F}$ of a particle.


## Two particle system
Eqn. \eqref{eqn:linmom-dp/dt=F} hold also for system of particles, where we will take only system consisted of two particles as the example. Now, mass $m$ is total mass of the system

\begin{equation}
\label{eqn:linmom-total-mass}
M = m_1 + m_2
\end{equation}

and momentum of the system

\begin{equation}
\label{eqn:linmom-total-momentum}
\vec{P} = \vec{p}_1 + \vec{p}_2,
\end{equation}

with

\begin{equation}
\label{eqn:linmom-momentum-i}
\vec{p}_i = m_i \vec{v}_i
\end{equation}

with $i = 1, 2$, for each particle. We can define center of mass velocity of the system $\vec{V}_{\rm com}$, which makes

\begin{equation}
\label{eqn:linmom-total-momentum-mcom}
\vec{P} = M \vec{V}_{\rm com}.
\end{equation}

Substitute Eqn. \eqref{eqn:linmom-total-mass} to the right side of Eqn. \eqref{eqn:linmom-total-momentum-mcom} and Eqn. \eqref{eqn:linmom-total-momentum} to the left side, we will have

\begin{equation}
\label{eqn:linmom-vcom-derivation}
\begin{array}{rcl}
\vec{p}_1 + \vec{p}_2 & = & (m_1 + m_2) \ \vec{V} _{\rm com} \newline
m_1 \vec{v}_1 + m_2 \vec{v}_2 & = & (m_1 + m_2) \ \vec{V} _{\rm com} \newline
\displaystyle \frac{m_1 \vec{v}_1 + m_2 \vec{v}_2}{m_1 + m_2} & = & \ \vec{V} _{\rm com},
\end{array}
\end{equation}

which defines the $\vec{V}_{\rm com}$.


## COM parameters of motion
As in [kinematics](kinematics), in COM reference of frame there will be also position and acceleration. For $N$ particles, the position, velocity, and acceleration are Eqn. \eqref{eqn:linmom-vcom-derivation}.

\begin{equation}
\label{eqn:linmom-Rcom}
\vec{R} _{\rm com} = \frac{\sum _{i = 1} ^N m_i \vec{r}_i}{\sum _{i = 1} ^N m_i},
\end{equation}

\begin{equation}
\label{eqn:linmom-Vcom}
\vec{V} _{\rm com} = \frac{\sum _{i = 1} ^N m_i \vec{v}_i}{\sum _{i = 1} ^N m_i},
\end{equation}

\begin{equation}
\label{eqn:linmom-Acom}
\vec{A} _{\rm com} = \frac{\sum _{i = 1} ^N m_i \vec{a}_i}{\sum _{i = 1} ^N m_i}.
\end{equation}

Eqns. \eqref{eqn:linmom-Rcom}, \eqref{eqn:linmom-Vcom}, and \eqref{eqn:linmom-Acom} will also have similar relations

\begin{equation}
\label{eqn:linmom-Vcom-Rcom}
\vec{V} _{\rm com} = \frac{d\vec{R} _{\rm com}}{dt}
\end{equation}

and

\begin{equation}
\label{eqn:linmom-Acom-Vcom}
\vec{A} _{\rm com} = \frac{d\vec{V} _{\rm com}}{dt}.
\end{equation}

Eqns. \eqref{eqn:linmom-Vcom-Rcom} and \eqref{eqn:linmom-Acom-Vcom} can be proven using relation for each particle $i$ through $\vec{v}_i = d\vec{r}_i/dt$ and $\vec{a}_i = d\vec{v}_i/dt$ and Eqns. \eqref{eqn:linmom-Rcom}, \eqref{eqn:linmom-Vcom}, \eqref{eqn:linmom-Acom}.


## Exercises
1. A $100 \ \rm g$-particle moves with velocity $1 \ \rm dm/s$ to $+x$ direction. Find its momentum and present it SI unit and vector. Remember that $1 \ {\rm kg} = 1000 \ {\rm g}$, $1 \ {\rm dm} = 0.1 \ {\rm m}$, and unit vector for $+x$ direction can be $\hat{i}$, $\hat{x}$, or $\hat{e}_x$.
2. Net fore on a particle is $\vec{F} = [(2t - 1) \hat{i} + t^2 \hat{j} + \hat{k}] \ {\rm N}$. Find its momentum and velocity at $t = 5 \ {\rm s}$, if mass of the particle is $0.1 \ {\rm kg}$.
3. Find expression for $\vec{R} _{\rm com}$ and $\vec{A} _{\rm com}$ for system of two particles as in Eqn. \eqref{eqn:linmom-vcom-derivation}.
4. There are three particles with mass $1 \ {\rm kg}$, $2 \ {\rm kg}$, and $3 \ {\rm kg}$, where their position are given by $\vec{r}_1 = [ t^3 \hat{i} + t^2 \hat{j} + t \hat{k} ] \ {\rm m}$, $\vec{r}_2 = [ (t^2 - 1) \hat{i} + (1 - 3t) \hat{j} - 10 \hat{k} ] \ {\rm m}$, and $\vec{r}_3 = [ t \hat{i} + (10 - t^2) \hat{k} ] \ {\rm m}$. Find position, velocity, and acceleration of system center of mass $\vec{R} _{\rm com}$, $\vec{V} _{\rm com}$, and $\vec{A} _{\rm com}$.
5. With the information for each particle $i$ that $\vec{v}_i = d\vec{r}_i/dt$ and $\vec{a}_i = d\vec{v}_i/dt$, proove Eqns. \eqref{eqn:linmom-Vcom-Rcom} and \eqref{eqn:linmom-Acom-Vcom}.


## References
1. <a name="ref1"></a>Carl R. Nave, "Momentum", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/mom.html> [20201026].
2. <a name="ref2"></a>Wikipedia contributors, "Momentum", Wikipedia, The Free Encyclopedia, 19 Oct 2020, 05:55 UTC, <https://en.wikipedia.org/w/index.php?oldid=984273085> [20201026].
3. <a name="ref3"></a>TheSI@nist.gov, "SI Units", National Institute of Standards and Technology, U.S. Department of Commerce, Gaithersburg, 15 Nov 2019, url <https://www.nist.gov/pml/weights-and-measures/metric-si/si-units> [20201026].
4. <a name="ref4"></a>Eric Sorensen, "Physicists create 'negative mass'", Phys.Org, 17 Apr 2017, url <https://phys.org/news/2017-04-physicists-negative-mass.html> [20201026].
5. <a name="ref5"></a>Wikipedia, "Produktregel", Die freie Enzyklopädie, 7 Dec 2019, 21:32 UTC, url <https://de.wikipedia.org/w/index.php?oldid=194721034> [20201026].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-10-26-linear-momentum.md)
