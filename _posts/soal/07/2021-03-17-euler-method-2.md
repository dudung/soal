---
layout: soal
author: viridi
title: "0077"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["ode", "ordinary differential equation", "numerical solution", "euler method", "simple harmonic motion", "fi3201", "2020-1"]
date: 2021-03-17 11:04:00 +07
permalink: /soal/0077
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/04/2021-03-17-euler-method-2.md
ref: https://en.wikipedia.org/wiki/Euler_method
---
Suatu gerak harmonis sederhana memiliki persamaan diferensial biasa linier homogen dalam bentuk

\begin{equation}\label{eqn:0077-0}
\frac{d^2x}{dt^2} + \omega^2 x = 0,
\end{equation}

dengan syarat awal $x(t_0) = t_0$ dan $v(t_0) = v_0$, serta $\Delta t = t_{n+1} - t_n$. Solusi solusi iteratif dari sistem ini adalah

<ol type="A">

<li>$x(t_{n+1}) = v(t_n) + a(t_n) \Delta t$ dan $v(t_{n+1}) = x(t_n) + v(t_n) \Delta t$.
<li>$v(t_{n+1}) = x(t_n) + a(t_n) \Delta t$ dan $x(t_{n+1}) = v(t_n) + v(t_n) \Delta t$.
<li>$v(t_{n+1}) = v(t_n) + a(t_n) \Delta t$ dan $x(t_{n+1}) = x(t_n) + v(t_n) \Delta t$.
<li>$x(t_{n+1}) = x(t_n) + a(t_n) \Delta t$ dan $v(t_{n+1}) = v(t_n) + x(t_n) \Delta t$.
<li>$v(t_{n+1}) = v(t_n) + x(t_n) \Delta t$ dan $x(t_{n+1}) = x(t_n) + a(t_n) \Delta t$.
