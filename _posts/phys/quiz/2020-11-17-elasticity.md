---
layout: post
author: viridi
title: elasticity
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: ["elasticity", "young modulus", "shear modulus", "bulk modulus"]
date: 2020-11-17 13:06:00 +07
permalink: /physics/quiz/elasticity
---
Examples of elasticity are discussed here.


## P01
Young's modulus $E$ is defined as ratio of stress $\sigma$ to strain $\varepsilon$

\begin{equation}
\label{eq:qelas-young-modulus}
E = \frac{\sigma}{\varepsilon}
\end{equation}

where stress is

\begin{equation}
\label{eq:qelas-young-modulus-stress}
\sigma = \frac{F}{A}
\end{equation}

and strain is

\begin{equation}
\label{eq:qelas-young-modulus-strain}
\varepsilon = \frac{\Delta L}{L},
\end{equation}

which turns Eqn. \eqref{eq:qelas-young-modulus} to

\begin{equation}
\label{eq:qelas-young-modulus-2}
E = \frac{F/A}{\Delta L / L} = \frac{FL}{A\Delta L}.
\end{equation}

In the stress-strain graph Young's modulus is the gradient of the curve in the elastic region.

**Question** Using the table provided in [[1](#ref1)] draw illustratively in a $\sigma-\varepsilon$ graph the elastic region of steel (solid line -----), glass (dashed line - - -), concerete (dotted line $\cdots$), and wood (dotted-dashed line $-\cdot-\cdot-$).


## P02
Shear modulus is defined as

\begin{equation}
\label{eq:qelas-shear-modulus}
G = \frac{F/A}{\Delta x / L},
\end{equation}

as illustrated in [[2](#ref2)], where $F/A$ is shear stress, $\Delta x$ is transverse displacement, and $L$ is initial length. Notice that $F$ paralel to the surface $A$ in shear modulus, while in Young's modulus $F$ is perpendicular to $A$. Instead of $G$, we can also use $S$ for shear modulus [[3](#ref3)]. In [[4](#ref4)] people use the configuration of quad shear test specimen to measure the shear modulus of GC1280 polyurethane compound.

**Question** Explain why the quad shear test method is chosen for finding the shear modulus of the GC1280 polyurethane compound? Write also the constant quantities provided from the measurement setup to be used in Eqn. \eqref{eq:qelas-shear-modulus} for dinding the shear modulus.
{% comment %} Answer: The quad shear test method is chosen because it subjects the polyurethane to only shear loading. {% endcomment %}


## P03
See the tutorial on how to perform an experiment to measure Young's modulus of a wire [[5](#ref5)].

**Question** Make a quantitative graph of stress $\sigma$ againts strain $\varepsilon$ and determine the gradient to get the Young's modulus. Compare the result with provided illustrative graph from the video.


## P04
..


## References
1. <a name="ref1"></a>Carl R. Nave, "Young's Modulus", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/permot3.html#c2> [20201117].
2. <a name="ref2"></a>Wikipedia contributors, "Shear modulus", Wikipedia, The Free Encyclopedia, 6 Jul 2020, 19:11 UTC, <https://en.wikipedia.org/w/index.php?oldid=966374343> [20201117].
3. <a name="ref3"></a>Vatche Deyirmenjian, David Harrison (eds.), "Shear Modulus", First Year Physics Laboratory, University of Toronto, 2 Mar 2020, url <https://faraday.physics.utoronto.ca/IYearLab/WilberforceRefShear4of8.pdf> [20201117].
4. <a name="ref4"></a>Gallagher Corporation, "Determining the Shear Modulus of Polyurethane \| Gallagher Corporation", YouTube, 03.02.2015, url <https://www.youtube.com/watch?v=TSXDdyvJ_uc> [20201117].
5. <a name="ref5"></a>amritacreate, "Young's Modulus - MeitY OLabs", YouTube, 06.02.2017, url <https://www.youtube.com/watch?v=50VYcOryCXo> [20201117].


## Note
There is not any note for now.


{% comment %}
Fig. <a href="#fig:vec-arrow-1">1</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/imp-force-01.png)
<br />
Figure <a name="fig:qmi-imp-force-01">2</a> Force given between $0.01 \ \rm s$ and $0.03 \ \rm s$..
{: refdef}
{% endcomment %}
