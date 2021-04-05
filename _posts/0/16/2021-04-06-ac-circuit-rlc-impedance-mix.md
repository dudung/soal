---
layout: soal
author: viridi
title: "0168"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["impedance", "rlc", "ac", "parallel", "alternating current", "fi1202", "2020-1"]
date: 2021-04-06 05:06:00 +07
permalink: /0168
src: https://github.com/dudung/soal/commits/master/_posts/0/16/2021-04-06-ac-circuit-rlc-impedance-mix.md
ref: https://getcalc.com/electrical-impedence-calculator.htm
---
Terdapat gabungan rangkaian paralel dan seri arus bolak-balik yang selalu terdiri dari sumber $S$ (amplitudo tegangan $V_S$, amplitudo arus $I_S$, frekuensi $f$), resistor $R$, induktor $L$, dan kapasitor $L$.

Terdapat kode untuk rangkaian dan impedansi sebagai berikut.

**Kode** | **Komponen** | **Rangkaian**
ACM0 | RLC | seri-paralel
ACM1 | RLC | seri
ACM2 | RLC | paralel

**Kode** | **Impedansi**
Z0 | $\displaystyle \frac1Z = \sqrt{\frac1{R^2} + \left( \frac1{X_L} - \frac1{X_C} \right)^2}$
Z1 | $\displaystyle Z = \sqrt{X_C^2 + \frac1{\frac1{R^2} + \frac1{X_L^2}}}$
Z2 | $\displaystyle Z = \sqrt{R^2 + (X_L - X_C)^2}$

Pasangan yang tepat dari rangkaian seri dan impedansi rangkaiannya adalah

<ol type="A">
<li>ACM0 -- Z0.
<li>ACM1 -- Z1.
<li>ACM2 -- Z2.
<li>ACM0 -- Z1.
<li>ACM1 -- Z0.
