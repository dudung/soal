---
layout: post
author: viridi
title: commuter air - particulate matter
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: abm
tags: ["particle", "random", "commuter"]
date: 2020-12-01 18:28:00 +07
permalink: /sd/commuter-air-pm
---
Microscopic particles of solid or liquid matter that are suspended in the air are known as particulate matter [[1](#ref1)]. Relation between in and out passanger in some commuter stations are proposed using system dynamics (SD) approach [[1](#ref2)].


## Causal loop v1
Some nodes related to environmental parameters ($h_{\rm prep}$, $v_{\rm wind}$, $T_{\rm env}$, $p_{\rm env}$, $\rm RH_{env}$), passanger and population around station $\rm STA$, health protocols ($\rm HP$), and particulate matters ($\rm PM_{10}$ and $\rm PM_{2.5}$) are used in creating the first version of causal loop as shown in Fig. <a href="#fig:commuter-pm-v1">1</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/sd/commuter-pm-v1.png)
<br />
Figure <a name="fig:commuter-pm-v1">1</a> Causal loop for passanger in and out, denoted by $N_{s,\rm in}$ and $N_{s,\rm out}$, at station $s$ to existence of SARS-COV-2 $n_{\rm SARS-COV-2}$.
{: refdef}

$\rm IQ$, $\rm EQ$, $\rm SQ$, and $\rm TQ$ are related to education level, information literacy, and responsibility of a person to follow the health protocols ($\rm HP$) in reducing the existence of SARS-COV-2 $n_{\rm SARS-COV-2}$ in the ambient air of a station $\rm STA$. This version has not been tested yet.


## Causal loop v2.1
A modification is adde to the two sub-loops, whare one is a balancing loop ($B$) and the other is a reinforcing loop ($R$), even the last is in a negative sense. The modified causal loop diagram is shown in Fig. <a href="#fig:commuter-pm-v2.1">2</a>.

{:refdef: style="text-align: center;"}
![..](/assets/img/sd/commuter-pm-v2.1.png)
<br />
Figure <a name="fig:commuter-pm-v2.1">1</a> Sub-loops showing balancing $B$ and reinforcing $R$ loops, modified from previous version of causal loop diagram.
{: refdef}

The version 2.1 in Fig. <a href="#fig:commuter-pm-v2.1">2</a> is created for testing the relation in more simpler way. Suppose that all the $\rm HP$ are simply reduced to single value $\rm HP \in [0, 1]$ and can not stop completely $n_{\rm SARS-COV-2}$. The difference between $N_{\rm inf}$ and $N_{\rm case}$ is also must be made clear, since they are both required to perform the reinforce loop ($R$). From the test clinic and hospital we can get number of the case $N_{\rm case}$, which does not reflect the real number of infected person $N_{\rm inf}$ due to small number of test compared to the sub-district population $P_{\rm sub-district}$ around a station $\rm STA$. A relation between $N_{\rm inf}$ and $N_{\rm case}$ can be as follow

\begin{equation}
\label{eqn:compm-N-case-N-inf}
N_{\rm case} = \alpha N_{\rm inf},
\end{equation}

where $\alpha$ is a predicted ratio of $N_{\rm case}$ to $N_{\rm inf}$, which could be function of time $t$. It should be that $0 \le \alpha \lt\lt 1$. We can use similar way to define the relation between $N_{\rm death}$ and $N_{\rm case}$ through

\begin{equation}
\label{eqn:compm-N-death-N-case}
N_{\rm death} = \beta N_{\rm case},
\end{equation}

where $\beta$ is also can be function of time $t$. Sub-district population around the station will be changed

\begin{equation}
\label{eqn:compm-P-sub-district}
P_{\rm sub-district}(t + \Delta t) = P_{\rm sub-district}(t) - N_{\rm death},
\end{equation}

with $\Delta t$ is taken to one day and unit of $t$ is day. The last relation for balancing loop ($B$) is between $P_{\rm sub-district}$ and $N_{\rm inf}$ through

\begin{equation}
\label{eqn:compm-N-inf-P-sub-district}
N_{\rm inf} = \gamma P_{\rm sub-district},
\end{equation}

where $\gamma$ is unknown since $N_{\rm inf}$ is also uknown. We can only have the information of $N_{\rm case}$ and reported $N_{\rm death}$, when the $N_{\rm death}$ is related to Covid-19 cases.


## References
1. <a name="ref1"></a>Wikipedia contributors, "Particulates", Wikipedia, The Free Encyclopedia, 28 Nov 2020, 11.37 UTC, url <https://en.wikipedia.org/w/index.php?oldid=991125731> [20201202].
2. <a name="ref1"></a>Wikipedia contributors, "System dynamics", Wikipedia, The Free Encyclopedia, 1 Jun 2020, 01:14 UTC, <https://en.wikipedia.org/w/index.php?oldid=960079253> [2021202].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/sd/2020-12-02-commuter-air-pm.md)
