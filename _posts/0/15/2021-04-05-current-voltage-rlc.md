---
layout: soal
author: viridi
title: "0159"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["current", "voltage", "relation", "ac", "resistor","inductor", "capacitor", "impedance", "reactance", "resistance", "fi1202", "2020-1"]
date: 2021-04-05 06:47:00 +07
permalink: /0159
src: https://github.com/dudung/soal/commits/master/_posts/0/15/2021-04-05-current-voltage-rlc.md
ref: https://www.electronics-tutorials.ws/accircuits/series-circuit.html
---
Terdapat arus bolak-balik

\begin{equation}\nonumber
I(t) = I_m \sin \omega t,
\end{equation}

yang sama mengalir pada sebuah resistor $R$, induktor $L$, dan kapasitor $C$, dengan $I_m$ adalah amplitudo arus bolak-balik dan $\omega$ adalah frekuensi sudut arus-bolak-balik, yang terkait dengan

\begin{equation}\nonumber
\omega = 2 \pi f,
\end{equation}

di mana $f$ sebagai frekuensi arus bolak-balik. Hubungan antara tegangan antar kedua ujung masing-masing komponen ($R$, $L$, $C$) diberikan dalam tabel berikut ini.

$X$ | Rumus | $V_X(t)$ | $V_{X,m} \sin (\omega t + \gamma \pi)$ | $\gamma$ | $Z$
:-: | :-: | --- | --- | :-: | :-:
$R$ | $V_R(t) = R \ I(t)$ | $(R \ I_m) \sin \omega t$ | $(Z \ I_m) \sin \omega t$ | $0$ | $R$
$L$ | $\displaystyle V_L(t) = L \ \frac{dI(t)}{dt}$ | $(\omega L \ I_m) \cos \omega t$ | $(Z \ I_m) \sin(\omega t + \tfrac12 \pi)$ | $\tfrac12$ | $X_L$
$C$ | $\displaystyle V_C(t) = \frac1C \ \int I(t) dt$ | $\displaystyle \left( \frac{I_m}{\omega C} \right) (-\cos \omega t)$ | $(Z \ I_m) \sin(\omega t - \tfrac12 \pi)$ | $-\tfrac12$ | $X_C$

Pernyataan yang tidak tepat adalah

<ol type="A">
<li>Impedansi $Z$ harus selalu mengandung komponen $R$, $L$, dan $C$, serta ketiga komponen tersebut harus selalu tersusun seri.
<li>Reaktansi induktif $X_L = \omega L$.
<li>Reaktansi kapasitif $\displaystyle X_C = \frac1{\omega C}$.
<li>Amplitudo $V_{X,m}$ selalu berbentuk suatu besaran bersatuan hambatan $\Omega$, yang dapat berupa $R$, $X_L$, $X_C$, $Z$, dikalikan $I_m$.
<li>Untuk suatu komponen tidak ideal, impedansinya secara umum adalah $Z = Z(R, L, C)$, yang bila tersusun seri ($R$, $L$, $C$) akan memberikan $Z = \sqrt{(X_L - X_C)^2 + R^2}$.