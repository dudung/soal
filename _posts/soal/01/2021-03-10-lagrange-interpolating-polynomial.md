---
layout: soal
author: viridi
title: "0015"
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["interpolation", "lagrange", "polynomial function"]
date: 2021-03-10 17:16:00 +07
permalink: /soal/0015
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/01/2021-03-10-list-square-fitting.md
ref: https://mathworld.wolfram.com/LagrangeInterpolatingPolynomial.html
---
Polinomial $P(x)$ berorde $N-1$ yang melewati semua pasangan data $\\{(x_i, y_i) \ \| \ i = 1, 2, \dots, N \\}$ dapat diperoleh, salah satunya, dengan menggunakan polinomial interpolasi Lagrange

\begin{equation} \nonumber
P(x) = \sum_{j = 1}^N y_j l_j(x),
\end{equation}

dengan

\begin{equation} \nonumber
l_j(x) = \prod_{
\begin{array}{c}
k = 1, \newline
k \ne j
\end{array}
}^N \frac{x - x_k}{x_j - x_k}.
\end{equation}

Untuk data berupa titik-titik $(0, 0)$, $(1, 3)$, dan $(2, 0)$ polinomial $l_1(x)$, $l_2(x)$, dan $l_3(x)$ adalah

<ol type="A">

<li>$\frac12 x(x - 1)$, $\frac12 (x - 1)(x - 2)$, $-x(x - 2)$.
<li>$-x(x - 2)$, $\frac12 x(x - 1)$, $\frac12 (x - 1)(x - 2)$.
<li>$-x(x - 2)$, $\frac12 (x - 1)(x - 2)$, $\frac12 x(x - 1)$.
<li>$\frac12 (x - 1)(x - 2)$, $\frac12 x(x - 1)$, $-x(x - 2)$.
<li>$\frac12 (x - 1)(x - 2)$, $-x(x - 2)$, $\frac12 x(x - 1)$,


