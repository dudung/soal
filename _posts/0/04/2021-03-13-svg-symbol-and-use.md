---
layout: soal
author: viridi
title: "0043"
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["svg", "referencing", "symbol", "html"]
date: 2021-03-13 20:52:00 +07
permalink: /soal/0043
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/04/2021-03-13-svg-symbol-and-use.md
ref: https://css-tricks.com/svg-symbol-good-choice-icons/
---
Perhatikan isi suatu elemen SVG

```svg
<svg style="display: none;">

<symbol id="xyz-axis" viewBox="-18 -50 90 50">
	<title>xyz axis</title>
	<desc>Icon of xyz axis x right y up, z out</desc>
	<style type="text/css">
	#arrow {stroke: black; stroke-width: 1.5px;}
	.variable {font: italic 16px times; fill: black;}
	</style>
	<path id="arrow" d="M0,0 h50 l-10,-3 v6 l10,-3" />
	<use xlink:href="#arrow" transform="rotate(-90)" />
	<circle cx="0" cy="0" r="5" stroke="black" fill="white" />
	<circle cx="0" cy="0" r="2" stroke="black" fill="black" />
	<text x="60" y="5" class="variable">x</text>
	<text x="-5" y="-60" class="variable">y</text>
	<text x="-15" y="15" class="variable">z</text>
</symbol>

<symbol id="yzx-axis" viewBox="-18 -50 90 50">
	<title>yzx axis</title>
	<desc>Icon of yzx axis y right z up, x out</desc>
	<style type="text/css">
	#arrow {stroke: black; stroke-width: 1.5px;}
	.variable {font: italic 16px times; fill: black;}
	</style>
	<path id="arrow" d="M0,0 h50 l-10,-3 v6 l10,-3" />
	<use xlink:href="#arrow" transform="rotate(-90)" />
	<circle cx="0" cy="0" r="5" stroke="black" fill="white" />
	<circle cx="0" cy="0" r="2" stroke="black" fill="black" />
	<text x="60" y="5" class="variable">y</text>
	<text x="-5" y="-60" class="variable">z</text>
	<text x="-15" y="15" class="variable">x</text>
</symbol>

<symbol id="zxy-axis" viewBox="-18 -50 90 50">
	<title>yzx axis</title>
	<desc>Icon of zxy axis z right x up, y out</desc>
	<style type="text/css">
	#arrow {stroke: black; stroke-width: 1.5px;}
	.variable {font: italic 16px times; fill: black;}
	</style>
	<path id="arrow" d="M0,0 h50 l-10,-3 v6 l10,-3" />
	<use xlink:href="#arrow" transform="rotate(-90)" />
	<circle cx="0" cy="0" r="5" stroke="black" fill="white" />
	<circle cx="0" cy="0" r="2" stroke="black" fill="black" />
	<text x="60" y="5" class="variable">z</text>
	<text x="-5" y="-60" class="variable">x</text>
	<text x="-15" y="15" class="variable">y</text>
</symbol>

</svg>
```

yang akan menghasilkan gambar berikut ini

<svg style="display: none;">

<symbol id="xyz-axis" viewBox="-18 -50 90 50">
	<title>xyz axis</title>
	<desc>Icon of xyz axis x right y up, z out</desc>
	<style type="text/css">
	#arrow {stroke: black; stroke-width: 1.5px;}
	.variable {font: italic 16px times; fill: black;}
	</style>
	<path id="arrow" d="M0,0 h50 l-10,-3 v6 l10,-3" />
	<use xlink:href="#arrow" transform="rotate(-90)" />
	<circle cx="0" cy="0" r="5" stroke="black" fill="white" />
	<circle cx="0" cy="0" r="2" stroke="black" fill="black" />
	<text x="60" y="5" class="variable">x</text>
	<text x="-5" y="-60" class="variable">y</text>
	<text x="-15" y="15" class="variable">z</text>
</symbol>

<symbol id="yzx-axis" viewBox="-18 -50 90 50">
	<title>yzx axis</title>
	<desc>Icon of yzx axis y right z up, x out</desc>
	<style type="text/css">
	#arrow {stroke: black; stroke-width: 1.5px;}
	.variable {font: italic 16px times; fill: black;}
	</style>
	<path id="arrow" d="M0,0 h50 l-10,-3 v6 l10,-3" />
	<use xlink:href="#arrow" transform="rotate(-90)" />
	<circle cx="0" cy="0" r="5" stroke="black" fill="white" />
	<circle cx="0" cy="0" r="2" stroke="black" fill="black" />
	<text x="60" y="5" class="variable">y</text>
	<text x="-5" y="-60" class="variable">z</text>
	<text x="-15" y="15" class="variable">x</text>
</symbol>

<symbol id="zxy-axis" viewBox="-18 -50 90 50">
	<title>yzx axis</title>
	<desc>Icon of zxy axis z right x up, y out</desc>
	<style type="text/css">
	#arrow {stroke: black; stroke-width: 1.5px;}
	.variable {font: italic 16px times; fill: black;}
	</style>
	<path id="arrow" d="M0,0 h50 l-10,-3 v6 l10,-3" />
	<use xlink:href="#arrow" transform="rotate(-90)" />
	<circle cx="0" cy="0" r="5" stroke="black" fill="white" />
	<circle cx="0" cy="0" r="2" stroke="black" fill="black" />
	<text x="60" y="5" class="variable">z</text>
	<text x="-5" y="-60" class="variable">x</text>
	<text x="-15" y="15" class="variable">y</text>
</symbol>

</svg>

<svg width="100" height="100">
<use xlink:href="#xyz-axis" />
</svg>

<svg width="100" height="100">
<use xlink:href="#yzx-axis" />
</svg>

<svg width="100" height="100">
<use xlink:href="#zxy-axis" />
</svg>

saat dipanggil dengan

```
<svg width="100" height="100">
<use xlink:href="#xyz-axis" />
</svg>

<svg width="100" height="100">
<use xlink:href="#yzx-axis" />
</svg>

<svg width="100" height="100">
<use xlink:href="#zxy-axis" />
</svg>
```

pada bagian lain suatu dokumen HTML. Pemanfaatan elemen `<symbol>` yang paling tepat adalah untuk
 
<ol type="A">
<li>icon.
<li>bagian dari suatu gambar.
<li>icon dan bagian dari suatu gambar.
<li>bukan icon ataupun bagian dari suatu gambar
<li>lain-lain.
