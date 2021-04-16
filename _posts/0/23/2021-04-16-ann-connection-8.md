---
layout: soal
author: viridi
title: "0239"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["artificial neural network", "ann", "feed forward", "connection", "weight", "layer", "node", "neuron", "list", "python", "fi3201", "2020-2"]
date: 2021-04-16 10:04:00 +07
permalink: /0239
src: https://github.com/dudung/soal/commits/master/_posts/0/23/2021-04-16-ann-connection-8.md
ref: https://hackernoon.com/everything-you-need-to-know-about-neural-networks-8988c3ee4491
---
Suatu arsitektur jaringan saraf tiruan (JST) berjenis feed forward terdiri beberapa neuron (node) masukan ($\LARGE \color{#ffcc00} \bullet$), beberapa neuron tersembunyi ($\LARGE \color{#66cc00} \bullet$) dalam tiap layer tersembunyi, dan beberapa neuron keluaran ($\LARGE \color{#ff6600} \bullet$).

![]({{site.baseurl}}/assets/img/0/23/0231.png)

Dengan menggunakan bahasa pemrograman Python dapat dituliskan suatu list sebagai berikut ini

```python
weight = [
	[ 
		[0.1, 0.2, 0.3, 0.4],
		[0.5, 0.6, 0.7, 0.8],
		[0.9, 0.8, 0.7, 0.6],
		[0.4, 0.3, 0.2, 0.1],
	],
	[
		[0.1, 0.2, 0.3, 0.4],
		[0.5, 0.6, 0.7, 0.8],
		[0.9, 0.8, 0.7, 0.6],
		[0.4, 0.3, 0.2, 0.1],
		[0.3, 0.5, 0.7, 0.9],
	],
	[
		[0.1, 0.6, 0.7, 0.6, 0.5],
		[0.2, 0.5, 0.8, 0.7, 0.4],
		[0.3, 0.4, 0.9, 0.8, 0.3],
	],
	[
		[0.1, 0.2, 0.3],
	]
]
```

yang merupakan salah satu cara menuliskan bobot terkait dengan gambar arsitektur JST di atas. Bila $w_{2111} = 0.1$, $w_{3524} = 0.9$, dan $w_{5143} = 0.3$, maka $w_{3322}$ adalah

<ol type="A">
<li>$0.9$.
<li>$0.8$.
<li>$0.7$.
<li>$0.6$.
<li>$0.3$.
