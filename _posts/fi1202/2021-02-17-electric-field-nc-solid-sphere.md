---
layout: post
author: viridi
title: electric field of non-conducting solid sphere
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["electric field", "sphere", "solid"]
date: 2021-02-17 18:02 +07
permalink: /fi1202/electric-field-nc-solid-sphere
---
Electric field of a non-conducting solid sphere will be discussed here. After read the problem you can proceed to the theory or go directly to the solution.


## problem
An electric charge $+Q$ is uniformly distributed throughout a non-conducting solid sphere or radius $a$. Determine the electric field everywhere inside and outside the sphere.
[[1](#ref1)].

## theory

### dot product of two unit vectors
If we have two unit vector $\hat{a}$ and $\hat{b}$ then their dot products is

\begin{equation}
\label{eqn:efncsp-dot-product-unit-vectors}
\hat{a} \cdot \hat{b} = \cos\beta
\end{equation}

where $\beta$ is the angle between this two unit vectors [[2](#ref2)]. Result of Eqn. \eqref{eqn:efncsp-dot-product-unit-vectors} will have value between -1 and 1.

### gauss law
The law states that flux of the electric field out of an arbitrary closed surface is proportional to the electric charge enclosed by the surface

\begin{equation}
\label{eqn:efncsp-gauss-law-proportional}
\oint \vec{E} \cdot d\vec{A} \propto q_{\rm enc},
\end{equation}

where the left side represents "flux of the electric field out of an arbitrary closed surface" and the right side represents "the electric charge enclosed by the surface". Eqn. \eqref{eqn:efncsp-gauss-law-proportional} can be written in the form of

\begin{equation}
\label{eqn:efncsp-gauss-law}
\oint \vec{E} \cdot d\vec{A} = \frac{q_{\rm enc}}{\varepsilon_0},
\end{equation}

by introducing $\varepsilon_0^{-1}$, which is the coefficient of proportionality [[3](#ref3)].

### gaussian surface
To obtain electric field $E$ from Eqn. \eqref{eqn:efncsp-gauss-law} we must choose Gaussian surface that matched the electric field vector $\vec{E}$. Since it has the form of

\begin{equation}
\label{eqn:efncsp-electric-field}
\vec{E} = E \hat{r},
\end{equation}

which we assume. Then we chooose

\begin{equation}
\label{eqn:efncsp-area-element}
d\vec{A} = \hat{r} dA = \hat{r} (rd\theta)(r\sin\theta d\phi) = \hat{r} r^2 \sin\theta d\theta d\phi,
\end{equation}

as the area element of the Gaussian surface. The $dA$ is surface element in spherical coordinates [[4](#ref4)].


## solution
### volume chart density
Since the charge is distributed uniformly throughout all parts of the solid sphere then we can have

\begin{equation}
\label{eqn:efncsp-rho}
\rho = \frac{Q}{V} = \frac{Q}{\frac43 \pi a^3},
\end{equation}

where $V = \frac43 \pi a^3$ is volume the sphere.

### gaussian surface


## references
1. <a name="ref1"></a>Sen-ben Liao, Peter Dourmashkin, John W. Belcher, "Gauss's Law", Physics 8.02, Electricity & Magnetism, ch. 4, p. 13-15, 2004, url <https://web.mit.edu/8.02t/www/802TEAL3D/visualizations/coursenotes/index.htm> [20210217].
2. <a name="ref2"></a>Hanna Pamula, "Angle Between Two Vectors Calculator", Omni Calculator, 21 Jan 2021, url <https://www.omnicalculator.com/math/angle-between-two-vectors> [20210218].
3. <a name="ref3"></a>Wikipedia contributors, "Proportionality (mathematics)", Wikipedia, The Free Encyclopedia, 10 Feb 2021, 21:37 UTC, url <https://en.wikipedia.org/w/index.php?oldid=1006068420> [20210218].
4. <a name="ref4"></a>tentaclenorm, Duck Deux, "Answer to 'Surface Element in Spherical Coordinates'", Mathematics Stack Exchange, 25 Mar 2018 at 22:40, url <https://math.stackexchange.com/a/131747> [20210218].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/fi1202/2021-02-17-electric-field-nc-solid-sphere.md)


{% comment %}
## references
1. <a name="ref1"></a>OpenStax, "6.4: Applyig Gauss's Law", Physics LibreTexts, 6 Nov 2020, url <https://phys.libretexts.org/Bookshelves/University_Physics/Book%3A_University_Physics_(OpenStax)/Map%3A_University_Physics_II_-_Thermodynamics_Electricity_and_Magnetism_(OpenStax)/06%3A_Gauss's_Law/6.04%3A_Applying_Gausss_Law> [20210216].
2. <a name="ref2"></a>Wikipedia contributors, "Gaussian surface", Wikipedia, The Free Encyclopedia, 15 Nov 2020, 22:24 UTC, url <https://en.wikipedia.org/w/index.php?oldid=988897483> [20210216].
3. <a name="ref3"></a>Carl R. Nave, "Gauss's Law", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/electric/gaulaw.html> [20210216].
4. <a name="ref4"></a>Michel van Biezen, "Physics - Gauss' Law (11 of 11) Cubic Gaussian Surface", YouTube, 12.03.2014, url <https://www.youtube.com/watch?v=MM-3sgswY9Q> [20210216].
5. <a name="ref5"></a>Wikipedia contributors, "Cubic crystal system", Wikipedia, The Free Encyclopedia, 31 Jan 2021, 02:31 UTC, url <https://en.wikipedia.org/w/index.php?oldid=1003869020> [20210216].
6. <a name="ref6"></a>Gregory Hawkins, "2.1 Basics of the Relativistic Cosmology: the Dynamics of the Universe", SlidePlayer, 2019, p. 14, url <https://slideplayer.com/slide/13942333/> [20210216].



Amount of charge enclosed by Gaussian surface is the enclosed charge [[1](#ref1), [2](#ref2)], where it can be assessed by mapping the electric field on a closed surface outside the charge distribution using Gauss's law [[3](#ref3)]. Some illustrations are given and discussed here.


## fraction, one, or multiple charges
Enclosed charge can consist of fraction of one charge, one charge, or multiple charges. It depends on the Gaussian surface that covers the charge(s).
 
{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/qenc/half-sphere-in-box.png)
<br />
Figure <a name="fig:ec-half-sphere-in-box">1</a> A charge $Q$ (left), enclosed charge $q_{\rm enc}$ is a whole charge $Q$ (center), and enclosed charge $q_{\rm enc}$ is half of the charge $\frac12 Q$.
{: refdef}

A whole charge or fraction of one charge enclosed by a Gaussian surface is given in Fig. <a href="#fig:ec-half-sphere-in-box">1</a>, where $q_{\rm enc}$ is simple part of charge that is inside the Gaussian surface (a closed surface). Result of $q_{\rm enc}$ in Fig. <a href="#fig:ec-half-sphere-in-box">1</a> (center) can be obtained using Gauss's law, indeed spherical charge distribution with cubic Gaussian surface, but you will face a very difficult integral, which is not recommended [[4](#ref4)]. We can also draw the Gaussian surfaces in illustrative way to show the concept as given in Fig. <a href="#fig:ec-qenc-surface-concept">2</a>

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/qenc/qenc-surface-concept.png)
<br />
Figure <a name="fig:ec-qenc-surface-concept">2</a> Some charges ($q_1$, $q_2$, $q_3$, $q_4$, $q_5$) and some Gaussian surfaces ($s_1$, $s_2$, $s_3$, $s_4$, $s_5$).
{: refdef}

We can have from Fig. <a href="#fig:ec-qenc-surface-concept">2</a> that enclosed charge $q_{\rm enc}$ by Gaussian surface $s_3$ (green dashed line) is $q_3 + q_4 = +2Q + (-Q) = +Q$. If you like to have a 3-d Gaussian surface, again a cubic surface, but with a real problem, let us take the Fig. <a href="#fig:ec-cell-sc-bcc">3</a> as example.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/qenc/cell-sc-bcc.png)
<br />
Figure <a name="fig:ec-cell-sc-bcc">3</a> Two varieties of the cubic crystal system: simple cubic (left) and body-centered cubic (right).
{: refdef}

In cubic crystal system there are simple cubic (SC) and body-centered cubic (BCC), whichh area two of three main varieties of the cubic crystal system [[5](#ref5)]. If each single sphere represents a charge $Q$ then in the SC we can have that $q_{\rm enc} = Q$ with cubic Gaussian surface as shown in previous figure. Can you see that?


## spherical charge distribution
By choosing a homogeneous and isotropic material [[6](#ref6)] we will illustrate the enclosed charge $q_{\rm enc}$ from a spherical charge distribution when we use a spherical Gaussian surface. Two system are discussed, which are solid and hollow spheres.

### solid sphere
{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/qenc/sphere-in-sphere.png)
<br />
Figure <a name="fig:ec-sphere-in-sphere">4</a> Spherial Gaussian surface of a spherical charge distribution.
{: refdef}

Enclosed charge of the system is

\begin{equation}
\label{eqn:ec-solid-sphere-homogeneous-isotropic}
q_{\rm enc} = \left\\{
\begin{array}{lr}
\displaystyle \left( \frac{r^3}{R^3} \right) Q, & 0 \le r \le R, \newline
Q, & R < r,
\end{array}
\right.,
\end{equation}

where $r$ is radius of the spherical Gaussian surface and $R$ is radius of the sphere.

### hollow sphere
{:refdef: style="text-align: center;"}
![..](/assets/img/phys/electrostatics/qenc/hollow-sphere-in-sphere.png)
<br />
Figure <a name="fig:ec-hollow-sphere-in-sphere">5</a> Spherial Gaussian surface for charge distribution of hollow sphere.
{: refdef}

For this system the enclosed charge is

\begin{equation}
\label{eqn:ec-hollow-sphere-homogeneous-isotropic}
q_{\rm enc} = \left\\{
\begin{array}{lr}
0, & 0 \le r < R_1, \newline
\displaystyle \left( \frac{r^3 - R_1^3}{R_2^3 - R_1^3} \right) Q, & R_1 \le r \le R_2, \newline
Q, & R < r,
\end{array}
\right.,
\end{equation}

where $r$ is radius of the spherical Gaussian surface, $R_1$ and $R_2$ are inner and outter radii of the hollow sphere, respectively.

### formulation
Enclosed charge can obtained using

\begin{equation}
\label{eqn:ec-enclosed-charge}
q_{\rm enc} = \int \rho dV = \int \rho(r) \ r^2 dr \int \sin\theta d\theta \int d\varphi = 4\pi \int \rho(r) \ r^2 dr,
\end{equation}

where $\rho = \rho(r)$ is volume charge density, which can be function of radius $r$. Then for solid sphere 

\begin{equation}
\label{eqn:ec-solid-sphere-homogeneous-isotropic-rho}
\rho(r) = \left\\{
\begin{array}{lr}
\displaystyle \frac{Q}{V}, & 0 \le r \le R, \newline
0, & R < r,
\end{array}
\right.,
\end{equation}

while for hollow sphere

\begin{equation}
\label{eqn:ec-hollow-sphere-homogeneous-isotropic-rho}
\rho(r) = \left\\{
\begin{array}{lr}
0, & 0 \le r < R_1, \newline
\displaystyle \frac{3Q}{4\pi (R_2^3 - R_1^3)}, & R_1 \le r \le R_2, \newline
0, & R < r,
\end{array}
\right.,
\end{equation}

with $r$, $R$, $R_1$, and $R_2$ as in Eqns. \eqref{eqn:ec-solid-sphere-homogeneous-isotropic} and \eqref{eqn:ec-hollow-sphere-homogeneous-isotropic}.


## exercises
1. Using cubic Gaussian surface in Fig. <a href="#fig:ec-half-sphere-in-box">1</a>, where is the position of the sphere to get $q_{\rm enc} = \frac18 Q$ exactly? Explain in brief.
2. Why is it not recommended to get the enclosed charge $q_{\rm enc}$ in Fig. <a href="#fig:ec-half-sphere-in-box">1</a> (center) using a cubic Gaussian surface? See [[4](#ref4)] if necessary to find the answer.
3. From Fig. <a href="#fig:ec-qenc-surface-concept">2</a> find enclosed charge $q_{\rm enc}$ for Gaussian surface $s_1$ and $s_4$. Show how you come the the answers.
4. Find the $q_{\rm enc}$ for BCC in Fig. <a href="#fig:ec-cell-sc-bcc">3</a> (right) with the given cubic Gaussian surface. Explain why you give the answer.
5. Show how to obtain Eqn. \eqref{eqn:ec-solid-sphere-homogeneous-isotropic-rho} using Eqn. \eqref{eqn:ec-enclosed-charge}.
6. Using Eqn. \eqref{eqn:ec-enclosed-charge}, try to derive Eqn. \eqref{eqn:ec-hollow-sphere-homogeneous-isotropic-rho}.
7. In Eqns. Eqn. \eqref{eqn:ec-solid-sphere-homogeneous-isotropic-rho} and Eqn. \eqref{eqn:ec-hollow-sphere-homogeneous-isotropic-rho} how the relation between radius range, e.g. $0 \le r \le R$ and lower and upper bounds of the integral? Explain in brief.
8. How do you obtain the factor $Q/V$ in Eqn. \eqref{eqn:ec-solid-sphere-homogeneous-isotropic-rho}?
9. In Eqn. \eqref{eqn:ec-hollow-sphere-homogeneous-isotropic-rho} there is a factor $\frac{3Q}{4\pi (R_2^3 - R_1^3)}$. Explain how to produce it.
10. Why are $\rho = 0$ out of the spherical systems in Figs. <a href="#fig:ec-solid-sphere-in-sphere">4</a> and <a href="#fig:ec-hollow-sphere-in-sphere">5</a>?

## references
1. <a name="ref1"></a>OpenStax, "6.4: Applyig Gauss's Law", Physics LibreTexts, 6 Nov 2020, url <https://phys.libretexts.org/Bookshelves/University_Physics/Book%3A_University_Physics_(OpenStax)/Map%3A_University_Physics_II_-_Thermodynamics_Electricity_and_Magnetism_(OpenStax)/06%3A_Gauss's_Law/6.04%3A_Applying_Gausss_Law> [20210216].
2. <a name="ref2"></a>Wikipedia contributors, "Gaussian surface", Wikipedia, The Free Encyclopedia, 15 Nov 2020, 22:24 UTC, url <https://en.wikipedia.org/w/index.php?oldid=988897483> [20210216].
3. <a name="ref3"></a>Carl R. Nave, "Gauss's Law", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/electric/gaulaw.html> [20210216].
4. <a name="ref4"></a>Michel van Biezen, "Physics - Gauss' Law (11 of 11) Cubic Gaussian Surface", YouTube, 12.03.2014, url <https://www.youtube.com/watch?v=MM-3sgswY9Q> [20210216].
5. <a name="ref5"></a>Wikipedia contributors, "Cubic crystal system", Wikipedia, The Free Encyclopedia, 31 Jan 2021, 02:31 UTC, url <https://en.wikipedia.org/w/index.php?oldid=1003869020> [20210216].
6. <a name="ref6"></a>Gregory Hawkins, "2.1 Basics of the Relativistic Cosmology: the Dynamics of the Universe", SlidePlayer, 2019, p. 14, url <https://slideplayer.com/slide/13942333/> [20210216].

{% endcomment %}
