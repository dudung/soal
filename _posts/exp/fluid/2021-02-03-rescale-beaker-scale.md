---
layout: post
author: viridi
title: rescale beaker capacity scale
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["experiment", "", "", ""]
date: 2021-02-03 21:08:00 +07
permalink: /exp/fluid/rescale-beaker-scale
---
We can use a beaker [[1](#ref1)] or a graduated cylinder [[2](#ref2)] to measure fluid volume, where the former has accuracy about 10 percent, while the later about 1 percent of the full scale [[3](#ref3)]. There is procedure to calibrate small volumetric laboratory glassware [[4](#ref4)].


## capacity scale
On a beaker capacity scale normally begins at some distance that is not so near the bottom due to rounded corner of the bottom. It is like the profile of quarter round but for the bottom [[5](#ref5)].

{:refdef: style="text-align: center;"}
![..](/assets/img/exp/fluid/becker-glass-nonlinear-scale.png)
<br />
Figure <a name="fig:rbs-beaker-scale-same-volume">1</a> Capacity scale of a beaker can have non-linear scale due to curved bottom.
{: refdef}

To design capacity scale indicating the same volume starts from the bottom we can fill the container, e.g. beaker, with a certain volume of fluid using a graduated cylinder or other volumetric measurement apparatus as in Fig. <a href="#fig:rbs-beaker-scale-same-volume">1</a> (right). Using the volume $V$ as a unit we can draw our capacity scale right from the bottom of any container. From previous figure we can have that

\begin{equation}
\label{eqn:rbs-height-y}
y_1 - y_0 > y_2 - y_1 > y_3 - y_2 = y_4 - y_3 = \dots = y_{14} - y_{13},
\end{equation}

but the every volume between two successive lines are always the same with value $V$.


## notes
+ It was a direction for [Hoshea](https://github.com/hoshea314) after discussion with [Rizqie Arbie](https://github.com/rizqie-arbie) and [me](https://github.com/dudung).
+ An idea came up due to parallex error, which can be avoided by placing observer eyes at the level of appropriate measurement marking [[6](#ref6)]. Unfortunately it can not be performed since fluid height keeps changing while position of the recording apparatus remains at the same vertical position as in the recorded video. Analysis of the form of fluid surface in the beaker might be interested since it will evolve from ellipse to line and back to ellipse


## References
1. <a name="ref1"></a>Wikipedia contributors, "Beaker (laboratory equipment)", Wikipedia, The Free Encyclopedia, 30 Dec 2020, 12:34 UTC, url <https://en.wikipedia.org/w/index.php?oldid=997197950> [20210203].
2. <a name="ref2"></a>Wikipedia contributors, "Graduated cylinder", Wikipedia, The Free Encyclopedia, 24 Dec 2020, 22:37 UTC, url <https://en.wikipedia.org/w/index.php?oldid=996167490> [20210203].
3. <a name="ref3"></a>Kari Wolfe, "The Difference Between a Beaker & a Graduated Cylinder". Sciencing, 13 Mar 2018, url <https://sciencing.com/difference-between-beaker-graduated-cylinder-5581202.html> [20210203].
4. <a name="ref4"></a>Josephine Lembeck, "The Calibration of Small Volumetric Laboratory Glassware", NBSIR 74-461, Institute for Basic Standards, National Bureau of Standards, Washington, D.C. 20234, Dec 1974, url <https://www.nist.gov/system/files/documents/calibrations/74-461.pdf> [20210203].
5. <a name="ref5"></a>-, "Countertop Edge Profiles", Arkadia Surfaces, Annapolis, url <https://www.arkadiasurfaces.com/services/edge-profiles/> [20210203].
6. <a name="ref6"></a>Karl Wallulis, "How to Prevent Parallax Error", Sciencing, 30 April 2018, url <https://sciencing.com/prevent-parallax-error-10000073.html> [20210203].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/exp/fluid/2021-02-03-rescale-beaker-scale.md)
