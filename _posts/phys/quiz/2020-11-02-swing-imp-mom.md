---
layout: post
author: viridi
title: swinging pendulum - momentum
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: ["conservation of energy", "pendulum", "conservation of momentum", "impulse"]
date: 2020-11-02 19:58:00 +07
permalink: /physics/quiz/swing-imp-mom
---
Two successive collisions, the first is swinging pendulum with a block and the second is moving block with another block, are discussed here.


## Problem
A system of swinging pendulum ($m_0 + m_1$) and two blocks ($m_2$ and $m_3$) on top of a horizontal surface, which is frictionless ($\mu_k = 0$), is shown in Fig. <a href="#fig:sim-system">1</a>.

{:refdef: style="text-align: center;"}
![swingin pendulum colliding a block](/assets/img/phys/swing-impuls-momentum.png)
<br />
Figure <a name="fig:sim-system">1</a> A pendulum swings and hits first block, transfer all its kinetic energy and momentum to it, later the first block collides second block and transfers only partially its kinetic energy and momentum.
{: refdef}

It would be better and easier if we divide the problem into four consecutive parts, where in each part some related concepts are applied.


## Concept
Following concepts are required in solving the problem
1. **Moment of inertia** <br />
For a mass $m$ with distance $l$ from center of rotation
\begin{equation}
\label{eqn:sim-moi-ml2}
I = ml^2
\end{equation}
and for a beam rotated on one of its end
\begin{equation}
\label{eqn:sim-moi-beam-end}
I = \frac{1}{3} M L^2,
\end{equation}
with $M$ and $L$ are mass and  length of the beam, respectively.
2. **Conservation of energy**<br />
Mechanical energy $E$ is conserved without work of non-conservative force
\begin{equation}
\label{eqn:sim-moi-coe}
E = mgh + \frac12 m v^2 + \frac12 I \omega^2
\end{equation},
where in right side there are terms for gravitational potential energy, translational kinetic energy, and rotational kinetic energy.
3. **Conservation of momentum**<br />
During a collision, in absence of external force, momentum $\vec{P}$ is conserved
\begin{equation}
\label{eqn:sim-moi-com}
\vec{P} = \vec{p}_1 + \vec{p}_2 + \dots + \vec{p}_N,
\end{equation}
for system consisted of $N$ particles.
4. **Impulse and momentum**<br />
Force $F$ can give an impuls to an object and change the object momentum
\begin{equation}
\label{eqn:sim-moi-imp-mom-force}
F \Delta t = I = \Delta p = p_f - p_i
\end{equation}
with $\Delta t$ is time duration where the force is working on the object.



## Note
There are some assumption used in solving this problem.

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/quiz/2020-11-02-swing-imp-mom.md)
