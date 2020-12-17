---
layout: post
author: viridi
title: carnot cycle
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["cycle", "thermodynamics", "efficiency", "engine"]
date: 2020-12-17 11:11:00 +07
permalink: /physics/carnot-cycle
---
In heat engines Carnot cycle is an ideal cyclical sequence of changes of pressure and temperature of a fluid, which is used as a standard of performance of all heat enginges operating between a high and a low temperature [[1](#ref1)]. It is only a theoretical construct since it is not an actual thermodynamic cycle, but it provides upper limit on the efficiency that any classical thermodynamic engine can achieve during the conversion of heat into work [[2](#ref2)]. This cycle concept is related to other concepts in thermodynamics, e.g isothermal and adiabatic processes, second law of thermodynamics, entropy, etc [[3](#ref3)].


## Cycle in p-V diagram
Ideal gas performing a Carnot cycle is shown in Fig. <a href="#fig:carnotc-carnot-cycle">1</a>, where therea are four points and four processes connecting the two sequential points in the cycle ($1 \rightarrow 2 \rightarrow 3 \rightarrow 4 \rightarrow 1$).

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/thermodynamics/carnot-cycle.png)
<br />
Figure <a name="fig:carnotc-carnot-cycle">1</a> A Carnot cycle consists of isothermal expansion, adiabatic expansion, isothermal compression, and adiabatic compression processes.
{: refdef}

Thera are isothermal and adiabatic processes during gas expansion and compression, where $1 \rightarrow 2$ is an isothermal expansion process, $2 \rightarrow 3$ is an adiabatic expansion process, $3 \rightarrow 4$ is an isothermal compression process, and $4 \rightarrow 1$ is an adiabatic compression process.


## Relation between states
Each point in $p-V$ diagram is a state of the ideal gas. Since the gas obeys ideal gas law

\begin{equation}
\label{eqn:carnotc-ideal-gas-law}
pV = nRT,
\end{equation}

where for isothermal process

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-isothermal}
pV = {\rm const}
\end{equation}

holds and for adiabatic process

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-adiabatic}
pV^\gamma = {\rm const}
\end{equation}

holds. Note that the ${\rm const}$ in Eqns. \eqref{eqn:carnotc-ideal-gas-law-isothermal} and \eqref{eqn:carnotc-ideal-gas-law-adiabatic} are different. Using the last two equations following table can be created to relate two different states belong to a same process.

**State** | $p$ | $V$ | $T$ | **Relation(s) to other state**
1 | $p_1$ | $V_1$ | $T_1$ | $T_1 = T_2$, &nbsp; $p_1 V_1 = p_2 V_2$ &nbsp; $p_1 V_1^\gamma = p_4 V_4^\gamma$
2 | $p_2$ | $V_2$ | $T_2$ | $T_2 = T_1$, &nbsp; $p_2 V_2 = p_1 V_1$, &nbsp; $p_2 V_2^\gamma = p_3 V_3^\gamma$
3 | $p_3$ | $V_3$ | $T_3$ | $T_3 = T_4$, &nbsp; $p_3 V_3 = p_4 V_4$ &nbsp; $p_3 V_3^\gamma = p_2 V_2^\gamma$
4 | $p_4$ | $V_4$ | $T_4$ | $T_4 = T_3$, &nbsp; $p_4 V_4 = p_3 V_3$ &nbsp; $p_4 V_4^\gamma = p_1 V_1^\gamma$

Last column of the previous table is obtained using Eqns. \eqref{eqn:carnotc-ideal-gas-law-isothermal} and \eqref{eqn:carnotc-ideal-gas-law-adiabatic}.


## Work
For the isothermal process, which is $1 \rightarrow 2$ and $3 \rightarrow 4$ processes in Fig. <a href="#fig:carnotc-carnot-cycle">1</a>, the work of gas is

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-isothermal-work}
W_{i \rightarrow f} = nRT \ln \left( \frac{V_f}{V_i} \right),
\end{equation}

where $i$ is for initial state and $f$ for final state, e.g. for $4 \rightarrow `$ process $i = 4$ and $f = 1$. And for adiabatic process, the work is

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-adiabatic-work}
W_{i \rightarrow f} = \frac{c_0}{1 - \gamma} \left(V_f^{1-\gamma} - V_i^{1-\gamma} \right) = \frac{nR}{1-\gamma} (T_f - T_i).
\end{equation}

with $c_0 = nRTV^{\gamma - 1}$. And for monoatomic gas $\gamma = 5/3$ since $C_p = \frac52 R$ and $C_V = \frac32 R$.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/thermodynamics/carnot-cycle-work-isothermal-expansion.png)
<br />
Figure <a name="fig:carnotc-carnot-cycle-work-isothermal-expansion">2</a>..
{: refdef}

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/thermodynamics/carnot-cycle-work-adiabatic-expansion.png)
<br />
Figure <a name="fig:carnotc-carnot-cycle-work-adiabatic-expansion">3</a>..
{: refdef}

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/thermodynamics/carnot-cycle-work-isothermal-compression.png)
<br />
Figure <a name="fig:carnotc-carnot-cycle-work-isothermal-compression">4</a>..
{: refdef}

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/thermodynamics/carnot-cycle-work-adiabatic-compression.png)
<br />
Figure <a name="fig:carnotc-carnot-cycle-work-adiabatic-compression">5</a>..
{: refdef}

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/thermodynamics/carnot-cycle-work-total.png)
<br />
Figure <a name="fig:carnotc-carnot-cycle-work-total">6</a>..
{: refdef}


## Change in internal energy
An ideal gas for any process will have change in internal energy

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-adiabatic-DU}
\Delta U_{i \rightarrow f} = \frac32 nR(T_f - T_i),
\end{equation}

which depends only on final and initial temperatures and does not depend on the trajectory of the process in $p-V$ diagram.


## Heat
For isobaric process heat can be obtained through

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-heat-isobaric}
Q_{i \rightarrow f} = C_p n (T_f - T_i)
\end{equation}

for isochoric (isovolume) process through

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-heat-isochoric}
Q_{i \rightarrow f} = C_V n (T_f - T_i)
\end{equation}

and for other process the first law

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-heat-first-law}
Q = \Delta U + W
\end{equation}

can be used to get the heat.


## References
1. <a name="ref1"></a>The Editors of Encyclopaedia Britannica, Gloria Lotha, Deepti Mahajan, Emily Rodiquez, "Carnot cycle", Encyclopædia Britannica, 27 Jul 2018, url <https://www.britannica.com/science/Carnot-cycle> [20201217].
2. <a name="ref2"></a>Wikipedia contributors, "Kinetic theory of gases", Wikipedia, The Free Encyclopedia, 2 Dec 2020, 21:15 UTC, url <https://en.wikipedia.org/w/index.php?oldid=991982665> [20201217].
3. <a name="ref3"></a>Carl R. Nave, "Kinetic Theory", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/thermo/carnotcon.html> [20201217].
4. <a name="ref4"></a>-, "What are PV diagrams?", Khan Academy, url <https://www.khanacademy.org/science/physics/thermodynamics/laws-of-thermodynamics/a/what-are-pv-diagrams> [20201217].
5. <a name="ref5"></a>Narlin Beaty, "Carnot Engine Practice Problem", GeoGebra, 8 Sep 2016, url <https://www.geogebra.org/m/vyXcfAKS> [20201217].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-12-17-carnot-cycle.md)

{% comment %}
Fig. <a href="#fig:x">1</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/x.png)
<br />
Figure <a name="fig:x">1</a> ...
{: refdef}
{% endcomment %}
