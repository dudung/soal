---
layout: soal
author: viridi
title: "0042"
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["svg", "referencing", "html"]
date: 2021-03-13 17:55:00 +07
permalink: /soal/0042
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/04/2021-03-13-svg-defs-and-use.md
ref: https://www.sarasoueidan.com/blog/structuring-grouping-referencing-in-svg/
---
Perhatikan isi suatu berkas SVG

```svg
<svg width="300" height="200">
<style type="text/css">
svg {
	background:#f8f8f8;
	margin:auto; display:block;
	border:1px #888 dashed;
}
#tire {fill:#000;}
#body {fill:#c22;}
#newcar {stroke:#cc0; stroke-width:4px;}
</style>
<defs>
	<g id="car">
		<path id="body" d="M10,10 h50 l30,10 v10 h-85 v-15 z" />
		<circle id="tire" cx="20" cy="30" r="8" />
		<circle id="tire" cx="70" cy="30" r="8" />
	</g>
</defs>
<use xlink:href="#car" x="30" y="20" />
<use xlink:href="#car" x="-150" y="50" transform="scale(-1.5,1.5)" />
<use id="newcar" xlink:href="#car" x="120" y="150" />
</svg>
```

yang menghasilkan gambar berikut ini.

<svg width="300" height="200">
<style type="text/css">
svg{
	background:#f8f8f8;
	margin:auto; display:block;
	border:1px #888 dashed;
}
#tire {fill:#000;}
#body {fill:#c22;}
#newcar {stroke:#cc0; stroke-width:4px;}
</style>
<defs>
	<g id="car">
		<path id="body" d="M10,10 h50 l30,10 v10 h-85 v-15 z" />
		<circle id="tire" cx="20" cy="30" r="8" />
		<circle id="tire" cx="70" cy="30" r="8" />
	</g>
</defs>
<use xlink:href="#car" x="30" y="20" />
<use xlink:href="#car" x="-150" y="50" transform="scale(-1.5,1.5)" />
<use id="newcar" xlink:href="#car" x="120" y="150" />
</svg>

Elemen SVG yang berfungsi untuk mendefinisikan suatu elemen baru tanpa menampilkannya dan elemen SVG yang kemudian digunakan untuk menampilkan elemen yang sudah didefinisikan tersebut adalah

<ol type="A">
<li><tt>&lt;use&gt;</tt> dan <tt>&lt;g&gt;</tt>.
<li><tt>&lt;defs&gt;</tt> dan <tt>&lt;g&gt;</tt>.
<li><tt>&lt;defs&gt;</tt> dan <tt>&lt;use&gt;</tt>.
<li><tt>&lt;style&gt;</tt> dan <tt>&lt;g&gt;</tt>.
<li><tt>&lt;use&gt;</tt> dan <tt>&lt;style&gt;</tt>.
