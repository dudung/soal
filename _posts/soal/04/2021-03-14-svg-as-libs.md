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
ref: https://vecta.io/blog/best-way-to-embed-svg
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
	svg { border: 1px black dashed; }
	foreignObject { border: 1px black dashed; }
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
		<g id="sphere-3-circles">
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
		</g>
	</defs>
</svg>

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
