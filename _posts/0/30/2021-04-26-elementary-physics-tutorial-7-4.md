---
layout: soal
author: viridi
title: "0304"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["interference", "thin film", "tutorial-7", "fi1202", "2020-2"]
date: 2021-04-26 19:55:00 +07
permalink: /0304
src: https://github.com/dudung/soal/commits/master/_posts/0/30/2021-04-26-elementary-physics-tutorial-7-4.md
ref: https://www.google.com
---
Cahaya monokromatik berpanjang gelombang $668 \ \rm nm$ melewati celah dengan lebar $6.73 \times 10^{-6} \ \rm m$ dan kemudian memberikan pola difraksi pada layar yang berjarak $1.85 \ \rm m$ dari celah. Pada kedua sisi terang pusat terdapat gelap ketiga. Jarak gelap ketiga terhadap terang pusat adalah

A | $0.577 \ \rm m$.
B | $0.520\ \rm m$.
C | $0.401\ \rm m$.
D | $0.380\ \rm m$.
E | $0.357\ \rm m$.


## &nbsp;
Sebuah celah tunggal dengan lebar celarh $a$ akan menghasilkan terang pusat pada layar dan posisi gelap ke-$m$ menurut

\begin{equation}\label{eqn:0304-0}
a \sin \theta = m \lambda, \ \ \ \ m = 1, 2, 3, \dots,
\end{equation}

dengan posisi vertikal garis gelap ke-$m$ terhadap terang pusat adalah

\begin{equation}\label{eqn:0304-1}
y_m = L \tan \theta, \ \ \ \ m = 1, 2, 3, \dots,
\end{equation}

dengan $L$ adalah jarak layar dari celah. Dengan menggunakan pendekatan $L > > y_m$ dapat diperoleh

\begin{equation}\label{eqn:0304-2}
\tan \theta \approx \sin \theta,
\end{equation}

yang akan membuat Persamaan \eqref{eqn:0304-1} menjadi

\begin{equation}\label{eqn:0304-3}
y_m \approx L \sin \theta = m \left( \frac{L \lambda}{a} \right), \ \ \ \ m = 1, 2, 3, \dots.
\end{equation}

Persamaan \eqref{eqn:0304-1} dan \eqref{eqn:0304-3} dapat digunakan bergantung informasi pada soal.

Cahaya monokromatik berpanjang gelombang $650 \ \rm nm$ melewati celah dengan lebar $6.80 \times 10^{-6} \ \rm m$ dan kemudian memberikan pola difraksi pada layar yang berjarak $1.95 \ \rm m$ dari celah. Pada kedua sisi terang pusat terdapat gelap kedua. Jarak gelap kedua terhadap terang pusat dapat dihitung dengan menggunakan kode Python berikut.

<iframe src="https://trinket.io/embed/python/f0b9b0e670" width="100%" height="280" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

{% comment %}
tutorial-7 problem-5
Cahaya dengan panjang gelombang 668 nm melewati sebuah celah dengan lebar 6,73 x 10-6 m dan jatuh pada layar yang berjarak 1,85 m. Berapa jarak gelap ke tiga dari terang pusat di kedua sisi pada layar?
Light that has a wavelength of 668 nm passes through a slit 6.73x10-6 m wide and falls on a screen that is 1.85 m away. What is the distance on the screen from the center of the central bright fringe to the third dark fringe on either side?
{% endcomment %}
