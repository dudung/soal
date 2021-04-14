---
layout: soal
author: viridi
title: "0229"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["artificial neural network", "ann", "feed forward", "three layers", "error", "delta rule", "fi3201", "2020-2"]
date: 2021-04-14 12:33:00 +07
permalink: /0229
src: https://github.com/dudung/soal/commits/master/_posts/0/22/2021-04-13-intro-to-ann-9.md
ref: https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/
---
Suatu arsitektur JST berjenis feed forward terdiri dari dua neuron masukan ($\LARGE \color{#ffcc00} \bullet$), dua neuron tersembunyi ($\LARGE \color{#66cc00} \bullet$), dan satu neuron keluaran ($\LARGE \color{#ff6600} \bullet$).

![]({{site.baseurl}}/assets/img/0/22/0228.png)

Terdapat pasangan data input $I_1$ dan $I_2$ sejumlah $N$ buah yang akan menghasilkan data output $O_1$ dengan jumlah yang sama. Target $T_1$ adalah nilai data sebenarnya yang diharapkan muncul, sehingga dapat didefinisikan kesalahan total untuk seluruh $N$ data dalam bentuk

\begin{equation}\label{eqn:0228-0}
\epsilon = \sum_{i = 1}^N \frac12 \left[ T_1^{(i)} - O_1^{(i)} \right]^2.
\end{equation}

Kesalahan total dapat diminimumkan dengan mengubah-ubah nilai-nilai bobot $w_{11}$, $w_{12}$, $w_{21}$, $w_{22}$, $u_{11}$, dan $u_{12}$ dengan melalui

\begin{eqnarray}
\frac{\partial \epsilon}{\partial w_{11}} = 0, \newline
\frac{\partial \epsilon}{\partial w_{12}} = 0, \newline
\frac{\partial \epsilon}{\partial w_{21}} = 0, \newline
\frac{\partial \epsilon}{\partial w_{22}} = 0, \newline
\frac{\partial \epsilon}{\partial u_{11}} = 0, \newline
\frac{\partial \epsilon}{\partial u_{12}} = 0,
\end{eqnarray}

bila memungkinan. Atau mengubahnya secara iteratif dengan meggunakan aturan delta, yang tak lain adalah penerapan algoritma gradient descent pada aturan pembelajaran JST. Dengan indeks atas $+$ menggambarkan nilai bobot yang telah diubah dan $\eta$ merupakan laju belajar. Bentuk iteratif pengubahan nilai-nilai bobot yang tidak tepat adalah

<ol type="A">
<li>$\displaystyle w_{11}^+ = w_{11} - \eta \frac{\partial \epsilon}{\partial w_{11}}$.
<li>$\displaystyle u_{11}^+ = u_{11} - \eta \frac{\partial \epsilon}{\partial u_{11}}$.
<li>$\displaystyle w_{12}^+ = w_{12} - \eta \frac{\partial \epsilon}{\partial w_{12}}$.
<li>$\displaystyle u_{12}^+ = u_{12} - \eta \frac{\partial \epsilon}{\partial u_{12}}$.
<li>$\displaystyle w_{11}^+ = u_{11} - \eta \frac{\partial \epsilon}{\partial u_{11}}$.
