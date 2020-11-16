---
layout: post
author: viridi
title: spring-mass system on horizontal surface
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["statics"]
date: 2020-11-15 20:38:00 +07
permalink: /physics/shm-spring-mass-horiz
---
A system consisted of a mass and a spring (also a wall) on a horizontal frictionless surface [[1](#ref1)] is an example of a simple harmonic motion, where systems of a spring-mass attached on ceiling and a simple pendulum are more common to discussed [[2](#ref2)].


## System
A mass $m$ connected to a spring with spring constant $k$ is moving on a frictionless ($\mu = 0$), horizontal surface. Another end of the massless spring is attached on a wall. The system is shown in Fig. <a href="#fig:shm-sms-hfless">1</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/shm-spring-mass-horiz-fless-0.png)
<br />
Figure <a name="fig:fig:shm-sms-hfless">1</a> Spring-mass system of a frictionless horizontal surface.
{: refdef}

Spring force works on the mass $m$ is

\begin{equation}
\label{eqn:shm-sms-hfless-system}
F = -k(x - x_0),
\end{equation}

where $x = x_0$ is the equilibrium position. At that position the spring $k$ is in a relax condition (not compressed nor stretched) and does not give any force to the mass $m$. Fig. <a href="#fig:shm-sms-hfless-oscillation">2</a> shows the relation between displacement $x - x_0$, spring force $F$, and velocity $v$ as the mass $m$ moving forward and backward.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/shm-spring-mass-horiz-fless-1.png)
<br />
Figure <a name="fig:fig:shm-sms-hfless-oscillation">2</a> Snapshot of spring-mass system in one oscillation period.
{: refdef}

A red dashed line is a rough curve illustrating the dynamics of object position at several times, which are not so accurate. We can choose $x_0 = 0$ and copy the red dashed line from Fig. Fig. <a href="#fig:shm-sms-hfless-oscillation">2</a> to make a complete cycle of an oscillation as shown in Fig. <a href="#fig:shm-sms-hfless-cycle">3</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/shm-spring-mass-horiz-fless-2.png)
<br />
Figure <a name="fig:fig:shm-sms-hfless-oscillation">3</a> Position of the mass of spring-mass system.
{: refdef}

The lower part of Fig. <a href="#fig:shm-sms-hfless-cycle">3</a> should be a sinusoidal function with $T$ is oscillation periode and $A$ is amplitude of the oscillation.


## Formulation
Since the net force works on the mass $m$ is the spring force given in Eqn. \eqref{eqn:shm-sms-hfless-system}, we will have

\begin{equation}
\label{eqn:shm-sms-hfless-system-formulation}
\begin{array}{rcl}
\sum F & = & ma \newline
-kx & = & ma \newline
0 & = & ma + kx \newline
ma + kx & = & 0 \newline
\displaystyle a + \frac{k}{m} x & = & 0 \newline
\displaystyle \frac{d^2x}{dt^2} + \omega^2 x & = & 0 \newline
\end{array}
\end{equation}

using Newton's 2nd law of motion. Notice that we set $x_0 = 0$ in Eqn. \eqref{eqn:shm-sms-hfless-system-formulation} as in Fig. <a href="#fig:shm-sms-hfless-cycle">3</a> and we define that

\begin{equation}
\label{eqn:shm-sms-hfless-system-formulation-omega}
\omega = \sqrt{\frac{k}{m}}.
\end{equation}

Eqn. \eqref{eqn:shm-sms-hfless-system-formulation} is a differential equation of a [simple harmonic motion](simple-harmonic-motion), where the solution is

\begin{equation}
\label{eqn:shm-sms-diff-eqn-soulution}
x(t) = A \sin (\omega t + \varphi_0),
\end{equation}

with $\varphi_0$ is initial phase of the oscillation. Its unit is $\rm rad$.


## Some relations
Related to the solution given by Eqn. \eqref{eqn:shm-sms-diff-eqn-soulution} there are some relations that are already common

\begin{equation}
\label{eqn:shm-sms-diff-eqn-soulution-rel-0}
\omega = 2\pi f,
\end{equation}

\begin{equation}
\label{eqn:shm-sms-diff-eqn-soulution-rel-1}
T = \frac{1}{f},
\end{equation}

\begin{equation}
\label{eqn:shm-sms-diff-eqn-soulution-rel-2}
x_\max = A,
\end{equation}

\begin{equation}
\label{eqn:shm-sms-diff-eqn-soulution-rel-3}
v_\max = \omega A,
\end{equation}

\begin{equation}
\label{eqn:shm-sms-diff-eqn-soulution-rel-4}
a_\max = \omega^2 A,
\end{equation}

where $\omega$ is angular frequency and $f$ is frequency. Their unit are $\rm rad/s$ and $\rm Hz$, respectively. Unit of $A$ and $x$ are length unit, eq. $\rm m$, $\rm cm$, or $\rm mm$.


## Exercises
1. <a name="prob1"></a>A $100 \ \rm g$-mass is attached on an ideal spring (linear, massless) with spring constant $4000 \pi^2 \ \rm N/m$ and moving on a frictionless horizontal surface. Find oscillation angular frequency, frequency, and period of the system.
{% comment %} Answer: $\omega = 200\pi \ \rm rad/s$, $f = 200 \ \rm Hz$, $T = 0.01 \ \rm s$. {% endcomment %}
2. 


## References
1. <a name="ref1"></a>Sydney Redner, "Mass on a Horizontal Spring", PY211 Lecture Notes, Boston University, Spring 2006, url <http://physics.bu.edu/~redner/211-sp06/class-oscillations/spring_mass.html> [20201116].
2. <a name="ref2"></a>Wikipedia contributors, "Simple harmonic motion", Wikipedia, The Free Encyclopedia, 19 Oct 2020, 03:17 UTC, url <https://en.wikipedia.org/w/index.php?oldid=984257153> [20201115].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-11-15-shm-spring-mass-horiz.md)


{% comment %}
Fig. <a href="#fig:x">1</a.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/x.png)
<br />
Figure <a name="fig:x">1</a> ...
{: refdef}
{% endcomment %}
