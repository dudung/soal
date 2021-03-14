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

<svg width="500" height="300">
	<style type="text/css">
		svg { border: 1px black dashed; }
		foreignObject { border: 1px black dashed; }
	</style>
	<use xlink:href="#sphere-3-circles" transform="scale(0.5)" />
	<use xlink:href="#xyz-axis" x="170" y="75" class="black" />
	<g transform="translate(240, 25)">
		<use xlink:href="#h-spring" x="10" y="18" class="black-outline"/>
		<use xlink:href="#block" x="130" y="10" class="white" id="moving-block" />
		<use xlink:href="#floor" x="10" y="50" />
		<use xlink:href="#left-wall" />
		<use xlink:href="#arr50px" transform="translate(150,30) rotate(90)" stroke="green" fill="green" />
		<use xlink:href="#arr50px" transform="translate(160,100) rotate(-90)" stroke="red" fill="red" />
		<foreignObject x="130" y="80" width="15" height="25">
		$\vec{w}$
		</foreignObject>
		<foreignObject x="165" y="70" width="15" height="25">
		$\vec{N}$
		</foreignObject>
		<foreignObject x="145" y="-15" width="15" height="25">
		$m$
		</foreignObject>
		<foreignObject x="70" y="-5" width="15" height="25">
		$k$
		</foreignObject>
	</g>
	<g transform="translate(20, 90)">
		<use xlink:href="#xyz-axis" x="10" y="190" class="black" />
		<path d="M60,130 q150,-200 300,50" class="red-curve" />
		<use xlink:href="#point" x="60" y="130" class="black" />
		<use xlink:href="#point" x="360" y="180" class="black" />
		<use xlink:href="#point" x="195" y="42" class="black" />
		<foreignObject x="30" y="140" width="55" height="25">
		$(x_0, y_0)$
		</foreignObject>
		<foreignObject x="165" y="10" width="55" height="25">
		$(x_1, y_1)$
		</foreignObject>
		<foreignObject x="290" y="170" width="55" height="25">
		$(x_2, y_2)$
		</foreignObject>
		<foreignObject x="125" y="90" width="120" height="25">
		$y = ax^2 + bx + c$
		</foreignObject>
	</g>
	<g transform="translate(400, 270)">
		<use xlink:href="#arr50px" transform="translate(0,0) rotate(0)" stroke="blue" fill="blue" />
		<use xlink:href="#arr50px" transform="translate(50,0) rotate(-45)" stroke="green" fill="green" />
		<use xlink:href="#arr50px" transform="translate(85,-35) rotate(-90)" stroke="red" fill="red" />
		<use xlink:href="#arr50px" transform="translate(85,-85) rotate(-135)" stroke="yellow" fill="yellow" />
		<use xlink:href="#arr50px" transform="translate(50,-120) rotate(-180)" stroke="magenta" fill="magenta" />
		<use xlink:href="#arr50px" transform="translate(0,-120) rotate(-225)" stroke="cyan" fill="cyan" />
	</g>
</svg>

dapat ditampilkan dengan hanya menggunakan code snippet berikut

```html
```

yang menunjukkan bahwa beberapa bentuk tersebut telah didefinisikan menggunakan elemen SVG `<defs>` dan kemudian dipanggil dengan elemen SVG `<use>`.
