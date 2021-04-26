---
layout: soal
author: viridi
title: "0305"
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
date: 2021-04-26 19:58:00 +07
permalink: /0305
src: https://github.com/dudung/soal/commits/master/_posts/0/30/2021-04-26-elementary-physics-tutorial-7-5.md
ref: https://www.google.com
---
Pita gelap pertama di kedua sisi terang pusat dipisahkan oleh sudut $51.0 ^\circ$ pada layar akibat difraksi oleh suatu celah pada cahaya biru berpanjang gelombang $440 \ \rm nm$. Lebar celah dan lebar sudut difraksi pusat untuk cahaya hijau berpanjang gelombang $555 \ \rm nm$ adalah

A | $1.022\rm \mu m$ dan $65.78 ^\circ$.
B | $1.071\rm \mu m$ dan $48.50 ^\circ$.
C | $1.071\rm \mu m$ dan $65.78 ^\circ$.
D | $1.022\rm \mu m$ dan $48.50 ^\circ$.
E | $1.017\rm \mu m$ dan $67.58 ^\circ$.


## &nbsp;
Posisi angular gelap ke-$m$ pada difraksi celah tunggal dengan lebar $a$ diberikan oleh

\begin{equation}\label{eqn:0305-0}
a \sin \theta = m \lambda, \ \ \ \ m = 1, 2, 3, \dots,
\end{equation}

dengan $\lambda$ adalah panjang gelombang cahaya yang mengalami difraksi. Pita gelap pertama ($m = 1$) pada kedua sisi terang pusat dipisahkan oleh sudut $\beta$

\begin{equation}\label{eqn:0305-1}
\beta = 2 \theta = 2 \arcsin \left( \frac{1\cdot\lambda}{a} \right).
\end{equation}

Bila $\beta$ diketahui maka lebar celah untuk dapat diperoleh

\begin{equation}\label{eqn:0305-2}
a = \frac{1\cdot\lambda}{\sin \tfrac12 \beta}.
\end{equation}

Angka $1$ pada Persamaan \eqref{eqn:0305-1} dan \eqref{eqn:0305-2} sengaja masih ditulis untuk memudahkan kaitan kedua persamaan tersebut dengan Persamaan \eqref{eqn:0305-0}.

Pita gelap pertama di kedua sisi terang pusat dipisahkan oleh sudut $51.0 ^\circ$ pada layar akibat difraksi oleh suatu celah pada cahaya hijau berpanjang gelombang $555 \ \rm nm$. Lebar celah dan lebar sudut difraksi pusat untuk cahaya biru berpanjang gelombang $440 \ \rm nm$ dapat dihitung menggunakan kode Python berikut.

<iframe src="https://trinket.io/embed/python/f0ccb4879a" width="100%" height="340" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


{% comment %}
tutorial-7 problem-6
Ketika cahaya biru panjang gelombang 440 nm melewati sebuah celah, pita gelap pertama di kedua sisi pusat dipisahkan oleh sudut 51,0°. Kemudian cahaya hijau panjang gelombang 555 nm dilewatkan pada celah tersebut. Tentukan lebar celah dan berapakah lebar sudut puncak difraksi pusat untuk cahaya hijau?
When the 440 nm wavelength blue light passes through a single slit, the first dark band is on either side of the center by an angle of 51.0°. Then a 555 nm wavelength green light is passed through the same slit. Determine the width of the slit and the angular width of the central diffraction peak of the green light?
{% endcomment %}
