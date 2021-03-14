---
layout: soal
author: viridi
title: "0049"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: true
category: physics
tags: ["svg", "html", "js", "button", "click"]
date: 2021-03-14 17:09:00 +07
permalink: /soal/0049
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/04/2021-03-14-svg-as-libs.md
ref: https://vecta.io/blog/best-way-to-embed-svg
---
Beberapa bentuk dalam gambar di bawah ini

<svg width="600" height="300">
	<use xlink:href="#sphere-3-circles" transform="scale(0.5)" />
</svg>

dapat ditampilkan dengan hanya menggunakan code snippet berikut

```html
```

yang menunjukkan bahwa beberapa bentuk tersebut telah didefinisikan menggunakan elemen SVG `<defs>` dan kemudian dipanggil dengan elemen SVG `<use>`.

<svg width="400" height="200">
	<use xlink:href="#3d-axis" x="20" y="60" class="black" />
	<use xlink:href="#xyz-axis" x="100" y="120" class="black" />
	<use xlink:href="#yzx-axis" x="200" y="80" class="black" />
	<use xlink:href="#zxy-axis" x="300" y="150" class="black" />
	<foreignObject x="75" y="150" width="150" height="25">
	$ax + by + cz + d = 0$
	</foreignObject>
</svg>

<svg width="300" height="300">
	<use xlink:href="#sphere-3-circles" />
	<foreignObject x="75" y="135" width="130" height="25">
	$x^2 + y^2 + z^2 = R^2$
	</foreignObject>
</svg>

<svg width="400" height="200">
	<use xlink:href="#xyz-axis" x="10" y="190" class="black" />
	<path d="M60,130 q150,-200 300,50" class="red-curve" />
	<use xlink:href="#point" x="60" y="130" class="black" />
	<use xlink:href="#point" x="360" y="180" class="black" />
	<use xlink:href="#point" x="195" y="42" class="black" />
	<foreignObject x="30" y="140" width="60" height="25">
	$(x_0, y_0)$
	</foreignObject>
	<foreignObject x="165" y="10" width="60" height="25">
	$(x_1, y_1)$
	</foreignObject>
	<foreignObject x="290" y="170" width="60" height="25">
	$(x_2, y_2)$
	</foreignObject>
	<foreignObject x="125" y="90" width="140" height="25">
	$y = ax^2 + bx + c$
	</foreignObject>
</svg>

<svg width="250" height="60">
	<use xlink:href="#h-spring" y="18" class="black-outline" id="spring" transform="translate(10)"/>
	<use xlink:href="#block" x="130" y="10" class="white" id="moving-block" />
	<use xlink:href="#floor" x="10" y="50" />
	<use xlink:href="#left-wall" />
</svg>
