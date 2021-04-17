---
layout: soal
author: viridi
title: "0253"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["wave", "doppler effect", "intensity", "distance", "tutorial-6", "fi1202", "2020-2"]
date: 2021-04-17 20:47:00 +07
permalink: /0253
src: https://github.com/dudung/soal/commits/master/_posts/0/25/2021-04-17-elementary-physics-tutorial-6-3.md
ref: http://hyperphysics.phy-astr.gsu.edu/hbase/Sound/souspe.html#c1
---
Terdapat dua buah mikrofon $M_1$ dan $M_2$ yang diletakkan pada jarak $L_1$ dan $L_2$ dari suatu sumber bunyi $S$ berupa speaker sebagaimana diilustrasikan dalam gambar berikut ini.

![]({{site.baseurl}}/assets/img/0/25/0253.png)

Jarak pisah kedua mikrofon adalah $1.5 \ \rm m$. Cepat rambat bunyi di udara pada suatu keadaaan adalah $343 \ \rm m/s$. Mikrofon $M_2$ menangkap terlebih dahulu bunyi yang berasal sumber bunyi $S$ dan baru $1.46 \ \rm ms$ kemudian bunyi yang sama mencapai mikrofon $M_1$.


Pada gambar berikut, sebuah mikrofon ditempatkan pada titik (0,0) sebuah koordinat kartesius. Sedangkan mikrofon kedua ditempatkan pada sumbu-y. kedua mikrofon tersebut terpisah sejauh D=1.5 m. Sebuah sumber suara kemudian ditemparkan pada sumbu +x dengan jarak terhadap mikrofon 1 dan 2 berturut-turut dinyatakan dengan L1 dan L2. Besar cepat rambat bunyi di udara adalah 343 m/s. Suara yang dihasilkan sumber mencapai mikrofon 1 terlebih dahulu, kemudian 1.46 ms kemudian mencapat mikrofon 2. Tentukan besarnya L1 dan L2.


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
