---
layout: soal
author: viridi
title: "0046"
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["svg", "referencing", "defs", "html", "js"]
date: 2021-03-14 09:13:00 +07
permalink: /soal/0046
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/04/2021-03-14-svg-defs-use-js.md
ref: http://xahlee.info/js/js_scritping_svg_basics.html
---
Elemen SVG dalam suatu halaman HTML dapat dibuat dengan menggunakan JavaScript (JS). SVG merupakan suatu XML, atau dapat dikatakan mirip dengan HTML tetapi dengan sintaks yang lebih ketat.

<div id="container1"></div>

<script>
var btn = document.createElement("button");
btn.innerHTML = "Click me for nothing";
btn.style.color = "#88f";
var container1 = document.getElementById("container1");
container1.appendChild(btn);
</script>

Dengan terlebih dahulu mendefinisikan suatu elemen HTML `<div>` dengan `id="container1"` code snippet berikut

```javascript
<script>
var btn = document.createElement("button");
btn.innerHTML = "Click me for nothing";
btn.style.color = "#88f";
var container1 = document.getElementById("container1");
container1.appendChild(btn);
</script>
```

dapat digunakan untuk menghasilkan tombol di atas. Untuk suatu elemen SVG element HTML `<div>` dengan `id="container2"` dibuat untuk tempat gambar berikut.

<div id="container2"></div>

<script>
var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
var circ1 = document.createElementNS("http://www.w3.org/2000/svg", "circle");
var circ2 = document.createElementNS("http://www.w3.org/2000/svg", "circle");
var container2 = document.getElementById("container2");

svg.setAttribute("width", "200");
svg.setAttribute("height", "100");

circ1.setAttribute("cx", "50");
circ1.setAttribute("cy", "50");
circ1.setAttribute("r", "49");
circ1.setAttribute("stroke", "#000");
circ1.setAttribute("stroke-width", "2");
circ1.setAttribute("fill", "#eee");

circ2.setAttribute("cx", "160");
circ2.setAttribute("cy", "50");
circ2.setAttribute("r", "30");
circ2.setAttribute("stroke", "#f00");
circ2.setAttribute("stroke-width", "1");
circ2.setAttribute("stroke-dasharray", "8 2 4 2");
circ2.setAttribute("fill", "#fee");

container2.appendChild(svg);
svg.appendChild(circ1);
svg.appendChild(circ2);
</script>

Gambar di atas diperoleh dengan code snippet berikut

```javascript
<script>
var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
var circ1 = document.createElementNS("http://www.w3.org/2000/svg", "circle");
var circ2 = document.createElementNS("http://www.w3.org/2000/svg", "circle");
var container2 = document.getElementById("container2");

svg.setAttribute("width", "200");
svg.setAttribute("height", "100");

circ1.setAttribute("cx", "50");
circ1.setAttribute("cy", "50");
circ1.setAttribute("r", "49");
circ1.setAttribute("stroke", "#000");
circ1.setAttribute("stroke-width", "2");
circ1.setAttribute("fill", "#eee");

circ2.setAttribute("cx", "160");
circ2.setAttribute("cy", "50");
circ2.setAttribute("r", "30");
circ2.setAttribute("stroke", "#f00");
circ2.setAttribute("stroke-width", "1");
circ2.setAttribute("stroke-dasharray", "8 2 4 2");
circ2.setAttribute("fill", "#fee");

container2.appendChild(svg);
svg.appendChild(circ1);
svg.appendChild(circ2);
</script>
```

yang dipanggil setelah elemen `<div>` terkait didefinisikan.

Perbedaan antara membuat suatu elemen HTML DOM dan suatu SVG terletak pada

<ol type="A">
<li>pembuatan obyek.
<li>penambahan obyek child ke obyek parent.
<li>pengubahan atribut suatu elemen.
<li>ketiga jawaban di atas benar.
<li>jawab A dan C benar.
