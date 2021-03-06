---
layout: soal
author: viridi
title: "0250"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["wave", "string tension", "mass density", "wave velocity", "transversal wave", "tutorial-6", "fi1202", "2020-2"]
date: 2021-04-17 22:55:00 +07
permalink: /0250
src: https://github.com/dudung/soal/commits/master/_posts/0/25/2021-04-17-elementary-physics-tutorial-6-0.md
ref: http://hyperphysics.phy-astr.gsu.edu/hbase/Waves/string.html#c2
---
Terdapat tali dengan massa $m$ yang diregangkan dan terikat ujung-ujungnya pada dua dua batang peyangga yang terpisah sejauh $L$. Saat salah satu peyangga dipukul dengan palu, sebuah gelombang transversal menjalar sepanjang tali dan mencapai peyangga lainnya dalam waktu $\Delta t$. Bila $m = 0.4 \ \rm kg$, $L = 8.7 \ \rm m$, dan $t = 0.85 \ \rm s$, tegangan tali adalah

A | $0.8166 \ \rm N$
B | $4.8166 \ \rm N$
C | $0.4817 \ \rm N$
D | $6.8164 \ \rm N$
E | $1.4866 \ \rm N$

## &nbsp;
Pada suatu tali dengan tegangan $\tau$ dan rapat massa $\mu$ laju rambat gelombang diberikan oleh

\begin{equation}\label{eqn:0250-0}
v = \sqrt{\frac{\tau}{\mu}},
\end{equation}

dengan

\begin{equation}\label{eqn:0250-1}
\mu = \frac{m}{L}.
\end{equation}

Agar gelombang transversal dapat menempuh jarak antar peyangga sebesar $L$ dalam waktu $t$ diperlukan laju rambat sebesar

\begin{equation}\label{eqn:0250-2}
v = \frac{L}{t}.
\end{equation}

Dengan menggunakan Persamaan \eqref{eqn:0250-0}, \eqref{eqn:0250-1}, dan \eqref{eqn:0250-2} dapat diperoleh

\begin{equation}\label{eqn:0250-3}
\end{equation}
\tau = \mu v^2 = \frac{m}{L} \left( \frac{L}{t} \right)^2 = \frac{mL}{t^2},

yang satuannya telah sama dengan satuan tegangan tali atau gaya, yaitu $\rm N$ atau $\rm kg \cdot m / s^2$. Terkait dengan Persaman \eqref{eqn:0250-3} terdapat kode Python yang dapat dijalankan secara online sebagai berikut ini.

<iframe src="https://trinket.io/embed/python/56ce1a928e" width="100%" height="200" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>