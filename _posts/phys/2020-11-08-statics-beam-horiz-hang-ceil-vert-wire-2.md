---
layout: post
author: viridi
title: horizontal beam suspended by two vertical wires
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: ["statics"]
date: 2020-11-08 19:49:00 +07
permalink: /physics/statics-beam-horiz-hang-ceil-vert-wire-2
---
A uniform beam is hung horizontally from ceiling through two vertical wires attached at some positions on the beam. It is a general case of a horizontal rod suspended by two vertical cables [[1](#ref1)].


## Problem
An uniform beam with mass $m$ and length $L$ is supported horizontally by two vertical wires attached to ceiling as show in following Fig. <a href="#fig:shbar-vwire2-0">1</a>.

{:refdef: style="text-align: center;"}
![horizontal beam suspended by two vertical wires](/assets/img/phys/hbar-vwire2-0.png)
<br />
Figure <a name="fig:shbar-vwire2-0">1</a> A beam supported horizontally by two vertical wires.
{: refdef}

Tension of left wire is marked as $T_1$, while tension of the other wire is marked as $T_2$. Length of the beam is $2 \ \rm m$ and its mass is $15 \ \rm kg$. Point $O$ is position of center of the mass of the beam. Distance of point $B$ from point $O$ or $l_1$ is $80 \ \rm cm$ and distance of point $D$ from point $O$ or $l_2$ is $40 \ \rm cm$. Find tension $T_1$ and $T_2$.


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


## Solution
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
T_1 & = & \displaystyle \left( \frac{l_2}{l_1} \right) T_2  \newline
\end{array}
\end{equation}

### Sum of torques at point $B$
When point $B$ is chosen as center of rotation we consider only forces not at that point as shown in Fig. <a name="#fig:shbar-vwire2-3">4</a>, where clockwise direction has positive sign.

{:refdef: style="text-align: center;"}
![horizontal beam suspended by two vertical wires](/assets/img/phys/hbar-vwire2-3.png)
<br />
Figure <a name="fig:shbar-vwire2-3">4</a> Torques when point $O$ as center of rotation.
{: refdef}

Then we can have

\begin{equation}
\label{eqn:shbar-sum-tau=0-applied-B}
\begin{array}{rcl}
\sum \tau_B & = & 0 \newline
\end{array}
\end{equation}

### Sum of torques at point $D$
When point $D$ is chosen as center of rotation we consider only forces not at that point as shown in Fig. <a name="#fig:shbar-vwire2-3">4</a>, where clockwise direction has positive sign.

{:refdef: style="text-align: center;"}
![horizontal beam suspended by two vertical wires](/assets/img/phys/hbar-vwire2-4.png)
<br />
Figure <a name="fig:shbar-vwire2-4">3</a> Torques when point $O$ as center of rotation.
{: refdef}

Then we can have

\begin{equation}
\label{eqn:shbar-sum-tau=0-applied-D}
\begin{array}{rcl}
\sum \tau_D & = & 0 \newline
\end{array}
\end{equation}


## References
1. <a name="ref1"></a>Richard Fitzpatrick, "Rods and cables", in Classical Mechanics: an introductory course, The University of Texas at Austin, 2 Feb 2006, url <http://farside.ph.utexas.edu/teaching/301/lectures/node128.html> [20201108].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-11-08-statics-beam-horiz-hang-ceil-vert-wire-2.md)
