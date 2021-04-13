---
layout: soal
author: viridi
title: "0220"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["artificial neural network", "ann", "architecture", "fi3201", "2020-2"]
date: 2021-04-13 13:56:00 +07
permalink: /0220
src: https://github.com/dudung/soal/commits/master/_posts/0/22/2021-04-13-intro-to-ann-0.md
ref: https://towardsdatascience.com/a-gentle-introduction-to-neural-networks-series-part-1-2b90b87795bc
---
Gelombang pada tali dapat dinyatakan dengan perambatan simpangannya dalam bentuk

\begin{equation}\label{eqn:0211-0}
y(x, t)= A \sin(kx \pm \omega t + \phi),
\end{equation}

dengan simpangan $y$, amplitudo $A$, bilangan gelombang $k$, posisi $x$, frekuensi angular $\omega$, waktu $t$, dan fasa awal $\phi$. Selain itu terdapat besaran lain seperti periode $T$, frekuensi $f$, panjang gelombang $\lambda$, dan laju rambant gelombang $v$, masing-masing terhubung melalui

\begin{eqnarray}
f = \frac{1}{T}, \newline
\omega = \frac{2\pi}{T}, \newline
k = \frac{2\pi}{\lambda}, \newline
v = \frac{\lambda}{T} = \frac{\omega}{k}.
\end{eqnarray}

Persamaan \eqref{eqn:0211-0} dapat dituliskan dalam beberapa bentuk seperti dalam tabel berikut ini.

ID  | Gelombang sinus
--- | ---
SW1 | $y(x, t)= A \sin [ k(x \pm v t) + \phi ]$
SW1 | $\displaystyle y(x, t)= A \sin \left[ 2\pi \left( \frac{x}{\lambda} \pm \frac{t}{T} \right) + \phi \right]$
SW3 | $\displaystyle y(x, t)= A \sin \left[ \frac{2\pi}{\lambda} (x \pm v t) + \phi \right]$
SW4 | $y(x, t)= A \sin (kx \pm 2\pi f t + \phi)$
SW5 | $\displaystyle y(x, t)= A \sin \left( kx \pm 2\pi \frac{t}{T} + \phi \right)$

Bila terdapat gelombang dengan bentuk

\begin{equation}\label{eqn:0211-5}
y(x, t)= 0.2 \sin \left( \pi x - 2\pi \frac{t}{0.1} + \frac{\pi}{2} \right),
\end{equation}

formulasi dengan ID yang paling cepat digunakan untuk memperoleh nilai-nilai $A$, $k$, $T$, dan $\phi$ adalah

<ol type="A">
<li>SW1.
<li>SW3.
<li>SW5.
<li>SW2.
<li>SW4.
