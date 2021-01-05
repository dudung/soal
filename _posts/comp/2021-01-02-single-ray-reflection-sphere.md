---
layout: post
author: viridi
title: single ray reflection sphere
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: computation
tags: ["geometrical otpics", "finite difference", "javascript"]
date: 2021-01-02 12:53:00 +07
permalink: /comp/single-ray-reflection-sphere
---
A particle, which performs as spherical convex mirror [[1](#ref1)], can reflect single ray of laser beam based on the law of reflection [[2](#ref2)]. We can consider that the reflection site as a new light source, similar as it [travels from original light source to a certain direction](/comp/single-ray-source-direction) until it arrives at [the reflection site on the surface of spherical particle](/comp/single-ray-reflection-site-on-sphere).


## normal direction
Illustration how a single ray of laser beam reflected by a particle acting as spherical mirror is given in Fig. <a ref="#fig:srrs-inc-ref-beam">1</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/comp/ray-reflected-sphere-0.png)
<br />
Figure <a name="fig:srrs-inc-ref-beam">1</a> Incident ray with direction $\hat{n} _{\rm dir}$ falls on reflection site $\vec{r}_C$ and then is reflected as reflected ray with direction $\hat{n} _{\rm ref}$.
{: refdef}

At the reflection site $\vec{r} _C$ we will have incident ray direction $\hat{n} _{\rm dir}$ and normal direction $\hat{n} _{\rm par}$ on the particle surface, where the last is simply

\begin{equation}
\label{eqn:srrs-normal-par}
\hat{n}_{\rm par} = \frac{\vec{r}_C - \vec{r}_O}{ \left| \vec{r}_C - \vec{r}_O \right|}
\end{equation}

with $\vec{r} _O$  is position of particle center. The normal vector $\hat{n} _{\rm par}$ is the normal line in law of reflection.


## ray direction after reflection
By simplying previous figure we can have Fig. <a ref="#fig:srrs-reflected-ray-derivation">2</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/comp/ray-reflected-sphere-1.png)
<br />
Figure <a name="fig:srrs-reflected-ray-derivation">2</a> Left: incident ray, normal line, reflected ray. Right: Derivation of reflected ray.
{: refdef}

Then with vector formulation of ray direction after reflection can be obtained [[3](#ref3)]

\begin{equation}
\label{eqn:srrs-normal-ref}
\hat{n} _{\rm ref} = \hat{n} _{\rm dir} - 2 (\hat{n} _{\rm dir} \cdot \hat{n} _{\rm par}) \hat{n} _{\rm par}.
\end{equation}

To produce Eqn. \eqref{eqn:srrs-normal-ref} we can use vector projections and components  [[4](#ref4)].


## references
1. <a name="ref1"></a>Richard Fitzpatrick, "Image Formation by Convex Mirrors", Electromagnetism and Optics: An introductory course, The University of Texas at Austin, 14 Jul 2007, url <http://farside.ph.utexas.edu/teaching/302l/lectures/node138.html> [20210103].
2. <a name="ref2"></a>Carl R. Nave, "Law of Reflection", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/phyopt/Fermat.html> [20210103].
3. <a name="ref3"></a>Wikipedia contributors, "Specular reflection", Wikipedia, The Free Encyclopedia, 18 Dec 2020, 14:02 UTC, url <https://en.wikipedia.org/w/index.php?oldid=994967599> [20210103].
4. <a name="ref4"></a>Bart Snapp, Jim Talamo, "Projections and components", Ximera, The Ohio State University, 31 Oct 2018, url <https://ximera.osu.edu/mooculus/calculus2/dotProducts/digInProjections2E> [20210105].


+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/comp/2021-01-02-single-ray-reflection-sphere.md)
