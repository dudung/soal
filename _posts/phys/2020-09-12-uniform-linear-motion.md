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
In this article we only discuss [position](position), [velocity](velocity), and [time](time) as parameters of motion [[4](#ref4)], where the position includes initial and final position, displacement, distance, and path length.

Since an ULM is a one-dimensional motion we will use the symbol of $x$ for position, $v$ for velocity, and $t$ for time. It is also common to use the subscript $0$ for initial and $t$ for final position, e.g. $x_0$ and $x_t$. For clarity this subscript will also be used for time, i.e.  $t_0$ and $t$.


## Sign convention
Position and velocity are physical quantities of type [vector](vector), which means that they have value (magnitude) and direction (sign). There should be an origin in defining position where it is indicated as $x = 0$. Position to the left of origin will have negative sign or $-$ and position to the right of origin will have positive sign or $+$. Appearance of the first is mandatory, while the second is only when necessary. And for velocity, minus sign indicates that the object moves to the left, while plus sign indicates that the object moves to the right.

<oo>
svg 600 200 #fafafa fig:ulm-pos-velo|Objects with: (a) $x > 0$, $v > 0$, (b) $x > 0$, $v < 0$, (c) $x < 0$, $v > 0$, (d) $x < 0$, $v < 0$.

style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 20 20 260 60 40 40
style lc:#000 ls:0 lw:1 lo:1
arrow 20 40 260 40
style lc:#000 ls:0 lw:1 lo:1 fc:#000
circle 140 40 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 265 40 x
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 17 65 -3
text 57 65 -2
text 97 65 -1
text 137 65 0
text 177 65 1
text 217 65 2
text 132 90 (a)

style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 320 20 560 60 40 40
style lc:#000 ls:0 lw:1 lo:1
arrow 320 40 560 40
style lc:#000 ls:0 lw:1 lo:1 fc:#000
circle 440 40 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 565 40 x
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 317 65 -3
text 357 65 -2
text 397 65 -1
text 437 65 0
text 477 65 1
text 517 65 2
text 432 90 (c)

style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 20 120 260 160 40 40
style lc:#000 ls:0 lw:1 lo:1
arrow 20 140 260 140
style lc:#000 ls:0 lw:1 lo:1 fc:#000
circle 140 140 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 265 140 x
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 17 165 -3
text 57 165 -2
text 97 165 -1
text 137 165 0
text 177 165 1
text 217 165 2
text 132 190 (b)

style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 320 120 560 160 40 40
style lc:#000 ls:0 lw:1 lo:1
arrow 320 140 560 140
style lc:#000 ls:0 lw:1 lo:1 fc:#000
circle 440 140 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 565 140 x
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 317 165 -3
text 357 165 -2
text 397 165 -1
text 437 165 0
text 477 165 1
text 517 165 2
text 432 190 (d)
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

where subscripts $i$ and $f$ stand for initial and final. We will use it for better understanding.


## Exercises
1. Explain what is the relation between Eqns. \eqref{eqn:ulm-position} and \eqref{eqn:ulm-position-i-f}. Map each symbol in the first equation to the second.
2. A particle perform a ULM and is observed at time $t = t_1$, $t = t_2$, and $t = t_3$ and its positions are recorded as $x = x_1$, $x = x_2$, and $x = x_3$ for each time. Which equation from Eqns.  Eqns. \eqref{eqn:ulm-position} - \eqref{eqn:ulm-position-i-f} is better to describe the relation between $x_2$ and $x_1$ and $x_3$ and $x_2$? Explain in brief your answer.


## References
1. <a name="ref2"></a>-, "Uniform Linear Motion: Constant Velocity Motion along a Line", Phyley, 3 Feb 2019, url <https://www.phyley.com/uniform-linear-motion> [20200913].
2. <a name="ref2"></a>José L. Fernández, "Equations of Constant Velocity Motion", Fisicalab, url <https://www.fisicalab.com/en/section/urm-equations> [20200913].
3. <a name="ref3"></a>The Editors of Encyclopaedia Britannica, "Vector", Encyclopædia Britannica, 27 May 2020, url <https://www.britannica.com/science/linear-motion> [20200913].
4. <a name="ref4"></a>Carl R. Nave, "Description of Motion", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/mot.html> [20200913].
5. <a name="ref5"></a>David Lewis, "Answer to 'Why are speed, velocity, acceleration, distance, displacement, and time called the parameters of motion?", Quora, 21 Mar 2017, url <https://qr.ae/pNCRxz> [20200913].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-09-12-uniform-linear-motion.md)
