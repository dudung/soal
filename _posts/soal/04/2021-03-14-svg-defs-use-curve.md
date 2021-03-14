---
layout: soal
author: viridi
title: "0045"
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["svg", "referencing", "defs", "html", "curve"]
date: 2021-03-14 07:57:00 +07
permalink: /soal/0045
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/04/2021-03-14-svg-defs-use-curve.md
ref: http://tutorials.jenkov.com/svg/defs-element.html
---
Telah didefinisikan beberapa bentuk SVG dengan memanfaatkan elemen `<defs>` agar digunakan untuk menampilkan sumbu koordinat, titik, dan kurva.


<svg style="display: none;">
	<style type="text/css">
	.black { stroke: #000; fill: #000; stroke-width: 1.25px; }
	.red-curve { stroke: #f00; fill: none; stroke-width: 2.5px; }
	.variable {
		font-family: times;
		font-size: 20px;
		font-style: italic;
		fill: black;
		stroke: none;
	}
	</style>
	<defs>
		<path id="arr50px" d="M0,0 h50 l-10,-3 v6 l10,-3" />
		<g id="3d-axis">
			<use xlink:href="#arr50px" />
			<use xlink:href="#arr50px" transform="rotate(-90)" />
			<circle x="0" y="0" r="5" fill="white" />
			<circle x="0" y="0" r="2" />
		</g>
		<g id="xyz-axis">
			<use xlink:href="#3d-axis" />
			<text x="55" y="5" class="variable">x</text>
			<text x="-5" y="-60" class="variable">y</text>
			<text x="-20" y="15" class="variable">z</text>
		</g>
		<g id="yzx-axis">
			<use xlink:href="#3d-axis" />
			<text x="55" y="5" class="variable">y</text>
			<text x="-5" y="-60" class="variable">z</text>
			<text x="-20" y="15" class="variable">x</text>
		</g>
		<g id="zxy-axis">
			<use xlink:href="#3d-axis" />
			<text x="55" y="5" class="variable">z</text>
			<text x="-5" y="-60" class="variable">x</text>
			<text x="-20" y="15" class="variable">y</text>
		</g>
		<circle id="point" cx="0" cy="0" r="3" stroke="none" />
	</defs>
</svg>

<svg width="400" height="200">
	<style type="text/css">
		//svg { border: 1px black solid; }
		//foreignObject { border: 1px black solid; }
	</style>
	<use xlink:href="#xyz-axis" x="10" y="190" class="black" />
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
	<path d="M60,130 q150,-200 300,50" class="red-curve" />
	<use xlink:href="#point" x="60" y="130" class="black" />
	<use xlink:href="#point" x="360" y="180" class="black" />
	<use xlink:href="#point" x="195" y="42" class="black" />
</svg>

Bentuk-bentuk ini kemudian digunakan untuk menghasilkan gambar di atas saat dipanggil dengan cara

```svg
<svg width="400" height="200">
	<use xlink:href="#xyz-axis" x="10" y="190" class="black" />
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
	<path id="curve" d="M60,130 q150,-200 300,50" class="red-curve" />
	<use xlink:href="#point" x="60" y="130" class="black" />
	<use xlink:href="#point" x="360" y="180" class="black" />
	<use xlink:href="#point" x="195" y="42" class="black" />
</svg>
```

pada bagian lain suatu dokumen HTML. Bentuk-bentuk yang telah didefinisikan sebelumnya adalah

<ol type="A">
<li> <tt>curve</tt> dan <tt>point</tt>.
<li> <tt>point</tt> dan <tt>xyz-axis</tt>.
<li> <tt>foreignObject</tt>.
<li> <tt>curve</tt> dan <tt>xyz-axis</tt>.
<li> tidak dapat dijelaskan dari code snippet yang diberikan.
