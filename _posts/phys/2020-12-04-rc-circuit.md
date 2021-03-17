---
layout: post
author: viridi
title: rc circuit
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["electric circuit"]
date: 2020-12-04 18:42:00 +07
permalink: /physics/rc-circuit
---
An electronic circuit composed of resistotrs and capacitors known as RC circuit [[1](#ref1)], whose simplest one with only one resistor $R$ and one capacitor $C$ arranged in series can be used to learn the process of charging [[2](#ref2)] and discharging [[3](#ref3)] a capacitor.


## first-order circuit
The simplest circuit composed of one resistor $R$ and capacitor $C$ is named first-order RC circuit. The circuit can a first-order series RC circuit [[4](#ref4)] or a paralel one [[5](#ref5)]. Fig. <a href="#fig:rc-circuit-first-order-open">1</a> shows the series and parallel first-order RC circuits.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/circuit/rc-circuit-first-order-open.png)
<br />
Figure <a name="fig:rc-circuit-first-order-open">1</a> First order RC circuits arranged in series (left) and parallel (right), both are open.
{: refdef}

An switch $S$ is an additional component for controlling when the current flows from battery $\epsilon$ through resistor $R$ and capacitor $C$. The unit for $R$ is $\rm \Omega$ (ohm), for $\epsilon$ is $\rm V$ (volt), and for $C$ is $\rm F$ (farad).


## Series circuit
Using series RC circuit in Fig. <a href="#fig:rc-circuit-first-order-open">1</a> (left) we can charge and discharge a capacitor.

### Charging a capacitor
At time $t < 0$ it is assumed that the capacitor $C$ does not have any charge $q$ in it. Charging process starts at time $t = 0$ when the switch $S$ is close for the first time and current $I$ begins to flow from the battery $\epsilon$ and pass through the resistor $R$ and capacitor $C$. There will be sudden high value of $I$ and then it is decreasing to zero.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/circuit/rc-series-charging.png)
<br />
Figure <a name="fig:rc-series-charging">2</a> Charging a capacitor: $t < 0$ (left) and $t = 0$ (right).
{: refdef}




### Discharging a capacitor
..

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/circuit/rc-series-discharging.png)
<br />
Figure <a name="fig:rc-series-charging">3</a> Discharging a capacitor: $t < 0$ (left) and $t = 0$ (right).
{: refdef}


## References
1. <a name="ref1"></a>Wikipedia contributors, "RC circuit", Wikipedia, The Free Encyclopedia, 18 Nov 2020, 06:06 UTC, url <https://en.wikipedia.org/w/index.php?oldid=989305163> [20201204].
2. <a name="ref2"></a>Carl R. Nave, "Charging a Capacitor", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/electric/capchg.html> [20201204].
3. <a name="ref3"></a>-, "RC Discharging Circuit", Electronics Tutorial, url <https://www.electronics-tutorials.ws/rc/rc_2.html> [20201204].
4. <a name="ref3"></a>John Santiago, "Analyze a Series RC Circuit Using a Differential Equation", dummies, url <https://www.dummies.com/education/science/science-electronics/analyze-a-series-rc-circuit-using-a-differential-equation/> [20201205].
5. <a name="ref3"></a>-, "First Order Circuits", EENG223 Circuit Theory I, Eastern Mediterranean University, url <https://opencourses.emu.edu.tr/file.php/3/Lecture_Notes/First_Order_Circuits.pdf> [20201205].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-12-04-rc-circuit.md)

{% comment %}
Fig. <a href="#fig:x">1</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/x.png)
<br />
Figure <a name="fig:x">1</a> ...
{: refdef}
{% endcomment %}
