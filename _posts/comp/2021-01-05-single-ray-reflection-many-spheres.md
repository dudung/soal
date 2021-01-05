---
layout: post
author: viridi
title: single ray reflection many spheres
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: computation
tags: ["geometrical otpics", "finite difference", "javascript"]
date: 2021-01-05 07:48:00 +07
permalink: /comp/single-ray-reflection-many-spheres
---
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
For the first sphere as shown in Fig. <a href="#fig:srrms-ray-reflection-sphere-1">1</a>

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


## references
1. <a name="ref1"></a>Carl R. Nave, "Law of Reflection", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/phyopt/Fermat.html> [20210105].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/comp/2021-01-05-single-ray-reflection-many-spheres.md)
