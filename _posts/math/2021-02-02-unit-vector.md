---
layout: post
author: viridi
title: unit vector
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["vector", "math"]
date: 2021-02-02 02:26:00 +07
permalink: /blank
---
Unit vector is a vector of length 1 and written in symbol with hat ($\hat{}$) [[1](#ref1)]. Examples of common unit vector are $\hat{i}$, $\hat{j}$, and $\hat{k}$, which represent unit vectors in $x$, $y$, and $z$, respectively [[2](#ref2)]. Take a look at a visualization of a unit vector and experience the relation between unit vector and vector components while you are changing them [[3](#ref3)].


## calculate a unit vector
If there is a vector

\begin{equation}
\label{eqn:uv-unit-vector-calculation-vector}
\vec{r} = x \hat{x} + y \hat{y} + z \hat{z},
\end{equation}

then its lenght is

\begin{equation}
\label{eqn:uv-unit-vector-calculation-length}
\begin{array}{rcl}
r & = & \|\vec{r}\| \newline
& = & \sqrt{\vec{r} \cdot \vec{r}} \newline
& = & \sqrt{(x \hat{x} + y \hat{y} + z \hat{z}) \cdot (x \hat{x} + y \hat{y} + z \hat{z})} \newline
& = & \sqrt{x^2 + y^2 + z^2}.
\end{array}
\end{equation}

The unit vector is

\begin{equation}
\label{eqn:uv-unit-vector-calculation-unit-vector}
\begin{array}{rcl}
\hat{r} & = & \displaystyle \frac{\vec{r}}{r} \newline
& = & \displaystyle \frac{x \hat{x} + y \hat{y} + z \hat{z}}{r} \newline
& = & \displaystyle \frac{x}{r}\hat{x} + \frac{y}{r}\hat{y} + \frac{z}{r}\hat{z} \newline
& = & \displaystyle \left( \frac{x}{\sqrt{x^2 + y^2 + z^2}} \right) \hat{x} + \left( \frac{y}{\sqrt{x^2 + y^2 + z^2}} \right) \hat{y} + \left( \frac{z}{\sqrt{x^2 + y^2 + z^2}} \right) \hat{z}.
\end{array}
\end{equation}

For a two-dimensional vector you can set $z$ component to zero.


## illustration
Let us draw three vectors in $xy$ space as shwon in Fig. <a href="#fig:uv-unit-vectors-in-xy-space">1</a>, where unit vectors always have the same direction with their vectors but with length of one.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/vector/unit-vectors-in-xy-space.png)
<br />
Figure <a name="fig:uv-unit-vectors-in-xy-space">1</a> Some vectors in $xy$ space.
{: refdef}

Vectors with numerical values in Fig. <a href="#fig:uv-unit-vectors-in-xy-space">1</a> are intended to show the value of unit vector in relation with its vector length. After knowing this we can draw arbitrary vector qualitatively in $xyz$ space as shown in Fig. <a href="#fig:uv-unit-vectors-in-xyz-space">2</a> instead of quantitatively as in previous Fig. <a href="#fig:uv-unit-vectors-in-xy-space">1</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/math/vector/unit-vectors-in-xyz-space.png)
<br />
Figure <a name="fig:uv-unit-vectors-in-xyz-space">2</a> Some vectors in $xyz$ space.
{: refdef}

Notice that a unit vector length is always one and it can be longer thant its vector, e.g. unit $\hat{a}$ is longer than vector $\vec{a}$, as shown in Fig. <a href="#fig:uv-unit-vectors-in-xyz-space">2</a>. As example, assume that there is a vector

\begin{equation}
\label{eqn:uv-example-1-vector}
\vec{a} = 0.01 \hat{x} - 0.01 \hat{y},
\end{equation}

that will have the unit vector of

\begin{equation}
\label{eqn:uv-example-1-unit-vector}
\hat{a} = 0.707 \hat{x} - 0.707 \hat{y},
\end{equation}

which is longer than the vector. It is better that Eqn. \eqref{eqn:uv-example-1-vector} is written as

\begin{equation}
\label{eqn:uv-example-1-vector-format}
\vec{a} = 0.01 \sqrt{2} \ (0.7071 \hat{x} - 0.7071 \hat{y})
\end{equation}

as advised in the next section. It might be clear if we write $\vec{a} = 0.01 (\hat{x} - \hat{y})$ instead of Eqn. \eqref{eqn:uv-example-1-vector} and  $\vec{a} = 0.01 \sqrt{2} \ (\frac12 \sqrt{2} \hat{x} - \frac12 \sqrt{2} \hat{y})$ instead of Eqn. \eqref{eqn:uv-example-1-vector-format}.


## physical quantity presentation
It is advisable to present a physical quantity of type vector in following format, e.g momentum of a point mass $m$,

\begin{equation}
\label{eqn:uv-physical-quantity-vector-presentation}
\vec{p} = 20 \ (0.7071\hat{x} - 0.7071\hat{y}) \ {\rm kg \cdot m \cdot s^{-1}},
\end{equation}

where $\vec{p}$ is symbol of momentum, $20$ is magnitude of the momentum, $(0.7071\hat{x} - 0.7071\hat{y})$ is unit vector of the momentum, and ${\rm kg \cdot m \cdot s^{-1}}$ is SI base unit for mommentum [[4](#ref4)].


## exercises
1. If there is a vector $\vec{c} = 3\hat{x} + 4\hat{y} + 12\hat{z}$, find its magnitude or length of the vector $c = \|\vec{c}\|$. Write also its unit vector according to third line of Eqn. \eqref{eqn:uv-unit-vector-calculation-unit-vector}.
2. Using Eqn. \eqref{eqn:uv-unit-vector-calculation-unit-vector} prove that $\hat{s}$ from $\vec{s}$ in Fig. <a href="#fig:uv-unit-vectors-in-xy-space">1</a>.
3. Present $\vec{F} = (-60\hat{x} + 80\hat{y}) \ {\rm N}$ using the format given in Eqn. \eqref{eqn:uv-physical-quantity-vector-presentation}.
4. A point mass moves with velocity $\vec{v} = (-\hat{x} + \hat{y}) \ {\rm \mu m/s}$. Rewrite it in the advisable format without using SI prefixes [[5](#ref5)].


## references
1. <a name="ref1"></a>Wikipedia contributors, "Unit vector", Wikipedia, The Free Encyclopedia, 1 Feb 2021, 05:06 UTC, url <https://en.wikipedia.org/w/index.php?oldid=1004126622> [20210202].
2. <a name="ref2"></a>Carl R. Nave, "Unit Vectors", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/vbas.html#c2> [20210202].
3. <a name="ref3"></a>Z. Blakley, "Unit Vector", GeoGebra, November 24, 2016 - 7:49 AM, url <https://www.geogebra.org/m/Qk2TvNXg> [20210202].
4. <a name="ref4"></a>Wikipedia contributors, "List of physical quantities", Wikipedia, The Free Encyclopedia, 25 Jan 2021, 15:26 UTC, url <https://en.wikipedia.org/w/index.php?oldid=1002671591> [20210202].
5. <a name="ref5"></a>-, "SI prefixes" in International System of Units (SI), Physical Measurement Laboratory of NIST, url <https://physics.nist.gov/cuu/Units/prefixes.html> [20210202].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/math/2021-02-02-unit-vector.md)
