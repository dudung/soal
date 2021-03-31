---
layout: soal
author: viridi
title: "0128"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["pde", "ftcs", "forward time centered space", "heat equation", "fi3201", "2020-1"]
date: 2021-03-31 08:18:00 +07
permalink: /0128
src: https://github.com/dudung/soal/commits/master/_posts/0/12/2021-03-31-pde-ftcs-scheme.md
ref: https://en.wikipedia.org/wiki/FTCS_scheme
---
FTCS (forward time centered space) merupakan metode beda hingga untuk menyelesaikan persamaan diferensial dengan menggunakan beda hingga maju untuk waktu (forward in time) dan beda hingga tengah untuk ruang (centered in space). Persamaan perambatan panas dala satu-dimensi

\begin{equation}\nonumber
\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}
\end{equation}

merupakan contoh yang sering digunakan untuk ilustrasi penerapan FTCS, Bila didefinisikan

\begin{equation}\nonumber
\beta = \frac{\alpha \Delta t}{(\Delta x)^2}
\end{equation}

Persamaan perambatan panas dalam satu dimensi dengan skema FTSC dapat dituliskan menjadi pernyataan berikut, kecuali

<ol type="A">
<li>$u(x, t + \Delta t) = u(x, t) + \beta [ u(x - \Delta x, t) - 2u(x, t) + u(x + \Delta x, t) ]$.
<li>$u(x, t + \Delta t) = (1 - 2\beta) u(x, t) + \beta u(x - \Delta x, t) + \beta u(x + \Delta x, t)$.
<li>$u_i^j =  u_i^{j+1} + \beta (u_{i-1}^{j+1} -  2 u_i^{j+1} + u_{i+1}^{j+1})$.
<li>$u_i^{j+1} = \beta u_{i-1}^j + (1 - 2\beta) u_i^j + \beta u_{i+1}^j$.
<li>$u_i^{j+1} =  u_i^j + \beta (u_{i-1}^j -  2 u_i^j + u_{i+1}^j)$.
