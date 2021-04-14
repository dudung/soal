---
layout: soal
author: viridi
title: "0226"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["artificial neural network", "ann", "step unit function", "bias", "or gate", "three input nodes", "fi3201", "2020-2"]
date: 2021-04-14 08:46:00 +07
permalink: /0226
src: https://github.com/dudung/soal/commits/master/_posts/0/22/2021-04-13-intro-to-ann-6.md
ref: https://www.allaboutcircuits.com/textbook/digital/chpt-3/multiple-input-gates/
---
Salah satu pemanfaatan paling sederhana satuan logis ambang (SLA) atau treshold logic unit (TLU) adalah dalam membuat gerbang logika dengan menggunakan jenis perceptron berikut, yang memiliki tiga node masukan ($\LARGE \color{#ffcc00} \bullet$) dan satu node keluaran ($\LARGE \color{#ff6600} \bullet$).

![]({{site.baseurl}}/assets/img/0/22/0225.png)

Tabel kebenaran gerbang OR dengan tiga masukan adalah sebagai berikut ini.

$x_1$ | $x_2$ | $x_3$ | $y_1$
0 | 0 | 0 | 0
0 | 0 | 1 | 1
0 | 1 | 0 | 1
0 | 1 | 1 | 1
1 | 0 | 0 | 1
1 | 0 | 1 | 1
1 | 1 | 0 | 1
1 | 1 | 1 | 1

Digunakan $w_{11} = \frac13$, $w_{12} = \frac13$, dan $w_{13} = \frac13$ dengan 

\begin{equation}\label{eqn:0225-0}
z_j = b + \sum_i w_{ji} x_i,
\end{equation}

dan

\begin{equation}\label{eqn:0225-1}
f(z_i) = \left\\{
\begin{array}{cc}
0, & z_i < 0, \newline
1, & z_i \ge 0.
\end{array}
\right.
\end{equation}

sehingga dapat dituliskan kembali tabel kebenarannya dengan tambahan kolom untuk nilai $f(z_1)$, $z_1$, dan $b$.

$x_1$ | $x_2$ | $x_3$ | $y_1$ || $f(z_1)$ | $z_1$ | $b$
:-: | :-: | :-: | :-: | :-: | :-: | :-: | :-:
0 | 0 | 0 | 0 || 1 | $\frac03$ | 0
0 | 0 | 1 | 1 || 1 | $\frac13$ | 0
0 | 1 | 0 | 1 || 1 | $\frac13$ | 0
0 | 1 | 1 | 1 || 1 | $\frac23$ | 0
1 | 0 | 0 | 1 || 1 | $\frac13$ | 0
1 | 0 | 1 | 1 || 1 | $\frac23$ | 0
1 | 1 | 0 | 1 || 1 | $\frac23$ | 0
1 | 1 | 1 | 1 || 1 | $\frac33$ | 0

yang menunjukkan bahwa masih $y_1 \ne f(z_1)$. Agar dapat terpenuhi bahwa $y_1 = f(z_1)$ dapat dilakukan, salah satu caranya, dengan membuat

<ol type="A">
<li>$b = 3$.
<li>$b = 1$.
<li>$b = 0$.
<li>$b = -\frac13$.
<li>$b = \frac13$.
