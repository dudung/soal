---
layout: soal
author: viridi
title: "0040"
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["svg", "mathjax", "html", "markdown"]
date: 2021-03-13 12:39:00 +07
permalink: /soal/0040
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/04/2021-03-13-mathjax-in-svg.md
ref: https://stackoverflow.com/a/15973585
---
Persamaan yang ditampilkan dengan menggunakan MathJax dapat disipkan dalam suatu berkas SVG sehingga memberikan hasil sebagai berikut ini.

<svg width="300" height="300" style="margin:auto; display:block;">
<foreignObject x="75" y="135" width="200" height="100">
$x^2 + y^2 + z^2 = R^2$
</foreignObject>

<path d="M 20,150 a 130,130 0 0,0 260,0 a 130,130 0 0,0 -260,0" fill="none" stroke="#44f" stroke-width="1" />

<path d="M 150,20 a 40,130 0 0,0 0,260" fill="none" stroke="#44f" stroke-width="1" />
<path d="M 150,20 a 40,130 0 0,1 0,260" fill="none" stroke="#44f" stroke-width="1" stroke-dasharray="4 2" />

<path d="M 20,150 a 130,40 0 0,0 260,0" fill="none" stroke="#44f" stroke-width="1" />
<path d="M 20,150 a 130,40 0 0,1 260,0" fill="none" stroke="#44f" stroke-width="1" stroke-dasharray="4 2" />

<circle cx="20" cy="150" r="2" stroke="black" />
<circle cx="280" cy="150" r="2" fill="black" />

<circle cx="150" cy="20" r="2" stroke="black" />
<circle cx="150" cy="280" r="2" stroke="black" />

<circle cx="188" cy="112" r="2" stroke="black" />
<circle cx="112" cy="188" r="2" stroke="black" />
</svg>

Untuk menyisipkan persamaan berbentuk $x^2 + y^2 + z^2 = R^2$ tersebut dalam gambar di atas, dapat digunakan elemen tertentu dalam SVG, yaitu

<ol type="A">
<li><tt>&lt;glyph&gt;</tt>.
<li><tt>&lt;text&gt;</tt>.
<li><tt>&lt;image&gt;</tt>.
<li><tt>&lt;foreignObject&gt;</tt>.
<li><tt>&lt;g&gt;</tt>.
