---
layout: soal
author: viridi
title: "0224"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["artificial neural network", "ann", "activation function", "step unit function", "binary step", "bias", "fi3201", "2020-2"]
date: 2021-04-14 04:39:00 +07
permalink: /0224
src: https://github.com/dudung/soal/commits/master/_posts/0/22/2021-04-13-intro-to-ann-4.md
ref: https://developer.ibm.com/articles/l-neural/
---
Langkah pertama untuk memahami jaringan saraf adalah dengan membuat abstraksi dari neuron biologis dan berkonsentrasi pada karakternya sebagai suatu satuan logis ambang (SLA) atau treshold logic unit (TLU) sebagaimana diilustrasikan berikut ini.

![]({{site.baseurl}}/assets/img/0/22/0223.png)

Keluaran SLA di atas adalah $y_i$ yang merupakan hasil dari fungsi aktivasi dengan masukannya adalah 

\begin{equation}\label{eqn:0224-0}
z_j = b + \sum_i w_{ji} x_i,
\end{equation}

di mana $b$ merupakan bias, $x_i$ adalah nilai pada neuron masukan $i$, dan $w_{ji}$, yang merupakan bobot, menggambarkan kontribusi masukan $i$ terhadap nilai $z_j$. Fungsi aktivasi $f(z_i)$ dapat merupakan fungsi tangga biner (binary step function) atau tangga satuan (unit step funvtion) berbentuk

\begin{equation}\label{eqn:0224-1}
f(z_i) = \left\\{
\begin{array}{cc}
0, & z_i < 0, \newline
1, & z_i \ge 0.
\end{array}
\right.
\end{equation}

Syarat aktivasi dalam Persamaan \eqref{eqn:0224-1} dapat diubah dari $0$ menjadi $a$ menggunakan bias $b$ pada Persamaan \eqref{eqn:0224-0} dengan menetapkan

<ol type="A">
<li>$b = a$.
<li>$b = -a$.
<li>$b = a^{-1}$.
<li>$b = e^a$.
<li>$b = \log a$.
