---
layout: soal
author: viridi
title: "0251"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["wave", "doppler effect", "intensity", "distance", "tutorial-6", "fi1202", "2020-2"]
date: 2021-04-17 18:31:00 +07
permalink: /0251
src: https://github.com/dudung/soal/commits/master/_posts/0/25/2021-04-17-elementary-physics-tutorial-6-1.md
ref: http://hyperphysics.phy-astr.gsu.edu/hbase/Waves/string.html#c2
---
Sebuah gelombang merambat di sepanjang sumbu $x$ menurut persaman

\begin{equation}\label{eqn:0251-0}
y = A \sin(\omega t + kx + \phi),
\end{equation}

dengan $y$ menyatakan simpangan dalam $\rm m$, $A$ amplitudoo dalam $\rm m$, $t$ waktu dalam $\rm s$, $x$ posisi dalam $\rm m$, dan $\phi$ dalam $\rm rad$. Bila $A = 0.17 \ \rm m$, $\omega = 8.2\pi \ \rm rad/s$, $k = 0.54\pi \ \rm rad/m$, dan $\phi = 0$, besar dan arah kecepatan gelombang tersebut adalah

A | $\ \rm m/s$ dan ke arah kanan.
B | $\ \rm m/s$ dan ke arah kiri.
C | $\ \rm m/s$ dan ke arah kanan.
D | $\ \rm m/s$ dan ke arah kiri.
E | $\ \rm m/s$ dan ke arah kanan.


{% comment %}
Terdapat tali dengan massa $m$ yang diregangkan dan terikat ujung-ujungnya pada dua dua batang peyangga yang terpisah sejauh $L$. Saat salah satu peyangga dipukul dengan palu, sebuah gelombang transversal menjalar sepanjang tali dan mencapai peyangga lainnya dalam waktu $\Delta t$. Bila $m = 0.4 \ \rm kg$, $L = 8.7 \ \rm m$, dan $t = 0.85 \ \rm s$, tegangan tali adalah

A | $0.3866 \ \rm N$
B | $0.0444 \ \rm N$
C | $0.4440 \ \rm N$
D | $4.0387 \ \rm N$
E | $0.9664 \ \rm N$

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
\tau = \mu v^2 = \frac{m}{L} \left( \frac{L}{t} \right)^2 = \frac{mL}{t^2},
\end{equation}

yang satuannya telah sama dengan satuan tegangan tali atau gaya, yaitu $\rm N$ atau $\rm kg \cdot m / s^2$. Terkait dengan Persaman \eqref{eqn:0250-3} terdapat kode Python yang dapat dijalankan secara online sebagai berikut ini.

<iframe src="https://trinket.io/embed/python/e1d54a4a0e" width="100%" height="200" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

{% endcomment %}
