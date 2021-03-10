---
layout: soal
author: viridi
title: "0006"
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["sysmtem of linear equation", "jacobi method", "iterative"]
date: 2021-03-10 10:31:00 +07
permalink: /soal/0006
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/00/2021-03-10-jacobi-method.md
ref: https://mathworld.wolfram.com/JacobiMethod.html
---
Terdapat suatu $M$ buath persamaan linier dengan $N$ buah variabel tidak diketahui $(x_1, x_2, \dots, x_N)$ dalam bentuk

\begin{equation} \nonumber
\sum_{j = 1}^N a_{ij} x_j = b_i,
\end{equation}

dengan $i = 1, 2, \dots, M$. Secara iteratif nilai dapat digunakan

\begin{equation} \nonumber
x_i^{k+1} = \frac{1}{a_{ii}} \left(b_i - \sum_{j \ne 1} a_{ij} x_j^k \right)
\end{equation}

untuk mencari $x_i^{k+1}$ pada iterasi ke $k+1$ dengan $\{x_i^1 \| i = 1, 2, \dots, N\}$ adalah tebakan awal iterasi. Cara di atas dikenal dengan nama

<ol type="A">
<li>Metode Newton-Raphson.
<li>Metode Gauss-Seidel.
<li>Metode eliminasi Gauss.
<li>Metode Jacobi.
<li>Metode Runge-Kutta.
