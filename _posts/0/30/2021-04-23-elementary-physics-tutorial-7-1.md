---
layout: soal
author: viridi
title: "0301"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["interference", "double-slit", "tutorial-7", "fi1202", "2020-2"]
date: 2021-04-24 04:42:00 +07
permalink: /0301
src: https://github.com/dudung/soal/commits/master/_posts/0/30/2021-04-23-elementary-physics-tutorial-7-1.md
ref: https://www.google.com
---
Order maksimum interferensi maksimum dan jumlah garis terang yang dapat terbentuk saat cahaya monokromatik dengan panjang gelombang $500 \ \rm nm$ melewati celah ganda dengan jarak antar celah $2.5 \ \rm \mu m$ adalah

A | $5$ dan $11$.
B | $4$ dan $9$.
C | $3$ dan $7$.
D | $2$ dan $5$.
E | $1$ dan $3$.

## &nbsp;
Jumlah garis terang yang dapat dibentuk hasil interferensi dua celah terbatas. Posisi angular $\theta$ garis terang yang terbentuk pada layar diberikan oleh

\begin{equation}\label{eqn:0301-0}
d \sin\theta_m = m \lambda, \ \ \ \ m = 1, 2, \dots.
\end{equation}

Nilai $\sin \theta$ terbatas, nilai maksimumnya adalah $+1$ saat $\theta = \frac12 \pi$. Persamaan \eqref{eqn:0301-0} dapat dituliskan kembali menjadi

\begin{equation}\label{eqn:0301-1}
m = \frac{d \sin\theta_m}{\lambda},
\end{equation}

yang akan memberikan nilai maksimum $m = m_{\rm max}$ saat digunakan $\theta = \frac12 \pi$. Jumlah garis terang yang terbentuk adalah

\begin{equation}\label{eqn:0301-2}
N_{\rm bright} = 2 m_{\rm max} + 1,
\end{equation}

dengan terdapat sejumlan $m_{\rm max}$ garis terang di atas dan di bawah terang pusat $m = 0$.

Kode Pyhon berikut dapat digunakan untuk menghitung jumlah garis terang yang dapat teramati saat cahaya monokromati dengan panjang gelombang $600 \ \rm nm$ melewati celah ganda dengan jarak antar celah $2.4 \ \rm \mu m$.

<iframe src="https://trinket.io/embed/python/6c24cc229b" width="100%" height="420" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>