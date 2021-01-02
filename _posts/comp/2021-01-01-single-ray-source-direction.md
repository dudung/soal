---
layout: post
author: viridi
title: single ray source direction
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: computation
tags: ["geometrical otpics", "finite difference", "javascript"]
date: 2021-01-01 20:17:00 +07
permalink: /comp/single-ray-source-direction
---

Using ray tracing [[1](#ref1)], where the modern optical design is still involving the method but as a computer-aided technique [[2](#ref2)], simulator can be developed [[3](#ref3)]. Simulation of laser beam interaction with random packings of mono-size and poly-size spherical particles implements this method [[4](#ref4)].


## light source
Two parameters are required to define a light source emitting a single ray as shown in Fig. <a href="#fig:srsd-lsd">1</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/comp/ray-source-direction.png)
<br />
Figure <a name="fig:srsd-lsd">1</a> A light source is positioned at $\vec{r} _{\rm src}$ with direction of $\hat{n} _{\rm dir}$, where $\theta = 0.5 \pi$ in this case ($\theta$ is measured from $z$ axis to the direction of $x$ axis).
{: refdef}

The first is 

\begin{equation}
\label{eqn:srsd-lso}
\vec{r}_{\rm src} = x _{\rm src} \ \hat{x} + y _{\rm src} \ \hat{y} + z _{\rm src} \ \hat{z}
\end{equation}

as position of laser source output and the second is

\begin{equation}
\label{eqn:srsd-lbd}
\hat{n}_{\rm dir} = \sin \theta _{\rm dir} \cos \phi _{\rm dir} \ \hat{x} + \sin \theta _{\rm dir} \sin \phi _{\rm dir} \ \hat{y} + \cos \theta _{\rm dir} \ \hat{z}
\end{equation}

as laser beam direction, which is a unit vector. The angles $\theta _{\rm dir}$ and $\phi _{\rm dir}$ are the angles in spherical coordinates using convention in physics $(r, \theta, \phi)$ [[5](#ref5)], where for unit vector $r = 1$ or $\|\hat{n} _{\rm dir}\| = 1$.


## ray tracing
In experiment laser is used to perform the ray tracing [[6](#ref6)] and the ray can be traced numerically in simple way using ray velocity $v_{\rm ray}$ and Eqns. \eqref{eqn:srsd-lso} and \eqref{eqn:srsd-lbd}. Position of laser beam wavefront at time $t$ can be defined as

\begin{equation}
\label{eqn:srsd-lbwf}
\vec{r}_{\rm waf} (t) = \vec{r} _{\rm src} +  \hat{n} _{\rm dir} v _{\rm ray} (t - t_0)
\end{equation}

if the laser is turned on at $t = t_0$. Since the time $t$ is disrete in numerical approximation, it will be updated through

\begin{equation}
\label{eqn:srsd-time-update}
t \equiv t_n = t_{n-1} + \Delta t,
\end{equation}

where $\Delta t$ is time step of the simulation and $n$ is $n$-th step in the iteration. We can also write Eqn. \eqref{eqn:srsd-time-update} in other form

\begin{equation}
\label{eqn:srsd-time-t}
t = t_0 + n \Delta t,
\end{equation}

with $n = 0, 1, 2, .., N$. Eqn. \eqref{eqn:srsd-lbwf} in better form

\begin{equation}
\label{eqn:srsd-lbwf-u}
\vec{r}_{\rm waf} (t) = \vec{r} _{\rm src} +  \hat{n} _{\rm dir} \ u(t - t_0) \ v _{\rm ray} \ (t - t_0)
\end{equation}

using unit step function [[7](#ref7)]

\begin{equation}
\label{eqn:srsd-u}
u(t- t_0) = \left\\{
\begin{array}{lr}
0, & t < t_0, \newline
1, & t \ge t_0,
\end{array}
\right.
\end{equation}

to assure that the laser beam wavefront is propagating only when $t \ge t_0$.


## implementation with js
Using JavaScript (JS) Eqns. \eqref{eqn:srsd-time-t} and \eqref{eqn:srsd-lbwf-u} can calculated using following snippets [[8](#ref8)]. One way to implement Eqn. \eqref{eqn:srsd-lbwf-u} is

```javascript
function getBeamWavefrontPosition(r_src, n_dir, v_ray, t_0, t) {
	var dt = t - t_0;
	var u = (t >= t_0) ? 1 : 0;
	var dr = Vect3.Mul(n_dir, u * v_ray * dt);
	var r_waf = Vect3.add(r_src, dr);
	return r_waf;
}
```

with `Vect3` is a class for 3d [vector](/physics/vector). And for Eqn. \eqref{eqn:srsd-time-t} is simply

```javascript
function advanceTime(dt, t) {
	var t_new = t + dt;
	return t_new;
}
```

where `t = t + dt` is still the simplest one. For drawing the ray trajectory array of `Vect3` is required.


## references
1. <a name="ref1"></a>Wikipedia contributors, "Ray tracing (physics)", Wikipedia, The Free Encyclopedia, 20 Dec 2020, 01:37 UTC, url <https://en.wikipedia.org/w/index.php?oldid=995258966> [20210101].
2. <a name="ref2"></a>Thomas V. Higgins, "All rays lead to geometrical optics", Laser Focus World, 1 Dec 2000, url <https://www.laserfocusworld.com/optics/article/16555510/all-rays-lead-to-geometrical-optics> [20210101].
3. <a name="ref3"></a>Johnson Rick Tu, "Ray Optics Simulation", GitHub, 20 Aug 2018, url <https://ricktu288.github.io/ray-optics/>
4. <a name="ref4"></a>O. B. Kovaleva, I. O. Kovaleva, and V. V. Belyaev, "Ray tracing method for simulation of laser beam interaction with random packings of powders", AIP Conference Proceedings [AIP Conf. Proc.], vol. 1939, no. 1, p. 020028, Mar 2018, url <https://doi.org/10.1063/1.5027340>
5. <a name="ref5"></a>Eric W. Weisstein, "Spherical Coordinates", from MathWorld--A Wolfram Web Resource, url <https://mathworld.wolfram.com/SphericalCoordinates.html> [20200101].
6. <a name="ref6"></a>Leno S. Pedrotti, "Basic Geometrical Optics", in Chandra Roychoudhuri (ed), Fundamentals of Photonics, 2008, pp. 73-116, url <https://doi.org/10.1117/3.784938.ch3>
7. <a name="ref7"></a>William F. Trenchm "8.4: The Unit Step Function", MTH 225 Differential Equations, Mathematics, LibreTexts, 7 Jan 2020, url <https://math.libretexts.org/Courses/Monroe_Community_College/MTH_225_Differential_Equations/8:_Laplace_Transforms/8.4:_The_Unit_Step_Function> [20210101].
8. <a name="ref8"></a>Wikipedia contributors, "Snippet (programming)", Wikipedia, The Free Encyclopedia, 19 Dec 2020, 05:43 UTC, url <https://en.wikipedia.org/w/index.php?oldid=995096644> [20210102].
+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/comp/2021-01-01-single-ray-source-direction.md)
