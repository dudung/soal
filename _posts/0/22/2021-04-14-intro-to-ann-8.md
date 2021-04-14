---
layout: soal
author: viridi
title: "0228"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["artificial neural network", "ann", "feed forward", "three layers", "error", "fi3201", "2020-2"]
date: 2021-04-14 12:00:00 +07
permalink: /0228
src: https://github.com/dudung/soal/commits/master/_posts/0/22/2021-04-13-intro-to-ann-8.md
ref: https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/
---
Suatu arsitektur JST berjenis feed forward terdiri dari dua neuron masukan ($\LARGE \color{#ffcc00} \bullet$), dua neuron tersembunyi ($\LARGE \color{#66cc00} \bullet$), dan satu neuron keluaran ($\LARGE \color{#ff6600} \bullet$).

![]({{site.baseurl}}/assets/img/0/22/0228.png)

Terdapat pasangan data input $I_1$ dan $I_2$ sejumlah $N$ buah yang akan menghasilkan data output $O_1$ dengan jumlah yang sama. Target $T_1$ adalah nilai data sebenarnya yang diharapkan muncul, sehingga dapat didefinisikan kesalahan total untuk seluruh $N$ data dalam bentuk

\begin{equation}\label{eqn:0228-0}
\epsilon = \sum_{i = 1}^N \epsilon_i.
\end{equation}

Rumusan kesalahan untuk setiap data ke-$i$ yang umumnya digunakan adalah


<ol type="A">
<li>$\displaystyle \frac12 \log \left[ T_1^{(i)} - O_1^{(i)} \right]$.
<li>$\displaystyle \frac12 \sqrt{ T_1^{(i)} - O_1^{(i)} }$.
<li>$\displaystyle \frac12 \left| T_1^{(i)} - O_1^{(i)} \right|$.
<li>$\displaystyle \frac12 \left[ T_1^{(i)} - O_1^{(i)} \right]$.
<li>$\displaystyle \frac12 \left[ T_1^{(i)} - O_1^{(i)} \right]^2$.
