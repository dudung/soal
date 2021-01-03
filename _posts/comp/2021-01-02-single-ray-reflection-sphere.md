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
Reflection of single ray of laser beam on particle acting as spherical convex mirror [[1](#ref1)] based on the law of reflection [[2](#ref2)] is discussed here.


## root finding
Assuming that there is `getBeamWavefrontPosition` function as in [single ray from a source to a certain direction](/comp/single-ray-source-direction), which can produce point $A$ at time $t$ and point $B$ at time $t + \Delta t$ as shown in Fig. <a href="#fig:srfs-ray-reflection-site">1</a>, where the actual reflection occurs at point $C$ with $\overline{OC} = R_{\rm par}$ is radius of spherical particle. Center of the particle is point $O$.

{:refdef: style="text-align: center;"}
![..](/assets/img/comp/ray-reflection-sphere.png)
<br />
Figure <a name="fig:srfs-ray-reflection-site">1</a> Ray reflection site $C$ on a spherical particle centered at $O$ with particle radius $R_{\rm par} = \overline{OC}$.
{: refdef}

Wavefront of the ray is propagating in $\hat{n} _{\rm dir}$ direction with position advancement $v _{\rm ray} \Delta t$ at each iteration. Obtaining point $C$ from point $A$ (out of the particle) and point $B$ (in the particle) is actually a root finding problem. Position of light beam wavefront is

\begin{equation}
\label{eqn:srfs-lbwf-u}
\vec{r}_{\rm waf} (t) = \vec{r} _{\rm src} +  \hat{n} _{\rm dir} \ u(t - t_0) \ v _{\rm ray} \ (t - t_0)
\end{equation}

as in [single ray from a source to a certain direction](/comp/single-ray-source-direction). Using Eqn. \eqref{eqn:srfs-lbwf-u} we can define

\begin{equation}
\label{eqn:srfs-lbwf-u-root-function}
f_{\rm root}(t) = \| \vec{r}_{\rm waf} (t) - \vec{r}_O \| - R _{\rm par},
\end{equation}

where $\vec{r}_O$ is position of center of spherical particle. Solution of Eqn. \eqref{eqn:srfs-lbwf-u-root-function} is found when

\begin{equation}
\label{eqn:srfs-lbwf-u-root-function-solution}
f _{\rm root}(t) = 0 \rightarrow t = t_C
\end{equation}

with $t_A \le t_C \le t_B$. In Fig. <a href="#fig:srfs-ray-reflection-site">1</a> $t_A = t$ and $t_B = t + \Delta t$, where $t_C$ is not known. Eqn. \eqref{eqn:srfs-lbwf-u-root-function-solution} do gives the root since $f _{\rm root}(t_A) > 0$ and $f _{\rm root}(t_B) < 0$, or $f _{\rm root}(t_A) f _{\rm root}(t_B) < 0$. And implementation of $f _{\rm root}$ in JS is simply

```javascript
function f_root(r_waf, r_O, R_par) {
	var dist = Vect3.sub(r_waf, r_O).len();
	var f = dist - Rpar;
	return f;
}
```

by assuming that `getBeamWavefrontPosition` function exists, which calculate `r_waf` value for one of the arguments of `f_root` function.


## secant method
Root of Eqn. \eqref{eqn:srfs-lbwf-u-root-function} can be find numerically, e.g. using secant method, which its iterative formula tion is  [[3](#ref3)]

\begin{equation}
\label{eqn:srfs-lbwf-u-root-solution-secant}
t_n = t _{n-1} - \left( \frac{t _{n-1} - t _{n-2}}{f _{n-1} - f _{n-2}} \right) f _{n-1},
\end{equation}

where $f_n = f(t_n)$. Since the method requires two pointm i.e. $(t _{n-1}, f _{n-1})$ and $(t _{n-2}, f _{n-2})$, we can simply use 

\begin{equation}
\label{eqn:srfs-lbwf-u-root-solution-secant-tn-2}
t _{n-2} = t_A
\end{equation}

and

\begin{equation}
\label{eqn:srfs-lbwf-u-root-solution-secant-tn-1}
t _{n-1} = t_B
\end{equation}

which are provided as in [single ray from a source to a certain direction](/comp/single-ray-source-direction) for `getBeamWavefrontPosition` function. Eqn. \eqref{eqn:srfs-lbwf-u-root-solution-secant} can be implemented in JS as follow

```javascript
function rootSecant(f, tA, tB, N) {
	var tn_2 = tB;
	var tn_1 = tA;
	var tn;
	for(var n = 0; n < N; n++) {
		var fn_2 = f(tn_2);
		var fn_1 = f(tn_1);
		
		tn = tn_1 - ( (tn_1 - tn_2) / (fn_1 - fn_2) ) * fn_1;
		
		tn_2 = tn_1;
		tn_1 = tn;
	}
	return tn;
}
```

using previous snippet of `f_root`, where $N$ is number of iteration. In the `main` function the use of previous function can be as follow

```javascript
var t_0 = 0;
var dt = 1;
var t = -10 * t_0;

var trajectory = [];
var r_src = new Vect3(1, 0, 0);
var n_dir = new Vect3(-0.8, 0.6, 0);
var v_ray = 0.1;

var r_O = new Vect3(-2, 4, 0);
var R_par = 0.1;

var N = 90;
for(var n = 0; n <= N; n++) {
	var r_waf = getBeamWavefrontPosition(r_src, n_dir, v_ray, t_0, t);
	trajectory.push(r_waf);
	
	var tA = t;
	var fA = f_root(r_waf, r_O, R_par);
	
	t = advanceTime(dt, t);
	var tB = t;
	var r_waf = getBeamWavefrontPosition(r_src, n_dir, v_ray, t_0, t);
	var fB = f_root(r_waf, r_O, R_par);
	
	if(fA * fB < 1) {
		var N_irf = 10;
		var tC = rootSecant(f_root, tA, tB, N2);
		
		var r_waf = getBeamWavefrontPosition(r_src, n_dir, v_ray, t_0, tC);
		trajectory.push(r_waf);
		
		break;
	}
}

drawPolyline(trajectory);
```

which draws the trajectory of laser beam until it touches the spharical particle, i.e. the reflection site.


## ray direction after reflection
Using the law of reflection [[2](#ref2)], vector formulation of ray direction after reflection can be obtained [[4](#ref4)]


## references
1. <a name="ref1"></a>Richard Fitzpatrick, "Image Formation by Convex Mirrors", Electromagnetism and Optics: An introductory course, The University of Texas at Austin, 14 Jul 2007, url <http://farside.ph.utexas.edu/teaching/302l/lectures/node138.html> [20210103].
2. <a name="ref2"></a>Carl R. Nave, "Law of Reflection", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/phyopt/Fermat.html> [20210103].
3. <a name="ref3"></a>Eric W. Weisstein, "Secant Method", from MathWorld--A Wolfram Web Resource, url <https://mathworld.wolfram.com/SecantMethod.html> [20200101].
4. <a name="ref4"></a>Wikipedia contributors, "Specular reflection", Wikipedia, The Free Encyclopedia, 18 Dec 2020, 14:02 UTC, url <https://en.wikipedia.org/w/index.php?oldid=994967599> [20210103].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/comp/2021-01-02-single-ray-reflection-sphere.md)
