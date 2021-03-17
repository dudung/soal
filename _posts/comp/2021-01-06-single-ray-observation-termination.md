---
layout: post
author: viridi
title: single ray observation termination
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: computation
tags: ["geometrical otpics", "finite difference", "javascript"]
date: 2021-01-06 07:48:00 +07
permalink: /comp/single-ray-observation-termination
---
..

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/comp/2021-01-06-single-ray-observation-termination.md)


{% comment %}
Reflection of single ray of laser beam on many spheres can be performed using [single ray reflection on a single sphere](/comp/single-ray-reflection-sphere) consecutively until the beam leaving the observation region or arrving at a light sensor.


## many spheres system
Fig. <a name="#fig:srrms-many-spheres-system">1</a> shows the illustration how a single ray of laser beam reflected multiple times by many spheres.

{:refdef: style="text-align: center;"}
![..](/assets/img/comp/ray-reflected-many-spheres.png)
<br />
Figure <a name="fig:srrs-inc-ref-beam">1</a> Single ray of laser beam reflected multiple times in a many spheres system ($N = 6$).
{: refdef}

In each reflection on a spherical particles law of relection [[1](#ref1)] always holds.


## reflection on 1st sphere
For the first sphere as shown in Fig. <a href="#fig:srrms-ray-reflection-sphere-1">2</a>

{:refdef: style="text-align: center;"}
![..](/assets/img/comp/ray-reflection-sphere-1.png)
<br />
Figure <a name="fig:srrms-ray-reflection-sphere-1">1</a> Single ray of laser beam reflected on the first sphere located at $\vec{r} _{O,1}$.
{: refdef}

following relation holds

\begin{equation}
\label{eqn:srrms-reflection-sphere-1}
\hat{n} _{\rm ref,1} = \hat{n} _{\rm dir} - 2 (\hat{n} _{\rm dir} \cdot \hat{n} _{\rm par,1}) \hat{n} _{\rm par,1},
\end{equation}

where the derivation has been discussed in [single ray reflection on a single sphere](/comp/single-ray-reflection-sphere).


## reflection on 2nd sphere
For the second sphere as shown in Fig. <a href="#fig:srrms-ray-reflection-sphere-2">3</a>

{:refdef: style="text-align: center;"}
![..](/assets/img/comp/ray-reflection-sphere-2.png)
<br />
Figure <a name="fig:srrms-ray-reflection-sphere-2">3</a> Single ray of laser beam reflected on the second sphere located at $\vec{r} _{O,2}$.
{: refdef}

following relation holds

\begin{equation}
\label{eqn:srrms-reflection-sphere-2}
\hat{n} _{\rm ref,2} = \hat{n} _{\rm ref,1} - 2 (\hat{n} _{\rm ref,1} \cdot \hat{n} _{\rm par,2}) \hat{n} _{\rm par,2},
\end{equation}

similar to Eqn. \eqref{eqn:srrms-reflection-sphere-1}.


## reflection on 3rd  sphere
For the third sphere as shown in Fig. <a href="#fig:srrms-ray-reflection-sphere-3">4</a>

{:refdef: style="text-align: center;"}
![..](/assets/img/comp/ray-reflection-sphere-3.png)
<br />
Figure <a name="fig:srrms-ray-reflection-sphere-3">4</a> Single ray of laser beam reflected on the third sphere located at $\vec{r} _{O,3}$.
{: refdef}

following relation holds

\begin{equation}
\label{eqn:srrms-reflection-sphere-3}
\hat{n} _{\rm ref,3} = \hat{n} _{\rm ref,2} - 2 (\hat{n} _{\rm ref,2} \cdot \hat{n} _{\rm par,3}) \hat{n} _{\rm par,3},
\end{equation}

similar to Eqn. \eqref{eqn:srrms-reflection-sphere-2}.


## reflection on 4th sphere
For the third sphere as shown in Fig. <a href="#fig:srrms-ray-reflection-sphere-4">5</a>

{:refdef: style="text-align: center;"}
![..](/assets/img/comp/ray-reflection-sphere-4.png)
<br />
Figure <a name="fig:srrms-ray-reflection-sphere-4">5</a> Single ray of laser beam reflected on the third sphere located at $\vec{r} _{O,4}$.
{: refdef}

following relation holds

\begin{equation}
\label{eqn:srrms-reflection-sphere-4}
\hat{n} _{\rm ref,4} = \hat{n} _{\rm ref,3} - 2 (\hat{n} _{\rm ref,3} \cdot \hat{n} _{\rm par,4}) \hat{n} _{\rm par,4},
\end{equation}

similar to Eqn. \eqref{eqn:srrms-reflection-sphere-3}.


## reflection on 5th  sphere
For the third sphere as shown in Fig. <a href="#fig:srrms-ray-reflection-sphere-5">6</a>

{:refdef: style="text-align: center;"}
![..](/assets/img/comp/ray-reflection-sphere-5.png)
<br />
Figure <a name="fig:srrms-ray-reflection-sphere-5">6</a> Single ray of laser beam reflected on the third sphere located at $\vec{r} _{O,5}$.
{: refdef}

following relation holds

\begin{equation}
\label{eqn:srrms-reflection-sphere-5}
\hat{n} _{\rm ref,5} = \hat{n} _{\rm ref,4} - 2 (\hat{n} _{\rm ref,4} \cdot \hat{n} _{\rm par,5}) \hat{n} _{\rm par,5},
\end{equation}

similar to Eqn. \eqref{eqn:srrms-reflection-sphere-4}.


## reflection on 6th  sphere
For the third sphere as shown in Fig. <a href="#fig:srrms-ray-reflection-sphere-6">7</a>

{:refdef: style="text-align: center;"}
![..](/assets/img/comp/ray-reflection-sphere-6.png)
<br />
Figure <a name="fig:srrms-ray-reflection-sphere-6">7</a> Single ray of laser beam reflected on the third sphere located at $\vec{r} _{O,6}$.
{: refdef}

following relation holds

\begin{equation}
\label{eqn:srrms-reflection-sphere-6}
\hat{n} _{\rm ref,6} = \hat{n} _{\rm ref,5} - 2 (\hat{n} _{\rm ref,5} \cdot \hat{n} _{\rm par,6}) \hat{n} _{\rm par,6},
\end{equation}

similar to Eqn. \eqref{eqn:srrms-reflection-sphere-5}.


## iteration formula
Resuming from Eqns. \eqref{eqn:srrms-reflection-sphere-1}-\eqref{eqn:srrms-reflection-sphere-6} we can have

\begin{equation}
\label{eqn:srrms-reflection-sphere-i}
\hat{n} _{\rm ref,i} = \hat{n} _{\rm ref,i-1} - 2 (\hat{n} _{\rm ref,i-1} \cdot \hat{n} _{\rm par,i}) \hat{n} _{\rm par,i}
\end{equation}

with $i = 1, 2, 3, ..$, where

\begin{equation}
\label{eqn:srrms-reflection-sphere-i=0}
\hat{n} _{\rm ref,0} = \hat{n} _{\rm dir},
\end{equation}

is the ray from the first light source located at $\vec{r} _{\rm src}$ as in Figs. <a name="#fig:srrms-many-spheres-system">1</a> and <a href="#fig:srrms-ray-reflection-sphere-1">2</a>. Eqn. \eqref{eqn:srrms-reflection-sphere-i} gives the direction of ray reflected by $i$-th sphere in $N$ spheres system.


## references
1. <a name="ref1"></a>Carl R. Nave, "Law of Reflection", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/phyopt/Fermat.html> [20210105].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/comp/2021-01-05-single-ray-reflection-many-spheres.md)

{% endcomment %}
