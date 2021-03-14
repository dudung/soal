---
layout: soal
author: viridi
title: "0048"
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["svg", "html", "js"]
date: 2021-03-14 14:16:00 +07
permalink: /soal/0048
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/04/2021-03-14-svg-js-spring.md
ref: 
---
Suatu bentuk didefinisikan dengan elemen SVG `<dev>` sebagaimana diberikan oleh code snippet berikut.

<svg style="display: none;">
	<style type="text/css">
	.black-outline { stroke: black; fill: none; stroke-width: 2px; }
	.white { stroke: black; fill: #fff; stroke-width: 2px; }
	</style>
	<defs>
		<g id="h-spring">
			<desc>w = 120, h = 24</desc>
			<path d="M0,12 h16 l8,-12 l8,24, l8,-24 l8,24, l8,-24 l8,24, l8,-24 l8,24, l8,-24 l8,24, l8,-12 h16" />
		</g>
		<g id="block">
			<desc>w = 40, h = 40</desc>
			<path d="M0,0 v40 h40 v-40 z" />
		</g>
		<g id="floor">
			<desc>w = 200, h = 10</desc>
			<rect x1="0" y1="0" width="200" height="10" stroke="none" fill="#ddd"	/>
			<line x1="0" y1="0" x2="200" y2="0" stroke="black" />
		</g>
		<g id="left-wall">
			<desc>w = 10, h = 50</desc>
			<rect x1="0" y1="0" width="10" height="50" stroke="none" fill="#ddd"	/>
			<line x1="10" y1="0" x2="10" y2="50" stroke="black" />
		</g>
	</defs>
</svg>

<svg width="200" height="60">
	<style type="text/css">
	//svg { border: 1px black dashed; }
	//foreignObject { border: 1px black solid; }
	</style>
	<use xlink:href="#h-spring" x="10" y="18" class="black-outline" />
	<use xlink:href="#block" x="130" y="10" class="white" id="moving-block" />
	<use xlink:href="#floor" x="10" y="50" />
	<use xlink:href="#left-wall" />
</svg>

<script>
function change(x) {
	mb = document.getElementById("moving-block");
}
</script>

{% comment %}
<!-- 20210314.1357 It fails and not understandable -->
<svg>
	<defs>
		<!-- url https://stackoverflow.com/a/46802047 -->
		<pattern id="dlines1" height="10" width="10" patternUnits="userSpaceOnUse">
			<!--line x1="0" y1="4" x2="5" y2="4" stroke-width="2" stroke="black"/-->
			<line x1="0" y1="10" x2="10" y2="0" stroke-width="1" stroke="#888" />
		</pattern>
		<!-- url https://developer.mozilla.org/en-US/docs/Web/SVG/Element/pattern -->
		<pattern id="dlines2" viewBox="0,0,10,10" width="10%" height="10%">
			<!--polygon points="0,0 2,5 0,10 5,8 10,10 8,5 10,0 5,2" /-->
			<path d="M0,10 l10,-10" stroke="#888" stroke-width="1px" />
		</pattern>
		<g id="floor">
			<rect x="0" y="0" width="40" height="40" fill="url(#dlines2)" />
		</g>
	</defs>
	<use xlink:href="#floor" x="0" y="0" transform="scale(2, 0.5)"/>
</svg>
{% endcomment %}
