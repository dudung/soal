---
layout: soal
author: viridi
title: "0076"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["ode", "ordinary differential equation", "numerical solution", "euler method", "fi3201", "2020-1"]
date: 2021-03-17 11:04:00 +07
permalink: /soal/0076
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/04/2021-03-17-euler-method-1.md
ref: http://calculuslab.deltacollege.edu/ODE/7-C-1/7-C-1-h-c.html
---
Suatu persamaan diferensial dalam bentuk

\begin{equation}\label{eqn:0076-0}
\frac{dx}{dt} = f(t, x)
\end{equation}

dengan syarat awal $x(t_0) = x_0$ dan $f(t_0, x_0)$, dapat diselesaikan dengan menggunakan metode Euler. Untuk kasus ini terdapat rumusan iteratif

\begin{equation}\label{eqn:0076-1}
x(t_{n+1}) = x(t_n) + v(t_n) \Delta t
\end{equation}

dengan $\Delta t = t_{n+1} - t_n$ dan $v = dx/dt$. Dengan syarat awal $v(t_0) = v_0$ dan $g(t_0, v_0)$, serta hubungan $a = dv/dt$ persamaan berikut

\begin{equation}\label{eqn:0076-2}
\frac{dv}{dt} = g(t, v)
\end{equation}

memiliki solusi iteratif

<ol type="A">
<li>$v(t_{n+1}) = v(t_n) - a(t_n) \Delta t$.
<li>$v(t_{n+1}) = v(t_n) - a(t_{n+1}) \Delta t$.
<li>$v(t_{n+1}) = v(t_n) + a(t_{n+1}) \Delta t$.
<li>$v(t_n) = v(t_{n+1}) - a(t_{n+1}) \Delta t$.
<li>$v(t_{n+1}) = v(t_n) + a(t_n) \Delta t$.
