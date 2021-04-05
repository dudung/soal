---
layout: soal
author: viridi
title: "0164"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["series", "current", "voltage", "relation", "ac", "resistor", "inductor", "capacitor", "impedance", "reactance", "resistance", "fi1202", "2020-1"]
date: 2021-04-05 16:45:00 +07
permalink: /0164
src: https://github.com/dudung/soal/commits/master/_posts/0/16/2021-04-05-ac-circuit-rlc-voltage-all.md
ref: https://www.electronics-tutorials.ws/accircuits/series-circuit.html
---
Terdapat sebuah rangkaian seri RLC arus bolak-balik, yang terdiri dari resistor $R = 60 \ {\rm \Omega}$, induktor $L = 318.4 \ {\rm mH}$, kapasitor $C = 159.1 \ {\rm \mu F}$, dan sumber tegangan bolak-balik $V_S(t)$, seperti pada gambar berikut ini.

![]({{site.baseurl}}/assets/img/0/16/0160.png)

Arus yang mengalir memiliki fungsi

\begin{equation}\nonumber
I_S(t) = I_m \sin \omega t,
\end{equation}

dengan amplitudo arus $I_m = 2 \ {\rm A}$ dan frekuensi $f = 50 \ {\rm Hz}$, yang akan memberikan frekuensi sudut $\omega = 2 \pi f$. Gambar di bawah ini memberikan grafik $I_S(t)$ untuk satu setengah perioda, $T = 0.02 \ {\rm s}$. Dalam gambar $I_S$ dinyatakan dalam $\rm A$ dan waktu $t$ dalam $\rm s$.

![]({{site.baseurl}}/assets/img/0/16/0160a.png)


$X$ | Grafik | $V_X(t)$
:-: | :-: | :-:
$R$ | ![]({{site.baseurl}}/assets/img/0/16/0160b.png) | $120 \sin 100\pi t \ {\rm V}$
$L$ | ![]({{site.baseurl}}/assets/img/0/16/0161.png) | $200 \sin (100\pi t + 0.500 \pi) \ {\rm V}$
$C$ | ![]({{site.baseurl}}/assets/img/0/16/0162.png) | $40 \sin (100\pi t - 0.500 \pi) \ {\rm V}$
$R+L+C$ | ![]({{site.baseurl}}/assets/img/0/16/0163.png) | $200 \sin (100\pi t + 0.295\pi) \ {\rm V}$.

Grafik dan persamaan yang benar adalah pada komponen

<ol type="A">
<li>Gabungan ketiga komponen $R + L + C$, resistor $R$, induktor $L$, dan kapasitor $C$.
<li>Resistor $R$ dan induktor $L$.
<li>Induktor $L$ dan kapasitor $C$.
<li>Kapasitor $C$ dan resistor $R$.
<li>Gabungan ketiga komponen $R + L + C$.
