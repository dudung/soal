---
layout: post
author: viridi
title: diagonal beam frictionless wall rough floor
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: ["statics"]
date: 2020-11-10 05:30:00 +07
permalink: /physics/statics-beam-diag-fless-wall-fric-floor
---
A uniform beam is diagonally positioned in such posture, so that left end of the beam is on a frictionless wall and the right end of the beam is on a floor with friction. The left end is at higher position in vertical direction compared to the right end. It is usually related to ladder [[1](#ref1)].


## Problem
An uniform beam is supported horizontally by two wires attached to ceiling, where each wire has different angle with horizontal direction as shown in following Fig. <a href="#fig:shbar-vwire2-0">1</a>. The beam is in a stable condition.

{:refdef: style="text-align: center;"}
![diagonal beam frictionless wall rough floor](/assets/img/phys/dbar-floor-wall-0.png)
<br />
Figure <a name="fig:shbar-vwire2-0">1</a> A beam supported horizontally by two vertical wires.
{: refdef}

Tension of left wire is marked as $T_1$, while tension of the other wire is marked as $T_2$. Length of the beam is $L$ and its mass is $m$. Point $O$ is position of center of the mass of the beam. Distance of point $B$ from point $O$ is $l_1$ and distance of point $D$ from point $O$ is $l_2$. If angle of the left wire with horizontal direction is $\theta_1$ and angle of the right wire with horizontal direction is $\theta_2$, find tension formulation of $T_1$ and $T_2$ as function of the other parameters.

{% comment %}

## Theory
The problem in Fig. <a href="#fig:shbar-vwire2-0">1</a> is part of statics, where we will use Newton's first law for linear motion

\begin{equation}
\label{eqn:shbar-sum-fx=0}
\sum F_x = 0
\end{equation}

in $x$ direction,

\begin{equation}
\label{eqn:shbar-sum-fy=0}
\sum F_y = 0
\end{equation}

in $y$ direction, and also for rotational motion

\begin{equation}
\label{eqn:shbar-sum-tau=0}
\sum \tau_P = 0
\end{equation}

at every point $P$, e.g. $A$, $B$, $C$, $D$, $E$, or $O$.


## Formulation
### Free-body diagram
From Fig. <a href="#fig:shbar-vwire2-0">1</a> we can draw the free-body diagram as shown in Fig. <a href="#fig:shbar-vwire2-1">2</a>, where the ceiling should not be drawn.

{:refdef: style="text-align: center;"}
![horizontal beam suspended by two vertical wires](/assets/img/phys/hbar-vwire2-1.png)
<br />
Figure <a name="fig:shbar-vwire2-1">2</a> Free-body digram of a beam supported horizontally by two vertical wires.
{: refdef}

Do not forget to draw the coordinate system, $x$ and $y$ axes, to support the description of the free-body diagram.

### Sum of forces in $x$ direction
From Fig. <a href="#fig:shbar-vwire2-1">2</a> we can see that there is any force or force component in $x$ direction. Then Eqn. \eqref{eqn:shbar-sum-fx=0} already holds.

### Sum of forces in $y$ direction
In $y$ direction, using Eqn. \eqref{eqn:shbar-sum-fy=0}, we can have that

\begin{equation}
\label{eqn:shbar-sum-fy=0-applied}
\begin{array}{rcl}
T_1 + T_2 - w & = & 0 \newline
T_1 + T_2 & = & w.
\end{array}
\end{equation}

### Sum of torques at point $O$
When point $O$ is chosen as center of rotation we consider only forces not at that point as shown in Fig. <a name="#fig:shbar-vwire2-2">3</a>, where clockwise direction has positive sign.

{:refdef: style="text-align: center;"}
![horizontal beam suspended by two vertical wires](/assets/img/phys/hbar-vwire2-2.png)
<br />
Figure <a name="fig:shbar-vwire2-2">3</a> Torques when point $O$ as center of rotation.
{: refdef}

Then we can have

\begin{equation}
\label{eqn:shbar-sum-tau=0-applied-O}
\begin{array}{rcl}
\sum \tau_O & = & 0 \newline
T_1 l_1 - T_2 l_2 & = & 0 \newline
T_1 l_1 & = & T_2 l_2 \newline
T_1 & = & \displaystyle \left( \frac{l_2}{l_1} \right) T_2,
\end{array}
\end{equation}

which shows the relation between $T_1$ and $T_2$.

### Sum of torques at point $B$
When point $B$ is chosen as center of rotation we consider only forces not at that point as shown in Fig. <a name="#fig:shbar-vwire2-3">4</a>, where clockwise direction has positive sign.

{:refdef: style="text-align: center;"}
![horizontal beam suspended by two vertical wires](/assets/img/phys/hbar-vwire2-3.png)
<br />
Figure <a name="fig:shbar-vwire2-3">4</a> Torques when point $B$ as center of rotation.
{: refdef}

Then we can have

\begin{equation}
\label{eqn:shbar-sum-tau=0-applied-B}
\begin{array}{rcl}
\sum \tau_B & = & 0 \newline
w l_1 - T_2 (l_1 + l_2) & = & 0 \newline
-T_2 (l_1 + l_2) & = & -w l_1 \newline
T_2 & = & \displaystyle \left( \frac{l_1}{l_1 + l_2} \right) w,
\end{array}
\end{equation}

that relates $T_2$ and $w$.

### Sum of torques at point $D$
When point $D$ is chosen as center of rotation we consider only forces not at that point as shown in Fig. <a name="#fig:shbar-vwire2-3">4</a>, where clockwise direction has positive sign.

{:refdef: style="text-align: center;"}
![horizontal beam suspended by two vertical wires](/assets/img/phys/hbar-vwire2-4.png)
<br />
Figure <a name="fig:shbar-vwire2-4">3</a> Torques when point $D$ as center of rotation.
{: refdef}

Then we can have

\begin{equation}
\label{eqn:shbar-sum-tau=0-applied-D}
\begin{array}{rcl}
\sum \tau_D & = & 0 \newline
T_1 (l_1 + l_2) - w l_2 & = & 0 \newline
T_1 (l_1 + l_2) & = & w l_2 \newline
T_1 & = & \displaystyle \left( \frac{l_2}{l_1 + l_2} \right) w,
\end{array}
\end{equation}

tat relates $T_1$ and $w$.


## Solution
### Using $\tau_O$
From Eqns. \eqref{eqn:shbar-sum-fy=0-applied} and \eqref{eqn:shbar-sum-tau=0-applied-O} we can have that

\begin{equation}
\label{eqn:shbar-sum-fy=0-applied-tau-O}
\begin{array}{rcl}
\displaystyle \left( \frac{l_2}{l_1} \right) T_2 + T_2 & = & w \newline
\displaystyle \left( \frac{l_2}{l_1} + 1 \right) T_2 & = & w \newline
\displaystyle \left( \frac{l_2 + l_1}{l_1} \right) T_2 & = & w \newline
T_2 & = & \displaystyle \left( \frac{l_1}{l_2 + l_1} \right) w.
\end{array}
\end{equation}

And substitute Eqn. \eqref{eqn:shbar-sum-fy=0-applied-tau-O} to Eqn. \eqref{eqn:shbar-sum-tau=0-applied-O}

\begin{equation}
\label{eqn:shbar-sum-tau=0-applied-O-T2}
\begin{array}{rcl}
T_1 & = & \displaystyle \left( \frac{l_2}{l_1} \right) \left( \frac{l_1}{l_2 + l_1} \right) w \newline
& = & \displaystyle \left( \frac{l_2}{l_2 + l_1} \right) w.
\end{array}
\end{equation}

It requires four steps to find Eqns. \eqref{eqn:shbar-sum-fy=0-applied-tau-O} and \eqref{eqn:shbar-sum-tau=0-applied-O-T2}.

### Using $\tau_B$
As shown previously in Eqn. \eqref{eqn:shbar-sum-tau=0-applied-B}, we can get directly Eqn. \eqref{eqn:shbar-sum-fy=0-applied-tau-O} only in one step.

### Using $\tau_D$
As shown previously in Eqn. \eqref{eqn:shbar-sum-tau=0-applied-D}, we can get directly Eqn. \eqref{eqn:shbar-sum-tau=0-applied-O-T2} only in one step.


## Note
### Applying numerical value
Using Eqns. \eqref{eqn:shbar-sum-fy=0-applied-tau-O} and \eqref{eqn:shbar-sum-tau=0-applied-O-T2} and values provided in the problem, $l_1 = 80 \ \rm cm$, $l_2 = 40 \ \rm cm$, $m = 15 \ \rm kg$, we can have

\begin{equation}
\label{eqn:shbar-value-T1}
\begin{array}{rcl}
T_1 & = & \displaystyle \left( \frac{l_2}{l_2 + l_1} \right) w \newline
& = & \displaystyle \left( \frac{0.4}{0.4 + 0.8} \right) (15 \cdot 10) \newline
& = & \displaystyle \left( \frac13 \right) 150 \newline
& = & 50 \ \rm N
\end{array}
\end{equation}

and

\begin{equation}
\label{eqn:shbar-value-T2}
\begin{array}{rcl}
T_2 & = & \displaystyle \left( \frac{l_1}{l_2 + l_1} \right) w \newline
& = & \displaystyle \left( \frac{0.8}{0.4 + 0.8} \right) (15 \cdot 10) \newline
& = & \displaystyle \left( \frac23 \right) 150 \newline
& = & 100 \ \rm N.
\end{array}
\end{equation}

Since the second vertical wire is nearer to beam center of mass $O$ compared to the first wire, then $T_2 > T_1$.

### More efficient way
There are two ways to get $T_1$ and $T_2$
+ four steps through Eqns. \eqref{eqn:shbar-sum-fy=0-applied}, \eqref{eqn:shbar-sum-tau=0-applied-O}, \eqref{eqn:shbar-sum-fy=0-applied-tau-O}, and \eqref{eqn:shbar-sum-tau=0-applied-O-T2}, or
+ two steps through Eqns. \eqref{eqn:shbar-sum-tau=0-applied-B} and \eqref{eqn:shbar-sum-tau=0-applied-D}.
You can determine which way is better compared to the other based on your own experience.

{% endcomment %}


## References
1. <a name="ref1"></a>William Moebs, Samuel J. Ling, Jeff Sanny, "Figure 12.14 A 5.0-m-long ladder rests against a frictionless wall.", in 12.2 Examples of Static Equilibrium, University Physics, vol. 1, OpenStax, 2016, url <https://opentextbc.ca/universityphysicsv1openstax/chapter/12-2-examples-of-static-equilibrium/> [20201111]..

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-11-10-statics-beam-diag-fless-wall-fric-floor.md)
