---
layout: soal
author: viridi
title: "0075"
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
date: 2021-03-17 10:44:00 +07
permalink: /soal/0075
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/04/2021-03-17-euler-method-0.md
ref: https://tutorial.math.lamar.edu/classes/de/eulersmethod.aspx
---
Suatu persamaan diferensial dalam bentuk

\begin{equation}\label{eqn:0075-0}
\frac{dy}{dt} = f(t, y)
\end{equation}

dengan syarat awal $y(t_0) = y_0$ dan $f(t_0, y_0)$, dapat diselesaikan dengan menggunakan metode Euler yang memiliki rumusan iteratif

<ol type="A">
<li>$y_{n+1} = y_n + f(t_n, y_n) \ (t_{n+1} - t_n)$.
<li>$y_{n} = y_{n+1} + f(t_n, y_n) \ (t_{n+1} - t_n)$.
<li>$y_{n+1} = y_n + f(t_n, y_n) \ (t_n - t_{n+1})$.
<li>$y_{n+1} = y_n - f(t_n, y_n) \ (t_{n+1} - t_n)$.
<li>$y_{n+1} = y_n + f(t_{n+1}, y_n) \ (t_{n+1} - t_n)$.
