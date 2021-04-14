---
layout: soal
author: viridi
title: "0230"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["artificial neural network", "ann", "feed forward", "three layers", "training", "fi3201", "2020-2"]
date: 2021-04-14 17:32:00 +07
permalink: /0230
src: https://github.com/dudung/soal/commits/master/_posts/0/23/2021-04-13-ann-training-0.md
ref: https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/
---
Suatu arsitektur JST berjenis feed forward terdiri dari dua neuron masukan ($\LARGE \color{#ffcc00} \bullet$), dua neuron tersembunyi ($\LARGE \color{#66cc00} \bullet$), dan satu neuron keluaran ($\LARGE \color{#ff6600} \bullet$).

![]({{site.baseurl}}/assets/img/0/22/0228.png)

Terdapat pasangan data input $I_1$ dan $I_2$ sejumlah $N$ buah yang akan menghasilkan data output $O_1$ dengan jumlah yang sama. Target $T_1$ adalah nilai data sebenarnya yang diharapkan muncul, sehingga dapat didefinisikan kesalahan total untuk seluruh $N$ data dalam bentuk

\begin{equation}\label{eqn:0230-0}
\varepsilon = \sum_{i = 1}^N \frac12 \left[ T_1^{(i)} - O_1^{(i)} \right]^2.
\end{equation}

Kesalahan total dapat diminimumkan dengan mengubah-ubah nilai-nilai bobot $w_{11}$, $w_{12}$, $w_{21}$, $w_{22}$, $u_{11}$, dan $u_{12}$ dengan melalui

\begin{equation}\label{eqn:0230-1}
v_{ij}^{\rm (new)} = v_{ij} - \eta \frac{\partial \varepsilon}{\partial v_{ij}},
\end{equation}

dengan $v_{ij}$ adalah suatu bobot dan $v_{ij}^{\rm (new)}$ adalah bobot yang telah diubah agar nilai error total $\varepsilon$ berkurang. Selanjutnya untuk memudahkan dipilih fungsi aktivasi $f(x)$ yang memiliki bentuk

\begin{equation}\label{eqn:0230-2}
\frac{\partial f(x)}{\partial x} = f(x) [1 - f(x) ]
\end{equation}

untuk turunannya. Terkait dengan $w_{ij}$ dan output $O_1^{(k)}$ dapat diperoleh hubungan

\begin{equation}\label{eqn:0230-3}
O_1^{(k)} = f\left[ u_{11} f(w_{11} I_1^{(k)} + u_{12} I_2^{(k)}) + u_{12} f(w_{21} I_1^{(k)} + w_{22} I_2^{(k)}) \right].
\end{equation}



<ol type="A">
<li>$$.
<li>$$.
<li>$$.
<li>$$.
<li>$$.
