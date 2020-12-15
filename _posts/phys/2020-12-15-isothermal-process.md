---
layout: post
author: viridi
title: isothermal process
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["", "", "", ""]
date: 2020-12-15 15:47:00 +07
permalink: /physics/isothermal-process
---
In an isothermal process temperature is constant or temperature change is zero [[1](#ref1)], where for ideal gas the change in internal energy is zero during the process [[2](#ref2)].


## Process in $p-V$ diagram
Fig. <a href="#fig:isoproc-isothermal-process">1</a>. shows the isothermal process, which can be an expansion of compression, where $X_{1 \rightarrow 2}$ is a process variable from point $1$ to point $2$, e.g. work $W$, heat $Q$, or change in internal energy $\Delta U$.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/thermodynamics/isothermal-process.png)
<br />
Figure <a name="fig:isoproc-isothermal-process">1</a> Isothermal process: expansion (left) and compression (right).
{: refdef}

Expansion is when final volume is larger than initial one, where in Fig. <a href="#fig:isoproc-isothermal-process">1</a> the initial volume is $V_1$ and final volume is $V_2$, while compression is when final volume is smaller than the initial. Fig. <a href="#fig:isoproc-isothermal-process">1</a> (left) shows isothermal expansion process ($V_2 > V_1$) and the (right) shows isothermal compression process ($V_2 < V_1$).


## Ideal gas law
For an isothermal process the ideal gas law can be used to write a relation

\begin{equation}
\label{eqn:isoproc-ideal-gas-law}
pV = c_0, 
\end{equation}

where

\begin{equation}
\label{eqn:isoproc-ideal-gas-law-c0}
c_0 = nRT
\end{equation}

is a constant.

## Work done by gas
Gas performs work to its environment in the form of

\begin{equation}
\label{eqn:isoproc-ideal-gas-work-by-gas}
W = \int p dV.
\end{equation}

Substitution of Eqn. \eqref{eqn:isoproc-ideal-gas-law} into Eqn. \eqref{eqn:isoproc-ideal-gas-work-by-gas} will produce

\begin{equation}
\label{eqn:isoproc-ideal-gas-work-by-gas-p}
W = \int \frac{c_0}{V} dV = c_0 \int \frac{dV}{V} = c_0 \ln V + c_1.
\end{equation}

Substitute Eqn. \eqref{eqn:isoproc-ideal-gas-law-c0} into Eqn. {eqn:isoproc-ideal-gas-work-by-gas-p} will give

\begin{equation}
\label{eqn:isoproc-ideal-gas-work-by-gas-isothermal}
W = nRT \ln V + c_1,
\end{equation}

which is work done by ideal gas in isothermal process. Note that $c_1$ is arbitrary constant due to integration. Eqn. \eqref{eqn:isoproc-ideal-gas-work-by-gas-isothermal} in the indefinite integral $\int p(V) dV$. When we put the lower and upper limits of the integral Eqn. \eqref{eqn:isoproc-ideal-gas-work-by-gas-isothermal} will become

\begin{equation}
\label{eqn:isoproc-ideal-gas-work-by-gas-isothermal-V1-V2}
W_{1 \rightarrow 2} = nRT \ln \frac{V_2}{V_1}
\end{equation}

with $V_1$ and $V_2$ are initial anda final volumes, respectively.

### Example 1
At $400 \ {\rm K}$ a $1.2027 \ {\rm mol}$ ideal gas begins an isothermal process with initial volume $2\times10^{-2} \ {\rm m^3}$ and initial pressure $2\times10^5 \ {\rm N/m^2}$ and ends the process with final pressure $4\times10^5 \ {\rm N/m^2}$ and final volume $10^{-2} \ {\rm m^3}$.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/thermodynamics/isothermal-compression-process.png)
<br />
Figure <a name="fig:isoproc-compression-isothermal-process">1</a> Isothermal compression process with $V_2 = \frac12 V_1$, $p_2 = 2 p_1$, and $n = 1.2027 \ {\rm mol}$.
{: refdef}

Find the work during the process.

+ It is a compression process since final volume is less than initial volume.
+ Work done by gas can be calculate through
\begin{equation}
\label{eqn:isoproc-example-1-1}
\begin{array}{rcl}
W & = & \displaystyle nRT \ln \frac{V_2}{V_1} \newline
& = & \displaystyle (1.2027 \ {\rm mol}) \ (8.314 \ \rm J/mol \cdot K)(400 \ {\rm K}) \ln \left( \frac{0.01 \ {\rm m^3}}{0.02 \ {\rm m^3}} \right) \newline 
& = & -2.772 \times 10^3 \ {\rm J} \approx -2.77 \ {\rm kJ}.
\end{array}
\end{equation}
+ Negative value of work means the gas do a negative work or the work is done to the gas from the environment (increase of pressure).
+ The answer: the work during the isothermal compression process is  $-2.77 \ {\rm kJ}$.

### Example 2
A $0.2405 \ \rm mol$ ideal gas has initial pressure $10^5 \ \rm Pa$ and volume $10 \ l$. From initial state the gas performs a isothermal expansion so that the final volume will be twice the initial volume.

{:refdef: style="text-align: center;"}
![..](/assets/img/phys/thermodynamics/isothermal-expansion-process.png)
<br />
Figure <a name="fig:isoproc-expansion-isothermal-process">1</a> Isothermal expansion process with $V_2 = 2V_1$, $p_1 = 10^5 \ {\rm Pa}$, and $n = 0.2405 \ {\rm mol}$.
{: refdef}

Find (a) gas temperature, (b) gas final pressure, (c) work done by gas during the process. Use gas constant $R = 8.314 \ \rm J/mol \cdot K$.

+ Convert pressure from $\rm Pa$ to $\rm N/m^2$ and we get $p_1 = 10^5 \ {\rm Pa} \times 1 \ {\rm (N/m^2) / Pa} = 10^5 \ {\rm N/m^2}$.
+ Convert volume from $l$ to $\rm m^3$ and we get $V_1 = 10 \ l \times 10^{-3} {\rm m^3} / l = 0.01 \ {\rm m^3}$.
+ Calculate gas temperature
\begin{equation}
\label{eqn:isoproc-example-2-1}
\begin{array}{rcl}
T_1 & = & \displaystyle \frac{p_1 V_1}{n R} \newline
& = & \displaystyle \frac{(10^5 \ {\rm N/m^2}) \ (0.01 \ {\rm m^3})}{(0.2405 \ {\rm mol}) \ (8.314 \ \rm J/mol \cdot K)} \newline
& = & 500.12 \ {\rm K} \approx 500 \ {\rm K}
\end{array}
\end{equation}
and $T_2 = T_1 = 500 \ {\rm K}$ since it is an isothermal process.
+ Final volume is twice initial volume, then $V_2 = 2 V_1 = 0.02 \ {\rm m^3}$.
+ Final pressure then will be obtained through
\begin{equation}
\label{eqn:isoproc-example-2-2}
\begin{array}{rcl}
p_2 & = & \displaystyle \frac{n R T_2}{V_2} \newline
& = & \displaystyle \frac{(0.2405 \ {\rm mol}) \ (8.314 \ \rm J/mol \cdot K)(500 \ {\rm K})}{(0.02 \ {\rm m^3})} \newline 
& = & 49,987 \ {\rm N/m^2} \approx 5 \times 10^4 \ {\rm N/m^2}.
\end{array}
\end{equation}
+ Work done by gas is
\begin{equation}
\label{eqn:isoproc-example-2-3}
\begin{array}{rcl}
W & = & \displaystyle nRT \ln \frac{V_2}{V_1} \newline
& = & \displaystyle (0.2405 \ {\rm mol}) \ (8.314 \ \rm J/mol \cdot K)(500 \ {\rm K}) \ln \left( \frac{0.02 \ {\rm m^3}}{0.01 \ {\rm m^3}} \right) \newline 
& = & 6.9298 \times 10^2 \ {\rm J} \approx 693 \ {\rm J}.
\end{array}
\end{equation}
+ Then the answers are: (a) $T_1 = T_2 = 500 \ {\rm K}$, (b) $p_2 = 50 \ {\rm kPa}$, (c)  $W_{1 \rightarrow 2} = 693 \ {\rm J}$.


## References
1. <a name="ref1"></a>Wikipedia contributors, "Isothermal process", Wikipedia, The Free Encyclopedia, 22 Oct 2020, 07:36 UTC, url <https://en.wikipedia.org/w/index.php?oldid=984813134> [20201215].
2. <a name="ref2"></a>Carl R. Nave, "Kinetic Theory", HyperPhysics, 2017, url <http://hyperphysics.phy-astr.gsu.edu/hbase/thermo/isoth.html> [20201210].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/phys/2020-12-15-isothermal-process.md)
