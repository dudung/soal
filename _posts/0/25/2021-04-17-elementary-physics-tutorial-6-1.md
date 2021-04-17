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
tags: ["wave", "sine wave", "solution to wave equation", "propagation direction", "tutorial-6", "fi1202", "2020-2"]
date: 2021-04-17 21:44:00 +07
permalink: /0251
src: https://github.com/dudung/soal/commits/master/_posts/0/25/2021-04-17-elementary-physics-tutorial-6-1.md
ref: http://hyperphysics.phy-astr.gsu.edu/hbase/Waves/wavsol.html#c4
---
Sebuah gelombang merambat di sepanjang sumbu $x$ menurut persaman

\begin{equation}\label{eqn:0251-0}
y = A \sin(\omega t + kx + \phi),
\end{equation}

dengan $y$ menyatakan simpangan dalam $\rm m$, $A$ amplitudoo dalam $\rm m$, $t$ waktu dalam $\rm s$, $x$ posisi dalam $\rm m$, dan $\phi$ dalam $\rm rad$. Bila $A = 0.17 \ \rm m$, $\omega = 8.2\pi \ \rm rad/s$, $k = 0.54\pi \ \rm rad/m$, dan $\phi = 0$, besar dan arah kecepatan gelombang tersebut adalah

A | $18.5185 \ \rm m/s$ dan ke arah kanan.
B | $18.5185 \ \rm m/s$ dan ke arah kiri.
C | $15.1852 \ \rm m/s$ dan ke arah kanan.
D | $15.1852 \ \rm m/s$ dan ke arah kiri.
E | $5.18518 \ \rm m/s$ dan ke arah kanan.


## &nbsp;
Laju rambat gelombang diberikan oleh

\begin{equation}\label{eqn:0251-1}
v = \frac{\omega}{k}
\end{equation}

dan

$k$ | $\omega$ | $\thicksim\rightarrow$
$+$ | $+$ | $x-$
$+$ | $-$ | $x+$
$-$ | $+$ | $x+$
$-$ | $-$ | $x-$

memberikan arahnya untuk Persamaan \eqref{eqn:0251-0}. Terkait dengan Persaman \eqref{eqn:0250-0} terdapat kode Python yang dapat dijalankan secara online sebagai berikut ini.

<iframe src="https://trinket.io/embed/python/b309ab7105" width="100%" height="200" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
