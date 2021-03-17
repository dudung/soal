---
layout: post
author: viridi
title: rolling down an incline
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: [""]
date: 2020-11-02 11:33:00 +07
permalink: /physics/rolling-down-an-incline
---
Discussing an object rolling down an incline is interesting, since it brings in many different concepts in introductory physics [[1](#ref1)], where the object can be sphere, hoop, or cylinder [[2](#ref2)]. It is also fun to observe the race of rolling objects with different moment of inertia [[3](#ref3)].


## Down an incline
While down an incline, object can performm a sliding or a rolling, where both ways are shown in Fig. <a href="#fig:rdai-down-an-incline">1</a>. Using the first way object can be still considered as a point mass and it requires that

\begin{equation}
\label{eqn:rdai-slides-requirement}
\tan \theta > \mu_s,
\end{equation}

to be able to slide down with normally $\mu_s > \mu_k$, while using the second way object must be considered as a rigid body and $\mu_s > \mu_k > 0$.

{:refdef: style="text-align: center;"}
![down an incline](/assets/img/phys/down-an-incline.png)
<br />
Figure <a name="fig:rdai-down-an-incline">1</a> A point mass slides down an incline (left) and rigid body rolls down an incline (right).
{: refdef}

As a point mass $m$ slides down an incline, its velocity $v$ changes due to its acceleration $a$. We can have

\begin{equation}
\label{eqn:rdai-slides-down}
a = g (\sin \theta - \mu_k \cos \theta) 
\end{equation}

for Fig. <a href="#fig:rdai-down-an-incline">1 (left)</a> from previous discussion and when $\mu_k = 0$, Eqn. \eqref{eqn:rdai-slides-down} will be reduced to

\begin{equation}
\label{eqn:rdai-slides-down-uk=0}
a = g \sin \theta.
\end{equation}

And as a rigid body rolls down an incline, its angular velocity $\omega$ changes due to its angular acceleration $\alpha$, where for pure rolling we have that

\begin{equation}
\label{eqn:rdai-pure-rolling-omega-v}
v = \omega R
\end{equation}

and

\begin{equation}
\label{eqn:rdai-pure-rolling-alpha-a}
a = \alpha R
\end{equation}

with $R$ is radius of the object.


## Pure rolling
For simplicity only pure rolling is considered in this discussion.

### Free-body diagram
Let's see the case in Fig. <a href="#fig:rdai-down-an-incline">1 (right)</a>, where its free-body diagram can be obtained as shown in Fig. <a href="#fig:rdai-free-body-diagram">2</a>.

{:refdef: style="text-align: center;"}
![down an incline](/assets/img/phys/rdai-free-body-diagram.png)
<br />
Figure <a name="fig:rdai-free-body-diagram">2</a> Free-body diagram of an object rolling down an incline.
{: refdef}

Fig. <a href="#fig:rdai-free-body-diagram">2 (left)</a> is showing the forces acteing upon the object, while the forces and also decompotision of weight $w$ along $x$ and $y$ directions is given in Fig. <a href="#fig:rdai-free-body-diagram">2 (right)</a>. Using the last part of the figure we will apply Newton's laws.

### Statics in $y$ direction
Using Newton's 1st law we can have in $y$ direction that

\begin{equation}
\label{eqn:rdai-pr-y}
\begin{array}{rcl}
\sum F_y & = & 0 \newline
N - w \cos \theta & = & 0 \newline
N & = & w \cos \theta.
\end{array}
\end{equation}

### Dynamics in $x$ direction
Using Newton's 2nd law we can have in $x$ direction that

\begin{equation}
\label{eqn:rdai-pr-x}
\begin{array}{rcl}
\sum F_x & = & m a_x \newline
w \sin \theta - f & = & m a_x.
\end{array}
\end{equation}

### Rotation during rolling
Using Newton's 2nd law for rotational motion we can have

\begin{equation}
\label{eqn:rdai-pr-theta}
\begin{array}{rcl}
\sum \tau & = & I \alpha \newline
f R & = & I \alpha.
\end{array}
\end{equation}

Notice that we do not calculate $f$ directly from $N$ but keep it unknown.

### Finding the solution
Using Eqn. \eqref{eqn:rdai-pure-rolling-alpha-a} in Eqn. \eqref{eqn:rdai-pr-theta} will give

\begin{equation}
\label{eqn:rdai-pr-f}
f = \frac{Ia}{R^2}.
\end{equation}

Substitution of Eqn. \eqref{eqn:rdai-pr-f} to Eqn. \eqref{eqn:rdai-pr-x} will produce

\begin{equation}
\label{eqn:rdai-pr-solution-x}
\begin{array}{rcl}
\displaystyle m g \sin \theta - \frac{Ia}{R^2} & = & m a \newline
m g \sin \theta & = & \displaystyle \left( m + \frac{I}{R^2} \right) a \newline
a & = & \displaystyle \left( \frac{m}{m + I/R^2} \right) g \sin \theta.
\end{array}
\end{equation}

For non-rotating point mass particle or rigid body with $I = 0$, Eqn. \eqref{eqn:rdai-pr-solution-x} will turn into Eqn. \eqref{eqn:rdai-slides-down-uk=0}. Notice that $a$ in Eqn. \eqref{eqn:rdai-pr-f} and $a_x$ in Eqn. \eqref{eqn:rdai-pr-x} are the same.


## Exercises
1. Find information about moments of inertia of hoop, solid cylinder, solid sphere, and thin spherical shell. Use the information in Eqn. \eqref{eqn:rdai-pr-solution-x} to find the acceleration.
2. See [[3](#ref3)] and use previous result to confirm it.


## References
1. <a name="ref1"></a>Rhett Allain, "Rolling Object Accelerating Down an Incline", Wired, 29 Sep 2014, url <https://www.wired.com/2014/07/a-rolling-object-accelerating-down-an-incline/> [20201102].
2. <a name="ref2"></a>Carl R. Nave, "Rolling Objects", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/rotwe.html#ro> [20201102].
3. Flipping Physics, "Which Will Be First? (Rolling Down an Incline)", YouTube, 17 Mar 2019, url <https://www.youtube.com/watch?v=jaqS5dJlrjY> [20201002].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-11-02-rolling-down-an-incline.md)
