---
layout: post
author: viridi
title: moment of inertia
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: [""]
date: 2020-11-02 06:17:00 +07
permalink: /physics/moment-of-inertia
---
Some concepts are related to moment of inertia, e.g. Newton's 2nd law for rotation, rotational kinetic energy, angular momentum, mass distribution, parallel and perpendicular axis theorems, etc [[1](#ref1)]. Moment of inertia is also known as mass moment of inertia, angular mass, or rotational intertia [[2](#ref2)].


## Definition
Moment of inertia $I$ is as defined product of mass of a section or part of an object $m$ and the square distance between that center of that part to a reference axis $r_\perp^2$, which 

\begin{equation}
\label{eqn:moi-def}
I = m r_\perp^2,
\end{equation}

where for system with many objects, e.g. $N$ body system, it becomes

\begin{equation}
\label{eqn:moi-def-discrete}
I = \sum_{i = 1}^N m_i r_{\perp, i}^2,
\end{equation}

since it is an extensive physical property that has additive feature. Eqn. \eqref{eqn:moi-def-discrete} can also be seen as a discrete system, while for a continuum system, it must use integral

\begin{equation}
\label{eqn:moi-def-continuum}
I = \int r_\perp^2 \ dm.
\end{equation}

Illustration of both systems is given in following Fig. <a href="#fig:moi-discrete-continuum">1</a>.

{:refdef: style="text-align: center;"}
![moment of inertia of dicrete and continuum systems](/assets/img/phys/moi-disc-cont.png)
<br />
Figure <a name="fig:moi-discrete-continuum">1</a> A discrete system consisted of four objects (left) and a continuum system (right).
{: refdef}


## Common moment of inertia
Regular form objects have a well-known moment of inertia. Some examples of them are shown in Fig. <a href="#fig:moi-common-form">2</a>.

{:refdef: style="text-align: center;"}
![example of common moment of inertia](/assets/img/phys/moi-common-forms.png)
<br />
Figure <a name="fig:moi-common-form">2</a> Common moments of inertia.
{: refdef}


## Parallel axis theorem
If moment of inertia through center of mass $I_{\rm com}$ is known then moment of inertia about to another axis parallel to the main axis can be calculated

\begin{equation}
\label{eqn:moi-def-parallel-axis-theorem}
I = I_{\rm com} + Ml^2,
\end{equation}

where $l$ is the distance for another axis to the main axis.


## Exercises
1. Use Eqn. \eqref{eqn:moi-def-parallel-axis-theorem} to prove the formulation of two moment of inertia in the last rows in Fig. <a href="#fig:moi-common-form">2</a>. Which formulation is showing the $I_{\rm com}$?


## References
1. <a name="ref1"></a>Carl R. Nave, "Moment of Intertia Concepts", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/inecon.html> [20201102].
2. <a name="ref2"></a>Wikipedia contributors, "Moment of inertia", Wikipedia, The Free Encyclopedia, 19 Oct 2020, 05:51 UTC, <https://en.wikipedia.org/w/index.php?oldid=984272703> [20201102].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-11-02-moment-of-inertia.md)
