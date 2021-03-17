---
layout: post
author: viridi
title: uniform linear motion
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: ["topics"]
date: 2020-09-12 21:20:00 +07
permalink: /physics/uniform-linear-motion
---
In uniform liniear motion (ULM) an object will move with constant velocty along a straight line [[1](#ref1)]. This constant velocty motion is also known as uniform rectilinear motion (URM) [[2](#ref1)]. This motion is part of linear motion, which is also called uniform motion or rectilinear motion, motion in one spatial dimension [[3](#ref3)]. There some physics concepts related to motion [[4](#ref4)].


## Parameters of motion
In this article we only discuss [position](position), [velocity](velocity), and [time](time) as parameters of motion [[5](#ref5)], where the position includes initial and final position, displacement, distance, and path length.

Since an ULM is a one-dimensional motion we will use the symbol of $x$ for position, $v$ for velocity, and $t$ for time. It is also common to use the subscript $0$ for initial and $t$ for final position, e.g. $x_0$ and $x_t$. For clarity this subscript will also be used for time, i.e.  $t_0$ and $t$.


## Sign convention
Position and velocity are physical quantities of type [vector](vector), which means that they have value (magnitude) and direction (sign). There should be an origin in defining position where it is indicated as $x = 0$. Position to the left of origin will have negative sign or $-$ and position to the right of origin will have positive sign or $+$. Appearance of the first is mandatory, while the second is only when necessary. And for velocity, minus sign indicates that the object moves to the left, while plus sign indicates that the object moves to the right.

<oo>
svg 600 200 #fafafa fig:ulm-pos-velo|Objects with: (a) $x > 0$, $v > 0$, (b) $x > 0$, $v < 0$, (c) $x < 0$, $v > 0$, (d) $x < 0$, $v < 0$.

style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 20 20 260 60 40 40
style lc:#000 ls:0 lw:1 lo:1 fc:#000
arrow 20 40 260 40
style lc:#000 ls:0 lw:1 lo:1 fc:#000
circle 140 40 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 265 40 x
text 225 10 v
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 17 65 -3
text 57 65 -2
text 97 65 -1
text 137 65 0
text 177 65 1
text 217 65 2
text 132 90 (a)
style lc:#080 ls:0 lw:1 lo:1 fc:#0c0
rect 170 20 20 20
style lc:#a00 ls:0 lw:2 lo:1 fc:#a00
arrow 180 10 220 10

style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 320 20 560 60 40 40
style lc:#000 ls:0 lw:1 lo:1 fc:#000
arrow 320 40 560 40
style lc:#000 ls:0 lw:1 lo:1 fc:#000
circle 440 40 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 565 40 x
text 365 10 v
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 317 65 -3
text 357 65 -2
text 397 65 -1
text 437 65 0
text 477 65 1
text 517 65 2
text 432 90 (c)
style lc:#080 ls:0 lw:1 lo:1 fc:#0c0
rect 310 20 20 20
style lc:#a00 ls:0 lw:2 lo:1 fc:#a00
arrow 320 10 360 10

style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 20 120 260 160 40 40
style lc:#000 ls:0 lw:1 lo:1 fc:#000
arrow 20 140 260 140
style lc:#000 ls:0 lw:1 lo:1 fc:#000
circle 140 140 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 265 140 x
text 165 110 v
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 17 165 -3
text 57 165 -2
text 97 165 -1
text 137 165 0
text 177 165 1
text 217 165 2
text 132 190 (b)
style lc:#080 ls:0 lw:1 lo:1 fc:#0c0
rect 210 120 20 20
style lc:#a00 ls:0 lw:2 lo:1 fc:#a00
arrow 220 110 180 110

style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 320 120 560 160 40 40
style lc:#000 ls:0 lw:1 lo:1 fc:#000
arrow 320 140 560 140
style lc:#000 ls:0 lw:1 lo:1 fc:#000
circle 440 140 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 565 140 x
text 305 110 v
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 317 165 -3
text 357 165 -2
text 397 165 -1
text 437 165 0
text 477 165 1
text 517 165 2
text 432 190 (d)
style lc:#080 ls:0 lw:1 lo:1 fc:#0c0
rect 350 120 20 20
style lc:#a00 ls:0 lw:2 lo:1 fc:#a00
arrow 360 110 320 110
</oo>

Objects with different position and velocity signs are shown in Fig. <a href="#fig:ulm-pos-velo">1</a>: (a) positive position and positive velocity, (b) positive position and negative velocity, (c) negative position and positive velocity, (d) negative position and negative velocity.


## Equations
Final position $x_t$ and its relation to initial position $x_0$, velocity $v$, initial time $t_0$, and time $t$ is given by

\begin{equation}
\label{eqn:ulm-position}
x_t = x_0 + v (t - t_0).
\end{equation}

In some books Eqn. \eqref{eqn:ulm-position} is written in the form of

\begin{equation}
\label{eqn:ulm-position-simpler}
x = x_0 + v t,
\end{equation}

which is simpler but with the same meaning. Notice that in Eqn. \eqref{eqn:ulm-position-simpler} it is assumed that $t_0 = 0$. More general form and clearer (advisable to use it) is

\begin{equation}
\label{eqn:ulm-position-i-f}
x_f = x_i + v (t_f - t_i),
\end{equation}

where subscripts $i$ and $f$ stand for initial and final. We will use it for better understanding. Let's use Eqn. \eqref{eqn:ulm-position-i-f} in solving problem in Fig. <a href="#fig:ulm-pos-velo-examp-1">2</a>.

<oo>
svg 600 100 #fafafa fig:ulm-pos-velo-examp-1|A particle performing uniform linear motion is observed at time $t_1$, $t_2$, $t_3$, and $t_4$.

style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 20 40 580 80 40 40
style lc:#000 ls:0 lw:1 lo:1 fc:#000
arrow 20 60 580 60
style lc:#000 ls:0 lw:1 lo:1 fc:#000
circle 220 60 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 585 60 x
text 105 30 v
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 17 85 -5
text 57 85 -4
text 97 85 -3
text 137 85 -2
text 177 85 -1
text 217 85 0
text 257 85 1
text 297 85 2
text 337 85 3
text 377 85 4
text 417 85 5
style lc:#080 ls:0 lw:1 lo:1 fc:#0c0
rect 50 40 20 20
rect 130 40 20 20
rect 290 40 20 20
rect 530 40 20 20
style lc:#a00 ls:0 lw:2 lo:1 fc:#a00
arrow 60 30 100 30
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 50 15 t
text 130 15 t
text 290 15 t
text 530 15 t
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 55 20 1
text 135 20 2
text 295 20 3
text 535 20 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 65 15 = 2 s
text 145 15 = 4 s
text 545 20 = 14 s
</oo>

Since the particle performing a ULM then its velocity must be constant or at all time $t_1$, $t_2$, $t_3$, and $t_4$ value of $v$ should remain the same. Can we calculate the velocity $v$ from Fig. <a href="#fig:ulm-pos-velo-examp-1">2</a>? The answer is yes since all information required in Eqn. \eqref{eqn:ulm-position-i-f} are already provided in the figure. From the figure we can have $x_1 = -4 \ \rm m$ at $t_1 = 2 \ \rm s$ and $x_2 = -2 \ \rm m$ at $t_2 = 4 \ \rm s$. Notice that the initial time is not necessary zero. Using Eqn. \eqref{eqn:ulm-position-i-f} following relation can be obtained

\begin{equation}
\label{eqn:ulm-position-i-f-velo}
v = \frac{x_f - x_i}{t_f - t_i} = \frac{x_2 - x_1}{t_2 - t_1},
\end{equation}

since intial $i = 1$ and final $f = 2$ in this case. Using provide information we can have

\begin{equation}
\nonumber
v = \frac{(-2 ) \ {\rm m} - (-4)\ {\rm m}}{4 \ {\rm s} - 2 \ {\rm s}} = \frac{(-2 + 4) \ {\rm m}}{2 \ {\rm s}} = \frac22 \ {\rm m/s} = 1 \ {\rm m/s}.
\end{equation}

Using similiar way value of $t_3$ and $x_4$ can be found.


## Graphs
In ULM we can draw at least two graphs. The first is $x - t$ graph and the second is $v - t$ graph. Beside those graphs, a $x - v$ graph can be also created. We use term graph instead of chart since graph is  more related to mathematical function [[6](#ref6)] we try to illustrate.

Suppose that a particle moves with constant velocity

\begin{equation}
\label{eqn:ulm-v-t}
v(t) = v_0, \ \ \ t \ge 0,
\end{equation}

performing a ULM. Its $v-t$ chart is simply as shown in Figs. <a href="#fig:ulm-pos-velo-graph-v-t-v0>0">3</a> and <a href="#fig:ulm-pos-velo-graph-v-t-v0<0">4</a>.

<oo>
svg 480 210 #fafafa fig:ulm-pos-velo-graph-v-t-v0>0|Velocity $v$ as function of time $t$: $v(t) = v_0$, with $v_0 > 0$.

style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 20 20 460 180 40 40
style lc:#000 ls:0 lw:1 lo:1 fc:#000
arrow 20 180 460 180
arrow 20 180 20 20
style lc:#000 ls:0 lw:1 lo:1 fc:#000
circle 20 180 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 465 185 t
text 15 15 v
text 3 60 v
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 5 185 0
text 17 200 0
text 57 200 1
text 97 200 2
text 137 200 3
text 177 200 4
text 217 200 5
text 257 200 6
text 297 200 7
text 337 200 8
text 377 200 9
text 412 200 10
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 10 65 0
style lw:2.5 lc:#f00 fo:1
line 20 60 420 60
</oo>

<oo>
svg 480 210 #fafafa fig:ulm-pos-velo-graph-v-t-v0<0|Velocity $v$ as function of time $t$: $v(t) = v_0$, with $v_0 < 0$.

style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 20 20 460 180 40 40
style lc:#000 ls:0 lw:1 lo:1 fc:#000
arrow 20 60 460 60
arrow 20 180 20 20
style lc:#000 ls:0 lw:1 lo:1 fc:#000
circle 20 60 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 465 65 t
text 15 15 v
text 3 140 v
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 5 65 0
text 25 80 0
text 57 80 1
text 97 80 2
text 137 80 3
text 177 80 4
text 217 80 5
text 257 80 6
text 297 80 7
text 337 80 8
text 377 80 9
text 412 80 10
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 10 145 0
style lw:2.5 lc:#f00 fo:1
line 20 140 420 140
</oo>

In both previous figures the curve is simply horizontal line, the first is above $x$-axis for $v_0 > 0$ and the second is below $x$-axis for $v_0 < 0$. And how about $v_0 = 0$? Can you make the graph?

Next step is to discuss $x-t$ graph related to Eqn. \eqref{eqn:ulm-v-t}. For position, the equation is

\begin{equation}
\label{eqn:ulm-x-t}
x(t) = x_0 + v_0 (t - t_0), \ \ \ t \ge t_0,
\end{equation}

where position at $t = t_0$ is $x(t_0) = x_0$. Thera are four variatons of $x-t$ graphs for Eqn. \eqref{eqn:ulm-x-t}, which are: (i) $x_0 > 0$, $v_0 > 0$, (ii) $x_0 > 0$, $v_0 < 0$, (iii) $x_0 < 0$, $v_0 > 0$, and (iv) $x_0 < 0$, $v_0 < 0$. For simplification, let's choose $t_0 = 0$.

<oo>
svg 600 380 #fafafa fig:ulm-pos-velo-graph-x-t|Position $x$ as function of time $t$ for different sign of $x_0$ and $v_0$: (a) $x_0 > 0$, $v_0 > 0$, (b) $x_0 < 0$, $v_0 > 0$, (c) $x_0 > 0$, $v_0 < 0$, and (d) $x_0 < 0$, $v_0 < 0$.

style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 10 20 280 140 30 30
style lc:#000 ls:0 lw:1 lo:1 fc:#000
arrow 100 140 100 20
arrow 10 80 280 80
style lc:#000 ls:0 lw:1 lo:1 fc:#000
circle 100 80 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 285 85 t
text 97 15 x
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 135 165 (a)
style lc:#f00 ls:0 lw:1 lo:1 fc:#f00
circle 100 50 2
style lc:#f00 ls:0 lw:1 lo:1 fc:#f00
line 100 50 280 20
style lc:#f00 ls:6-3 lw:1 lo:1 fc:#f00
line 100 50 10 65
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 83 41 x
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 90 46 0

style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 310 20 580 140 30 30
style lc:#000 ls:0 lw:1 lo:1 fc:#000
arrow 400 140 400 20
arrow 310 80 580 80
style lc:#000 ls:0 lw:1 lo:1 fc:#000
circle 400 80 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 585 85 t
text 397 15 x
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 435 165 (b)
style lc:#f00 ls:0 lw:1 lo:1 fc:#f00
circle 400 110 2
style lc:#f00 ls:0 lw:1 lo:1 fc:#f00
line 400 110 580 80
style lc:#f00 ls:6-3 lw:1 lo:1 fc:#f00
line 400 110 310 125
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 383 101 x
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 390 106 0

style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 10 220 280 340 30 30
style lc:#000 ls:0 lw:1 lo:1 fc:#000
arrow 100 340 100 220
arrow 10 280 280 280
style lc:#000 ls:0 lw:1 lo:1 fc:#000
circle 100 280 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 285 285 t
text 97 215 x
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 135 365 (c)
style lc:#f00 ls:0 lw:1 lo:1 fc:#f00
circle 100 250 2
line 100 250 280 280
style lc:#f00 ls:6-3 lw:1 lo:1 fc:#f00
line 100 250 10 235
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 83 241 x
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 90 246 0

style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 310 220 580 340 30 30
style lc:#000 ls:0 lw:1 lo:1 fc:#000
arrow 400 340 400 220
arrow 310 280 580 280
style lc:#000 ls:0 lw:1 lo:1 fc:#000
circle 400 280 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 585 285 t
text 397 215 x
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 435 365 (e)
style lc:#f00 ls:0 lw:1 lo:1 fc:#f00
circle 400 310 2
line 400 310 580 340
style lc:#f00 ls:6-3 lw:1 lo:1 fc:#f00
line 400 310 310 295
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 383 301 x
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 390 306 0

style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 312 170 x
text 312 195 t
text 265 182 v

style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 300 170 &Delta;
text 296 175 ___
text 300 195 &Delta;
text 280 182 =
</oo>

If $x_0 > 0$ the line crossess vertical axis above horizontal axis and if $x_0 < 0$ it crossess vertical axis below horizontal axis as shown in Fig. <a href="fig:ulm-pos-velo-graph-x-t">5</a>. Value of $v_0$ determines gradient of the line, then $v_0 > 0$ will produce line to up right direction, while $v_0 < 0$ will produce line to down right direction. Dashed line show the function for $t < t_0$, where in this this example $t_0 \ge 0$.


## Exercises
1. Explain what is the relation between Eqns. \eqref{eqn:ulm-position} and \eqref{eqn:ulm-position-i-f}. Map each symbol in the first equation to the second.
2. A particle perform a ULM and is observed at time $t = t_1$, $t = t_2$, and $t = t_3$ and its positions are recorded as $x = x_1$, $x = x_2$, and $x = x_3$ for each time. Which equation from Eqns.  Eqns. \eqref{eqn:ulm-position} - \eqref{eqn:ulm-position-i-f} is better to describe the relation between $x_2$ and $x_1$ and $x_3$ and $x_2$? Explain in brief your answer.
3. Set value of velocities in Fig. <a href="#fig:ulm-pos-velo">1</a> (a) - (d) of your choice and explain why you choose such value.
4. Calculate value of $t_3$ from Fig. <a href="#fig:ulm-pos-velo-examp-1">2</a>. Which equation you use?
5. Calculate value of $x_4$ also from Fig. <a href="#fig:ulm-pos-velo-examp-1">2</a>. Explain which equation you use. Confirm the result from the figure by filling the missing axis tick marks.
6. Using Figs. <a href="#fig:ulm-pos-velo-graph-v-t-v0>0">3</a> and <a href="#fig:ulm-pos-velo-graph-v-t-v0<0">4</a>, make a graph of $v(t) = v_0$ for $v_0 = 0$. 
7. Write equation for $x(t)$ for all graphs in Fig. <a href="fig:ulm-pos-velo-graph-x-t">5</a> by assuming that horizontal tick is equal to $1 \ \rm s$ and vertical tick is equal to $1 \ \rm m$. Use fraction notation instead of decimal for simpler expression.
8. If position particle every time $t$ is given by $x(t) = (1 + 2t) \ \rm m$, draw graph showing particle position for $t = 0, 1, 4, 8 \ \rm s$.
9. Find the equation in Fig. <a href="fig:ulm-pos-velo-graph-x-t">5</a> and explain its relation to Eqn. \eqref{eqn:ulm-x-t} or Eqn. \eqref{eqn:ulm-position-i-f-velo}.


## References
1. <a name="ref2"></a>-, "Uniform Linear Motion: Constant Velocity Motion along a Line", Phyley, 3 Feb 2019, url <https://www.phyley.com/uniform-linear-motion> [20200913].
2. <a name="ref2"></a>José L. Fernández, "Equations of Constant Velocity Motion", Fisicalab, url <https://www.fisicalab.com/en/section/urm-equations> [20200913].
3. <a name="ref3"></a>The Editors of Encyclopaedia Britannica, "Vector", Encyclopædia Britannica, 27 May 2020, url <https://www.britannica.com/science/linear-motion> [20200913].
4. <a name="ref4"></a>Carl R. Nave, "Description of Motion", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/mot.html> [20200913].
5. <a name="ref5"></a>David Lewis, "Answer to 'Why are speed, velocity, acceleration, distance, displacement, and time called the parameters of motion?", Quora, 21 Mar 2017, url <https://qr.ae/pNCRxz> [20200913].
6. <a name="ref6"></a>Guffa, "Answer to 'What's the difference between a graph, a chart, and a plot?'", English Stack Exchange, 23 Sep 2011, url <https://english.stackexchange.com/a/43029> [20200913].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-09-12-uniform-linear-motion.md)
