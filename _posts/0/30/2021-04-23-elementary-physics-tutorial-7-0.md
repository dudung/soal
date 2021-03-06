---
layout: soal
author: viridi
title: "0300"
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
date: 2021-04-23 20:40:00 +07
permalink: /0300
src: https://github.com/dudung/soal/commits/master/_posts/0/30/2021-04-23-elementary-physics-tutorial-7-0.md
ref: https://www.google.com
---
Terdapat celah ganda yang menghasilkan pola-pola interferensi pada layar, yang terletak sejauh $L$ dari celah, setelah berkas cahaya monokromatik dengan panjang gelombang $\lambda$ melewati celah. Jarak antar celah adalah $d$. Posisi terang ke-$n$ terletak pada

\begin{equation}\label{eqn:0300-0}
\sin\theta_n = \frac{\lambda}{d} n, \ \ \ \ n = 1, 2, \dots.
\end{equation}

dari terang pusat. Untuk sudut $\theta$ kecil atau $y_n < < L$ dapat digunakan aproksimasi

\begin{equation}\label{eqn:0300-1}
\sin \theta_n \approx \tan \theta_n = \frac{y_n}{L},
\end{equation}

sehingga Persamaan \eqref{eqn:0300-0} akan menjadi

\begin{equation}\label{eqn:0300-2}
y_n = \frac{L \lambda}{d} n, \ \ \ \ n = 1, 2, \dots.
\end{equation}

Suatu celah ganda dengan jarak celah $d$ dilewati oleh cahaya monokromatik dengan dua panjang gelombang berbeda pada suatu waktu. Pola-pola interferensi tertangkap pada layar yang terletak pada jarak $L = 1.6 \ \rm m$ dari celah. Untuk $\lambda_A = 480 \ \rm nm$ diperoleh $y_{A,3} = 16 \ \rm mm$, maka untuk $\lambda_B = 650 \ \rm nm$ akan diperoleh $y_{B,2}$ yang bernilai

A | $7.88 \ \rm mm$.
B | $14.44 \ \rm mm$.
C | $17.72 \ \rm mm$.
D | $32.50 \ \rm mm$.
E | selain dari semua jawaban di atas.


## &nbsp;
Bila terdapat cahaya dengan dua panjang gelombang berbeda melewati celah ganda yang sama, pada saat berbeda, dengan jarak antar kedua celah $d$, Persamaan \eqref{eqn:0300-2} dapat dituliskan menjadi

\begin{equation}\label{eqn:0300-3}
d = \frac{L \lambda_A}{y_{A,3}} n_A
\end{equation}

untuk $\lambda = \lambda_A$, $n_A = 3$ pada suatu saat dan

\begin{equation}\label{eqn:0300-4}
d = \frac{L \lambda_B}{y_{B,2}} n_B
\end{equation}

untuk $\lambda = \lambda_B$, $n_B = 2$ pada saat yang lain, sehingga

\begin{equation}\label{eqn:0300-5}
y_{B,2} = \frac{n_B L \lambda_B}{n_A L \lambda_A} y_{A,3} = \frac{n_B \lambda_B}{n_A \lambda_A} y_{A,3}.
\end{equation}

Persamaan \eqref{eqn:0300-5} dan data dalam soal dapat digunakan untuk menghitung $y_{B,2}$ menggunakan kode Python berikut.

<iframe src="https://trinket.io/embed/python/513b3181bd" width="100%" height="220" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
