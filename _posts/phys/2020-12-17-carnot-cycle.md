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

### Isothermal expansion process
Process $1 \rightarrow 2$ is a isothermal expansion process, where the work in this process is shown in Fig. <a href="#fig:carnotc-carnot-cycle-work-isothermal-expansion">2</a> as area shaded with gray parallel lines.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/thermodynamics/carnot-cycle-work-isothermal-expansion.png)
<br />
Figure <a name="fig:carnotc-carnot-cycle-work-isothermal-expansion">2</a> Isothermal expansion process as part of a Carnot cycle.
{: refdef}

Using Eqn. \eqref{eqn:carnotc-ideal-gas-law-isothermal-work} we can have

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-work-isothermal-expansion}
W_{1 \rightarrow 2} = nRT_1 \ln \left( \frac{V_2}{V_1} \right),
\end{equation}

which gives positive value since $V_2 > V_1$.

### Adiabatic expansion process
Process $2 \rightarrow 3$ is a adiabatic expansion process, where the work in this process is shown in Fig. <a href="#fig:carnotc-carnot-cycle-work-adiabatic-expansion">3</a> as area shaded with gray parallel lines.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/thermodynamics/carnot-cycle-work-adiabatic-expansion.png)
<br />
Figure <a name="fig:carnotc-carnot-cycle-work-adiabatic-expansion">3</a> Adiabatic expansion process as part of a Carnot cycle.
{: refdef}

Using Eqn. \eqref{eqn:carnotc-ideal-gas-law-adiabatic-work} we can have

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-work-adiabatic-expansion}
W_{2 \rightarrow 3} = \frac{nR}{1-\gamma} (T_3 - T_2),
\end{equation}

which gives positive value since $T_3 < T_2$  and $\gamma > 1$. For monoatomic gas \eqref{eqn:carnotc-ideal-gas-law-work-adiabatic-expansion} will become

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-work-adiabatic-expansion-2}
W_{2 \rightarrow 3} = -\frac32 nR (T_3 - T_2),
\end{equation}

since $\gamma = 5/3$.

### Isothermal compression process
Process $3 \rightarrow 4$ is a isothermal compression process, where the work in this process is shown in Fig. <a href="#fig:carnotc-carnot-cycle-work-isothermal-compression">4</a> as area shaded with gray parallel lines.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/thermodynamics/carnot-cycle-work-isothermal-compression.png)
<br />
Figure <a name="fig:carnotc-carnot-cycle-work-isothermal-compression">4</a> Isothermal compression process as part of a Carnot cycle.
{: refdef}

Using Eqn. \eqref{eqn:carnotc-ideal-gas-law-isothermal-work} we can have

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-work-isothermal-compression}
W_{3 \rightarrow 4} = nRT_3 \ln \left( \frac{V_4}{V_3} \right),
\end{equation}

which gives negative value since $V_4 < V_3$.

### Adiabatic compression process
Process $4 \rightarrow 1$ is a adiabatic compression process, where the work in this process is shown in Fig. <a href="#fig:carnotc-carnot-cycle-work-adiabatic-compression">5</a> as area shaded with gray parallel lines.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/thermodynamics/carnot-cycle-work-adiabatic-compression.png)
<br />
Figure <a name="fig:carnotc-carnot-cycle-work-adiabatic-compression">5</a> Adiabatic compression process as part of a Carnot cycle.
{: refdef}

Using Eqn. \eqref{eqn:carnotc-ideal-gas-law-adiabatic-work} we can have

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-work-adiabatic-compression}
W_{4 \rightarrow 1} = \frac{nR}{1-\gamma} (T_1 - T_4),
\end{equation}

which gives positive value since $T_1 > T_4$  and $\gamma > 1$. For monoatomic gas \eqref{eqn:carnotc-ideal-gas-law-work-adiabatic-compression} will become

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-work-adiabatic-compression-2}
W_{4 \rightarrow 1} = -\frac32 nR (T_1 - T_4),
\end{equation}

since $\gamma = 5/3$.

### Closed cycle
When previous work is summed up, then total work for the cycle is obtained as shown Fig. <a href="#fig:carnotc-carnot-cycle-work-total">6</a> as area shaded shaded with gray parallel lines.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/thermodynamics/carnot-cycle-work-total.png)
<br />
Figure <a name="fig:carnotc-carnot-cycle-work-total">6</a> Total work of a Carnot cycle.
{: refdef}

The total work is

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-work-total}
W_{\rm closed \ cycle} = W_{1 \rightarrow 2} + W_{2 \rightarrow 3} + W_{3 \rightarrow 4} + W_{4 \rightarrow 1},
\end{equation}

where each terms in the right side of Eqn. \eqref{eqn:carnotc-ideal-gas-law-work-total} are from Eqns. \eqref{eqn:carnotc-ideal-gas-law-work-isothermal-expansion}, \eqref{eqn:carnotc-ideal-gas-law-work-adiabatic-expansion}, \eqref{eqn:carnotc-ideal-gas-law-work-isothermal-compression}, and \eqref{eqn:carnotc-ideal-gas-law-work-adiabatic-compression}.


## Change in internal energy
An ideal gas for any process will have change in internal energy

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-DU}
\Delta U_{i \rightarrow f} = \frac32 nR(T_f - T_i),
\end{equation}

which depends only on final and initial temperatures and does not depend on the trajectory of the process in $p-V$ diagram. Using Eqn. \eqref{eqn:carnotc-ideal-gas-law-DU} we can have $\Delta U$ for all processes.

### Isothermal expansion process
\begin{equation}
\label{eqn:carnotc-ideal-gas-law-DU-1->2}
\Delta U_{1 \rightarrow 2} = 0,
\end{equation}

### Adiabatic expansion process
\begin{equation}
\label{eqn:carnotc-ideal-gas-law-DU-2->3}
\Delta U_{2 \rightarrow 3} = \frac32 nR(T_3 - T_2),
\end{equation}

### Isothermal compression process
\begin{equation}
\label{eqn:carnotc-ideal-gas-law-DU-3->4}
\Delta U_{3 \rightarrow 4} = 0,
\end{equation}

### Adiabatic compression process
\begin{equation}
\label{eqn:carnotc-ideal-gas-law-DU-4->1}
\Delta U_{4 \rightarrow 1} = \frac32 nR(T_1 - T_4).
\end{equation}

Eqns. \eqref{eqn:carnotc-ideal-gas-law-DU-1->2} and \eqref{eqn:carnotc-ideal-gas-law-DU-3->4} are zero since $T_2 = T_1$ and $T_4 = T_3$.


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

and for other process the first law of thermodynamics

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-heat-first-law}
Q = \Delta U + W
\end{equation}

can be used to get the heat. Since in Carnot cycle there is not any isobaric and isochoric processes, then we can only use Eqn. \eqref{eqn:carnotc-ideal-gas-law-heat-first-law} for calculating $Q$ for every process.

### Isothermal expansion process
Substitution of Eqns. \eqref{eqn:carnotc-ideal-gas-law-work-isothermal-expansion} and \eqref{eqn:carnotc-ideal-gas-law-DU-1->2} into Eqn. \eqref{eqn:carnotc-ideal-gas-law-heat-first-law} will produce

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-heat-first-law-1->2}
Q_{1 \rightarrow 2} = \Delta U_{1 \rightarrow 2} + W_{1 \rightarrow 2} = 0 + nRT \ln \left( \frac{V_2}{V_1} \right) = nRT \ln \left( \frac{V_2}{V_1} \right),
\end{equation}

which has positive value since $V_2 > V_1$.

### Adiabatic expansion process
Substitution of Eqns. \eqref{eqn:carnotc-ideal-gas-law-work-adiabatic-expansion} and \eqref{eqn:carnotc-ideal-gas-law-DU-2->3} into Eqn. \eqref{eqn:carnotc-ideal-gas-law-heat-first-law} will produce

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-heat-first-law-2->3}
Q_{2 \rightarrow 3} = \Delta U_{2 \rightarrow 3} + W_{2 \rightarrow 3} = -\frac32 nR (T_3 - T_2) + \frac32 nR(T_3 - T_2) = 0,
\end{equation}

which holds for every adiabatic process, that is $Q = 0$.

### Isothermal compression process
Substitution of Eqns. \eqref{eqn:carnotc-ideal-gas-law-work-isothermal-compression} and \eqref{eqn:carnotc-ideal-gas-law-DU-3->4} into Eqn. \eqref{eqn:carnotc-ideal-gas-law-heat-first-law} will produce

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-heat-first-law-3->4}
Q_{3 \rightarrow 4} = \Delta U_{3 \rightarrow 4} + W_{3 \rightarrow 4} = 0 + nRT \ln \left( \frac{V_4}{V_3} \right) = nRT \ln \left( \frac{V_4}{V_3} \right),
\end{equation}

which has negative value since $V_4 < V_3$.

### Adiabatic compression process
We can directly say that

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-heat-first-law-4->1}
Q_{4 \rightarrow 1} = 0,
\end{equation}

since it is an adiabatic process. Or Substitution of Eqns. \eqref{eqn:carnotc-ideal-gas-law-work-adiabatic-compression} and \eqref{eqn:carnotc-ideal-gas-law-DU-4->1} into Eqn. \eqref{eqn:carnotc-ideal-gas-law-heat-first-law} will produce

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-heat-first-law-4->1-2}
Q_{4 \rightarrow 1} = \Delta U_{4 \rightarrow 1} + W_{4 \rightarrow 1} = \frac32 nR (T_1 - T_4) - \frac32 nR(T_1 - T_4) = 0
\end{equation}

as in Eqn. \eqref{eqn:carnotc-ideal-gas-law-heat-first-law-2->3}.


## Closed cycle table
Value of change in internal energy $\Delta U$, heat $Q$, and work $W$ for all processes can put in table as follow.

**Process** | **Name** | $\Delta U$ | $Q$ | $W$
$1 \rightarrow 2$ | isothermal expansion | $0$ \eqref{eqn:carnotc-ideal-gas-law-DU-1->2} | $nRT_1 \ln \left( \frac{V_2}{V_1} \right)$ \eqref{eqn:carnotc-ideal-gas-law-heat-first-law-1->2} | $nRT_1 \ln \left( \frac{V_2}{V_1} \right)$ \eqref{eqn:carnotc-ideal-gas-law-work-isothermal-expansion}
$2 \rightarrow 3$ | adiabatic expansion | $\frac32 nR(T_3 - T_2)$ \eqref{eqn:carnotc-ideal-gas-law-DU-2->3} | $0$ \eqref{eqn:carnotc-ideal-gas-law-heat-first-law-2->3} | $-\frac32 nR (T_3 - T_2)$ \eqref{eqn:carnotc-ideal-gas-law-work-adiabatic-expansion}
$3 \rightarrow 4$ | isothermal compression | $0$  \eqref{eqn:carnotc-ideal-gas-law-DU-3->4} | $nRT_3 \ln \left( \frac{V_4}{V_3} \right)$ \eqref{eqn:carnotc-ideal-gas-law-heat-first-law-3->4} | $nRT_3 \ln \left( \frac{V_4}{V_3} \right)$ \eqref{eqn:carnotc-ideal-gas-law-work-isothermal-compression}
$4 \rightarrow 1$ | adiabatic compression | $\frac32 nR(T_1 - T_4)$ \eqref{eqn:carnotc-ideal-gas-law-DU-4->1} | $0$ \eqref{eqn:carnotc-ideal-gas-law-heat-first-law-4->1-2} | $-\frac32 nR (T_1 - T_4)$ \eqref{eqn:carnotc-ideal-gas-law-work-adiabatic-compression-2}
$1 \rightarrow 2$ $\rightarrow 3$ $\rightarrow 4$ $\rightarrow 1$ | **Total** | 0 | $nRT_1 \ln \left( \frac{V_2}{V_1} \right)$ + $nRT_3 \ln \left( \frac{V_4}{V_3} \right)$ | $nRT_1 \ln \left( \frac{V_2}{V_1} \right)$ + $nRT_3 \ln \left( \frac{V_4}{V_3} \right)$
 
Note that in every row Eqn. \eqref{eqn:carnotc-ideal-gas-law-heat-first-law} always holds.


## Efficiency
Carnot cycle is a heat engine with efficiency defined as

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-efficiency}
\eta = \frac{W}{|Q_H|} = \frac{|Q_H| - |Q_C|}{|Q_H|} = 1 - \left| \frac{Q_C}{Q_H} \right|
\end{equation}

where hot temperature $T_H = T_1 = T_2$ and cold temperature $T_C = T_3 = T_4$. From Eqn. \eqref{eqn:carnotc-ideal-gas-law-heat-first-law-1->2} and \eqref{eqn:carnotc-ideal-gas-law-heat-first-law-3->4} we can have

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-heat-first-law-1->2-QH}
|Q_H| = Q_H = nRT_H \ln \left( \frac{V_2}{V_1} \right)
\end{equation}

since $V_2 > V_1$

and

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-heat-first-law-3->4-QC}
|Q_C| = -Q_C = -nRT_C \ln \left( \frac{V_4}{V_3} \right) = nRT_C \ln \left( \frac{V_3}{V_4} \right)
\end{equation}

since $V_4 < V_3$. Substitution of Eqns. \eqref{eqn:carnotc-ideal-gas-law-heat-first-law-1->2-QH} and \eqref{eqn:carnotc-ideal-gas-law-heat-first-law-3->4-QC} into Eqn. \eqref{eqn:carnotc-ideal-gas-law-efficiency will produce

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-efficiency-2}
\eta = 1 - \frac{nRT_C \ln \left( \frac{V_3}{V_4} \right)}{nRT_H \ln \left( \frac{V_2}{V_1} \right)} = 1 - \frac{T_C}{T_H}
\end{equation}

due to Eqn. \eqref{eqn:carnotc-ideal-gas-law-adiabatic}, which holds only for Carnot cycle [[5](#ref5)].

### Proof
Using Eqn. \eqref{eqn:carnotc-ideal-gas-law-adiabatic} we can relate $V_2$ with $V_3$ and $V_4$ and $V_1$ through

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-adiabatic-2-3}
p_2 V_2^\gamma = p_3 V_3^\gamma
\end{equation}

and

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-adiabatic-4-1}
p_4 V_4^\gamma = p_1 V_1^\gamma.
\end{equation}

From Eqn. \eqref{eqn:carnotc-ideal-gas-law} we can have

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-1-2-3-4}
\frac{p_1 V_1}{T_1} = \frac{p_2 V_2}{T_2} = \frac{p_3 V_3}{T_3} = \frac{p_4 V_4}{T_4} = nR.
\end{equation}

We can rewrite

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-adiabatic-pVT}
p_i V_i^\gamma = p_i V_i V_i^{\gamma - 1},
\end{equation}

which can be implemented in Eqn. \eqref{eqn:carnotc-ideal-gas-law-adiabatic-2-3} then gives

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-adiabatic-2-3--1}
\begin{array}{rcl}
p_2 V_2 V_2^{\gamma-1} & = & p_3 V_3 V_3^{\gamma-1} \newline
\displaystyle \left( \frac{T_2}{T_3} p_3 V_3 \right) V_2^{\gamma-1} & = & p_3 V_3 V_3^{\gamma-1} \newline
\displaystyle \frac{T_2}{T_3} & = & \displaystyle \left( \frac{V_3}{V_2} \right)^{\gamma-1} \newline
\displaystyle \frac{T_H}{T_C} & = & \displaystyle \left( \frac{V_3}{V_2} \right)^{\gamma-1},
\end{array}
\end{equation}

and also implemented in Eqn. \eqref{eqn:carnotc-ideal-gas-law-adiabatic-4-1} then gives

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-adiabatic-4-1--1}
\begin{array}{rcl}
p_4 V_4 V_4^{\gamma-1} & = & p_1 V_1 V_1^{\gamma-1} \newline
\displaystyle \left( \frac{T_4}{T_1} p_1 V_1 \right) V_4^{\gamma-1} & = & p_1 V_1 V_1^{\gamma-1} \newline
\displaystyle \frac{T_4}{T_1} & = & \displaystyle \left( \frac{V_1}{V_4} \right)^{\gamma-1} \newline
\displaystyle \frac{T_C}{T_H} & = & \displaystyle \left( \frac{V_1}{V_4} \right)^{\gamma-1}.
\end{array}
\end{equation}

Multiply Eqn. \eqref{eqn:carnotc-ideal-gas-law-adiabatic-2-3--1} with Eqn. \eqref{eqn:carnotc-ideal-gas-law-adiabatic-4-1--1} will produce

\begin{equation}
\label{eqn:carnotc-ideal-gas-law-adiabatic-v1-2-3-4}
\begin{array}{rcl}
\displaystyle \left( \frac{V_3}{V_2} \right)^{\gamma-1} & = & \displaystyle \left( \frac{V_4}{V_1} \right)^{\gamma-1} \newline
\displaystyle \frac{V_3}{V_2} & = & \displaystyle \frac{V_4}{V_1} \newline
\displaystyle \frac{V_3}{V_4} & = & \displaystyle \frac{V_2}{V_1} \newline
\displaystyle \ln \left( \frac{V_3}{V_4} \right) & = & \ln \left( \displaystyle \frac{V_2}{V_1} \right).
\end{array}
\end{equation}

Substitute final line of Eqn. \eqref{eqn:carnotc-ideal-gas-law-adiabatic-v1-2-3-4} into middle side of Eqn. \eqref{eqn:carnotc-ideal-gas-law-efficiency-2} will produce the right side of Eqn. \eqref{eqn:carnotc-ideal-gas-law-efficiency-2}.


## Exercises
1. Open a web reference [[6](#ref6)], answer `Ans 1` - `Ans 8`, change the parameters $n$, $p_1$, $V_1$, $V_3$, and $V_4$, and reanswer `Ans 1` - `Ans 8` until you understand how to obtain the right answer. Section [Relation between states](#relation-between-states) will help.
2. Open a web reference [[7](#ref7)] and exercise to calculate eficiency from net work $W$, heat in $Q_H$, heat out $Q_C$ and also from higher temperature $T_H = T_1$, lower temperature $T_C = T_2$.
3. See [Carnot cyle example 1](carnot-cycle-example-1) for a numerical example.


## References
1. <a name="ref1"></a>The Editors of Encyclopaedia Britannica, Gloria Lotha, Deepti Mahajan, Emily Rodiquez, "Carnot cycle", Encyclopædia Britannica, 27 Jul 2018, url <https://www.britannica.com/science/Carnot-cycle> [20201217].
2. <a name="ref2"></a>Wikipedia contributors, "Kinetic theory of gases", Wikipedia, The Free Encyclopedia, 2 Dec 2020, 21:15 UTC, url <https://en.wikipedia.org/w/index.php?oldid=991982665> [20201217].
3. <a name="ref3"></a>Carl R. Nave, "Kinetic Theory", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/thermo/carnotcon.html> [20201217].
4. <a name="ref4"></a>-, "What are PV diagrams?", Khan Academy, url <https://www.khanacademy.org/science/physics/thermodynamics/laws-of-thermodynamics/a/what-are-pv-diagrams> [20201217].
5. <a name="ref5"></a>Carl R. Nave, "Carnot efficiency", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/thermo/carnot.html> [20201217].
6. <a name="ref6"></a>Narlin Beaty, "Carnot Engine Practice Problem", GeoGebra, 8 Sep 2016, url <https://www.geogebra.org/m/vyXcfAKS> [20201217].
7. <a name="ref7"></a>Chris Hamper, "Carnot cycle ( with energies and efficiency)", GeoGebra, 17 Jan 2015, url <https://www.geogebra.org/m/dW93FqWd> [20201217].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-12-17-carnot-cycle.md)
