---
layout: soal
author: viridi
title: "0044"
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["svg", "referencing", "defs", "html"]
date: 2021-03-14 07:12:00 +07
permalink: /soal/0044
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/04/2021-03-14-svg-defs-and-use.md
ref: http://tutorials.jenkov.com/svg/defs-element.html
---
Suatu elemen SVG dengan isi

```svg
<svg style="display: none;">
	<style type="text/css">
	.black { stroke: #000; fill: #00; stroke-width: 1.25px; }
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
	</defs>
</svg>
```

digunakan untuk menghasilkan gambar berikut

<svg style="display: none;">
	<style type="text/css">
	.black { stroke: #000; fill: #00; stroke-width: 1.25px; }
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
	</defs>
</svg>

<svg width="400" height="200">
	<style type="text/css">
		//svg { border: 1px black solid; }
		//foreignObject { border: 1px black solid; }
	</style>
	<use xlink:href="#3d-axis" x="20" y="60" class="black" />
	<use xlink:href="#xyz-axis" x="100" y="120" class="black" />
	<foreignObject x="75" y="150" width="150" height="25">
	$x^2 + y^2 + z^2 = R^2$
	</foreignObject>
	<use xlink:href="#yzx-axis" x="200" y="80" class="black" />
	<use xlink:href="#zxy-axis" x="300" y="150" class="black" />
</svg>

saat dipanggil dengan

```svg
<svg width="400" height="200">
	<style type="text/css">
		//svg { border: 1px black solid; }
		//foreignObject { border: 1px black solid; }
	</style>
	<use xlink:href="#3d-axis" x="20" y="60" class="black" />
	<use xlink:href="#xyz-axis" x="100" y="120" class="black" />
	<foreignObject x="75" y="150" width="150" height="25">
	$x^2 + y^2 + z^2 = R^2$
	</foreignObject>
	<use xlink:href="#yzx-axis" x="200" y="80" class="black" />
	<use xlink:href="#zxy-axis" x="300" y="150" class="black" />
</svg>
```

pada bagian lain suatu dokumen HTML. Bentuk yang dapat digunakan dengan menggunakan elemen `<use>` adalah
 
<ol type="A">
<li> <tt>arr50px</tt>.
<li> <tt>3d-axis</tt>.
<li> <tt>arr50px</tt>, <tt>3d-axis</tt>.
<li> <tt>xyz-axis</tt>, <tt>yzx-axis</tt>, <tt>zxy-axis</tt>.
<li> semua bentuk di atas yang memiliki <tt>id</tt>.
