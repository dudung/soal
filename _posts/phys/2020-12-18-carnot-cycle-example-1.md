---
layout: post
author: viridi
title: carnot cycle example 1
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["cycle", "thermodynamics", "efficiency", "engine"]
date: 2020-12-18 05:33:00 +07
permalink: /physics/carnot-cycle-example-1
---
An example of [Carnot cycle](carnot-cycle) is discussed here.


## Cycle in p-V diagram
Fig. <a href="#fig:ccex1-pV-diagram-normal-scale">1</a> shows a Carnot cycle in $p-V$ diagram with normal scale.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/thermodynamics/carnot-cycle-pV-chart-normal-scale-0.png)
<br />
Figure <a name="fig:ccex1-pV-diagram-normal-scale">1</a> A Carnot cycle consists of isothermal expansion ($1 \rightarrow 2$), adiabatic expansion ($2 \rightarrow 3$), isothermal compression ($3 \rightarrow 4$), and adiabatic compression ($4 \rightarrow 1$) processes.
{: refdef}

In order to give clearer view we can have previous diagram in log scale as shown in Fig. <a href="#fig:ccex1-pV-diagram-log-scale">2</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/thermodynamics/carnot-cycle-pV-chart-log-scale-0.png)
<br />
Figure <a name="fig:ccex1-pV-diagram-log-scale">1</a> A Carnot cycle, which consists of isothermal expansion ($1 \rightarrow 2$), adiabatic expansion ($2 \rightarrow 3$), isothermal compression ($3 \rightarrow 4$), and adiabatic compression ($4 \rightarrow 1$) processes, is shown with log scale on each of the  axes.
{: refdef}

Note that Fig. <a href="#fig:ccex1-pV-diagram-normal-scale">1</a> in normal scale and with real number is not shown as in theoretical discussion in [Carnot cyle](carnot-cycle), where it has been so illustrated to give a better view in differing each of the processes.


## Problem
A monoatomic ideal gas is performing a Carnot cycle. There are four states indicated by $1$, $2$, $3$, $4$ to give coordinates in $(p, V, T)$ space as $(p_i, V_i, T_i)$ with $i = 1, 2, 3, 4$. Illustration of the cycle in $p-V$ diagram is shown in Fig <a href="#fig:ccex1-carnot-cycle">3</a>. Note that we use theoretical $p-V$ diagram for better illustration instead of Fig. <a href="#fig:ccex1-pV-diagram-normal-scale">1</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/thermodynamics/carnot-cycle.png)
<br />
Figure <a name="fig:ccex1-carnot-cycle">3</a> A Carnot cycle consists of isothermal expansion ($1 \rightarrow 2$), adiabatic expansion ($2 \rightarrow 3$), isothermal compression ($3 \rightarrow 4$), and adiabatic compression ($4 \rightarrow 1$) processes.
{: refdef}

Highest pressure in the cyle is $1.25 \times 10^6 \ {\rm N/m^2}$, lowest volume is $0.008 \ {\rm m^3}$, and highest temperature is $2000 \ \{\rm K}$, while lowest pressure in the cyle is $39.063 \times 10^3 \ {\rm N/m^2}$, highest volume is $0.512 \ {\rm m^3}$, and lowest temperature is $500 \ \{\rm K}$. Please (a) find amount of gas $n$ in $\rm mol$, (b) write equations relating two states $(p_2, V_2, T_2)$ and $(p_1, V_1, T_1)$, $(p_2, V_2, T_2)$ and $(p_3, V_3, T_3)$, $(p_4, V_4, T_4)$ and $(p_1, V_1, T_1)$, and $(p_4, V_4, T_4)$ and $(p_3, V_3, T_3)$, (c) find gas pressure $p_2$ and volume $V_2$, (d) find gas pressure $p_4$ and volume $V_4$, (e) complete the following table, and (f) calculate efficiency of the cycle.

**State** | $p \ (\rm N/m^2)$ | $V \ (\rm m^3)$ | $T \ (\rm K)$ | $pV/nRT$
$1$ | | | | 
$2$ | | | |
$3$ | | | |
$3$ | | | |

Remember that $C_p = \frac52 R$, $C_p = \frac32 R$, $\gamma = C_p / C_V$, ideal gas $pV = nRT$, isothermal process $pV = \rm const$, and adiabatic process $pV^\gamma = \rm const$. Note that last column in previous table is for checkin the results using ideal gas law.

### Short solution
Please use following information only for comfirmation your answer after you solve the problem.

```
1 1250000	0.008	2000 1  400
2 156250	0.064	2000 1 1600
3   4883	0.512	 500 1 1600
4  39063	0.064	 500 1  400
```

## Exercise
1. Try the online resources [[1](#ref1)] and [[2](#ref2)] to get another variation of states $(p_i, V_i, T_i)$ with $i = 1, 2, 3, 4$ of a Carnot cycle or the cycle efficiency.


## References
1. <a name="ref1"></a>Narlin Beaty, "Carnot Engine Practice Problem", GeoGebra, 8 Sep 2016, url <https://www.geogebra.org/m/vyXcfAKS> [20201218].
2. <a name="ref2"></a>Chris Hamper, "Carnot cycle ( with energies and efficiency)", GeoGebra, 17 Jan 2015, url <https://www.geogebra.org/m/dW93FqWd> [20201218].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-12-18-carnot-cycle-example-1.md)
