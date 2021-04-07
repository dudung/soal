---
layout: soal
author: viridi
title: "0178"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["genetic algorithm", "terminology", "crossover", "fi3201", "2020-2"]
date: 2021-04-07 12:04:00 +07
permalink: /0178
src: https://github.com/dudung/soal/commits/master/_posts/0/17/2021-04-07-ga-terminology-8.md
ref: https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_fundamentals.htm
---

Untuk membentuk dua kromosom baru (anak) dari dua kromosom yang sebelumnya telah ada dalam populasi (induk) dapat dilakukan proses crossover gen-gen pada kedua induk, sebagaimana diilustrasikan di bawah ini untuk penyusunan tiga obyek dalam suatu ruangan. Obyek A dinyatakan dengan warna $\color{lightblue} \blacksquare$, bahan B dengan warna $\color{magenta} \blacksquare$ dan bahan C dengan warna $\color{lightgreen} \blacksquare$.

Induk | Fenotip | Genotip | Genotip | Fenotip | Anak
I1 | ![]({{site.baseurl}}/assets/img/0/17/0178a.png) | `4114344` | `4111344` | ![]({{site.baseurl}}/assets/img/0/17/0178c.png) | A1
I2 | ![]({{site.baseurl}}/assets/img/0/17/0178b.png) | `1111314` | `1114314` | ![]({{site.baseurl}}/assets/img/0/17/0178d.png) | A2

Dengan `|` adalah posisi crossover dilakukan, pernyataan yang tepat terkait dengan crossover pada gambar di atas adalah

<ol type="A">
<li>I1 = <code>411|43|44</code> dan I2 = <code>111|13|14</code>.
<li>I1 = <code>411|4344</code> dan I2 = <code>111|1314</code>.
<li>I1 = <code>41143|44</code> dan I2 = <code>11113|14</code>.
<li>I1 = <code>41|14344</code> dan I2 = <code>11|11314</code>.
<li>I1 = <code>4114|344</code> dan I2 = <code>1111|314</code>.