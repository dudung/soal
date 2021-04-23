---
layout: soal
author: viridi
title: "0289"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["spatial discretization", "grid", "heat conduction", "fourier's law", "steady state", "numerical solution", "2-d", "fi3201", "2020-2"]
date: 2021-04-23 19:40:00 +07
permalink: /0289
src: https://github.com/dudung/soal/commits/master/_posts/0/28/2021-04-23-fourier-law-hc-fd-2d-9.md
ref: https://www.eng.auburn.edu/~dmckwski/mech7210/condbook.pdf#page=94
---
Terdapat segiempat dengan panjang $L$ dan tinggi $H$ yang keempat titik sudutnya memiliki koordinat $(0, 0)$, $(L, 0)$, $(L, H)$, dan $(0, H)$, dengan syarat batas temperaturnya

\begin{equation}\label{eqn:0289-0}
T(0, y) = T(x, 0) = T(L, y) = T_1, \ \ \ \ T(x, H) = T_2,
\end{equation}

yang dapat diilustrasikan dalam gambar bagian kiri berikut.

![]({{site.baseurl}}/assets/img/0/28/0289a.png) | ![]({{site.baseurl}}/assets/img/0/28/0289b.png)

Diskritisasi segiempat pada gambar di atas bagian kiri diberikan pada gambar di atas bagian kanan dengan temperatur pada batas-batasnya adalah kanan (right) $T_R$, bawah (bottom) $T_B$, kiri (left) $T_L$, dan atas (top) $T_T$. Koordinat $(x, y)$ yang semula kontinu menjadi bernilai diskrit dan cukup dinyatakan dengan $(i, j)$. Pernyataan yang benar adalah


A | $T_L = T_2$, &nbsp;&nbsp; $a = (0, 2)$.
B | $T_R = T_1$, &nbsp;&nbsp; $c = (N, 2)$.
C | $T_T = T_2$, &nbsp;&nbsp; $b = (4, 0)$.
D | $T_B = T_2$, &nbsp;&nbsp; $d = (4, M)$.
E | $T_L = T_2$, &nbsp;&nbsp; $b = (4, 0)$.
