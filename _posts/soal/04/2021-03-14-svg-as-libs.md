---
layout: soal
author: viridi
title: "0049"
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["svg", "html", "js", "button", "click"]
date: 2021-03-14 17:09:00 +07
permalink: /soal/0049
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/04/2021-03-14-svg-as-libs.md
ref: https://www.w3schools.com/jsref/event_onclick.asp
---

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
	.black-outline { stroke: black; fill: none; stroke-width: 1px; }
	.white { stroke: black; fill: #fff; stroke-width: 2px; }
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
		<g id="h-spring">
			<desc>w = 120, h = 24</desc>
			<path d="M0,12 h16 l8,-12 l8,24, l8,-24 l8,24, l8,-24 l8,24, l8,-24 l8,24, l8,-24 l8,24, l8,-12 h16" />
		</g>
		<g id="block">
			<desc>w = 40, h = 40</desc>
			<path d="M0,0 v40 h40 v-40 z" />
		</g>
		<g id="floor">
			<desc>w = 240, h = 10</desc>
			<rect x1="0" y1="0" width="240" height="10" stroke="none" fill="#ddd"	/>
			<line x1="0" y1="0" x2="240" y2="0" stroke="black" />
		</g>
		<g id="left-wall">
			<desc>w = 10, h = 50</desc>
			<rect x1="0" y1="0" width="10" height="50" stroke="none" fill="#ddd"	/>
			<line x1="10" y1="0" x2="10" y2="50" stroke="black" />
		</g>
	</defs>
</svg>

<svg width="250" height="60">
	<style type="text/css">
	svg { border: 1px black dashed; }
	foreignObject { border: 1px black solid; }
	</style>
	<use xlink:href="#h-spring" y="18" class="black-outline" id="spring" transform="translate(10)"/>
	<use xlink:href="#block" x="130" y="10" class="white" id="moving-block" />
	<use xlink:href="#floor" x="10" y="50" />
	<use xlink:href="#left-wall" />
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
