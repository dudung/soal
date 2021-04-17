---
layout: soal
author: viridi
title: "0252"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["wave", "sine wave", "solution to wave equation", "propagation direction", "tutorial-6", "fi1202", "2020-2"]
date: 2021-04-17 22:06:00 +07
permalink: /0252
src: https://github.com/dudung/soal/commits/master/_posts/0/25/2021-04-17-elementary-physics-tutorial-6-2.md
ref: http://hyperphysics.phy-astr.gsu.edu/hbase/Waves/wavsol.html#c4
---
Osilasi pada posisi $x = 0$ dari sebuah gelombang transversal yang merambat pada tali diberikan dalam gambar berikut ini.

![]({{site.baseurl}}/assets/img/0/25/0252.png)

Gelombang tersebut merambat ke arah sumbu $x$ positif dengan kelajuan $0.15 \ \rm m/s$. Dengan menggunakan informasi dari gambar di atas dapat diperoleh persamaan matematis gelombang tersebut dalam bentuk

A | $y(x, t) = 0.01 \sin \left( 10\pi t - \frac{200}{3}\pi x + \phi \right)$.
B | $y(x, t) = 0.01 \sin \left( 10\pi t + \frac{200}{3}\pi x + \phi \right)$.
C | $y(x, t) = 0.01 \sin \left( -31.4159 t - 209.4395 x + \phi \right)$.
D | $y(x, t) = 0.01 \sin \left( 209.4395 t - 31.4159 x + \phi \right)$.
E | $y(x, t) = 0.01 \sin \left( -209.4395 t + 31.4159 x + \phi \right)$.


## &nbsp;
Gelombang sinus memiliki persamaan

\begin{equation}\label{eqn:0252-0}
y(x, t) = A \sin(\pm kx \pm \omega t + \phi), 
\end{equation}

dengan $y$ simpangan ($\rm m$), $A$ amplitudo ($\rm m$), $k$ bilangan gelombang ($\rm rad/m$), $x$ posisi ($\rm m$), $\omega$ frekuensi angular ($\rm rad/s$), $t$ waktu ($\rm s$), dan $\phi$ fasa awal ($\rm rad$). Arah perambatan gelombang diberikan ($\thicksim\rightarrow$) ditentukan menurut

$\thicksim\rightarrow$ | $k$ | $\omega$
$x+$ | $+$ | $-$
$x-$ | $+$ | $+$
$x+$ | $-$ | $+$
$x-$ | $-$ | $-$

untuk gelombang sinus pada Persamaan \eqref{eqn:0252-0}. Dari grafik osilasi pada suatu posisi tertentu, misalnya $x = x_0$, dapat diperoleh $y(t) = y(x_0, t)$ yang akan memberikan amplitudo $A$ dan periode osilasi $T$, yang kemudian dapat digunakan untuk menghitung

\begin{equation}\label{eqn:0252-1}
\omega = \frac{2\pi}{T},
\end{equation}

yang merupakan frekuensi angular. Bilangan gelombang dapat diperoleh dengan

\begin{equation}\label{eqn:0252-2}
k = \frac{\omega}{v},
\end{equation}

dengan $v$ merupakan laju perambatan gelombang. Selanjutnya, menggunakan grafik yang diberikan dan Persamaan \eqref{eqn:0252-1} dan \eqref{eqn:0252-2} dapat dihitung $\omega$ dan $k$ menggunakan kode Python berikut.

<iframe src="https://trinket.io/embed/python/027e6599bc" width="100%" height="200" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
