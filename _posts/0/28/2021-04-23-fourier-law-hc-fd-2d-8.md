---
layout: soal
author: viridi
title: "0288"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["heat conduction", "fourier's law", "steady state", "separation of variable", "numerical solution", "grid", "2-d", "fi3201", "2020-2"]
date: 2021-04-23 16:50:00 +07
permalink: /0288
src: https://github.com/dudung/soal/commits/master/_posts/0/28/2021-04-23-fourier-law-hc-fd-2d-8.md
ref: https://www.eng.auburn.edu/~dmckwski/mech7210/condbook.pdf#page=94
---
Terdapat segiempat yang memiiki distribusi temperatur $T(x, y)$ yang bersyarat batasnya adalah

\begin{equation}\label{eqn:0288-0}
T(0, y) = T(x, 0) = T(L, y) = T_1, \ \ \ \ T(x, H) = T_2,
\end{equation}

dengan $0 \le x \le L$ dan $0 \le y \le H$, sebagaimana diilustrasikan dalam gambar berikut (kiri) dan salah satu cara diskritasinya (kanan).

![]({{site.baseurl}}/assets/img/0/28/0282.png) | ![]({{site.baseurl}}/assets/img/0/28/0288.png)

Dengan diskritisasi ruang pada arah $x$ dan $y$ adalah $\Delta x$ dan $\Delta y$ dapat diperoleh

\begin{equation}\label{eqn:0288-1}
x_i = i \Delta x, \ \ \ \ i = 0, \dots, N
\end{equation}

dan

\begin{equation}\label{eqn:0288-2}
y_j = j \Delta y, \ \ \ \ j = 0, \dots, M.
\end{equation}

Perumusan $\Delta x$ dan $\Delta y$ adalah

A | $\displaystyle \frac{L}{N+1}$ dan $\displaystyle \frac{H}{M+1}$
B | $\displaystyle \frac{L}{N-1}$ dan $\displaystyle \frac{H}{M-1}$
C | $\displaystyle \frac{L}{N-1}$ dan $\displaystyle \frac{H}{M}$
D | $\displaystyle \frac{L}{N}$ dan $\displaystyle \frac{H}{M-1}$
E | $\displaystyle \frac{L}{N}$ dan $\displaystyle \frac{H}{M}$
