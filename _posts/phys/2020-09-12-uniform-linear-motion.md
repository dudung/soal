---
layout: post
author: viridi
title: uniform liniear motion
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
grid 20 20 220 180 40 40

style lc:#000 ls:0 lw:1 lo:1
arrow 20 180 220 180
arrow 20 180 20 20

style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 225 185 x
text 20 12 y

style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 15 197 0
text 55 197 1
text 95 197 2
text 135 197 3
text 175 197 4

text 5 185 0
text 5 145 1
text 5 105 2
text 5 65 3

style lc:#f00 ls:0 lw:2 lo:1 fc:#f00 fo:1
arrow 20 180 180 60

style lw:0 fc:#000 fo:1 ts:normal tw:bold tf:Times tz:16px
text 95 105 c

style lc:#000 ls:8-4 lw:0.8 lo:1
line 20 60 180 60
line 180 60 180 180
</oo>

Objects with different position and velocity signs are shown in Fig. <a href="#fig:ulm-pos-velo">1</a>: (a) positive position and positive velocity, (b) positive position and negative velocity, (c) negative position and positive velocity, (d) negative position and negative velocity.


## Equations
Final position $x_t$ and its relation to initial position $x_0$, velocity $v$, initial time $t_0$, and time $t$ is given by

\begin{equation}
\label{eqn:ulm-position}
x_t = x_0 + v (t - t_0).
\end{equation}

In some books Eqn. \eqref{eqn:ulm-position} is written

\begin{equation}
\label{eqn:ulm-position-simpler}
x = x_0 + v t.
\end{equation}

which is simpler but with the same meaning. Notice that in \eqref{eqn:ulm-position-simpler} it is assumed that $t_0 = 0$.


## References
1. <a name="ref2"></a>-, "Uniform Linear Motion: Constant Velocity Motion along a Line", Phyley, 3 Feb 2019, url <https://www.phyley.com/uniform-linear-motion> [20200913].
2. <a name="ref2"></a>José L. Fernández, "Equations of Constant Velocity Motion", Fisicalab, url <https://www.fisicalab.com/en/section/urm-equations> [20200913].
3. <a name="ref3"></a>The Editors of Encyclopaedia Britannica, "Vector", Encyclopædia Britannica, 27 May 2020, url <https://www.britannica.com/science/linear-motion> [20200913].
4. <a name="ref4"></a>Carl R. Nave, "Description of Motion", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/mot.html> [20200913].
5. <a name="ref5"></a>David Lewis, "Answer to 'Why are speed, velocity, acceleration, distance, displacement, and time called the parameters of motion?", Quora, 21 Mar 2017, url <https://qr.ae/pNCRxz> [20200913].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-09-12-uniform-linear-motion.md)
