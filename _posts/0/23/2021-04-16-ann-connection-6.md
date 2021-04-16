---
layout: soal
author: viridi
title: "0237"
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
date: 2021-04-16 09:37:00 +07
permalink: /0237
src: https://github.com/dudung/soal/commits/master/_posts/0/23/2021-04-16-ann-connection-6.md
ref: https://hackernoon.com/everything-you-need-to-know-about-neural-networks-8988c3ee4491
---
Suatu arsitektur jaringan saraf tiruan (JST) berjenis feed forward terdiri beberapa neuron (node) masukan ($\LARGE \color{#ffcc00} \bullet$), beberapa neuron tersembunyi ($\LARGE \color{#66cc00} \bullet$) dalam tiap layer tersembunyi, dan beberapa neuron keluaran ($\LARGE \color{#ff6600} \bullet$).

![]({{site.baseurl}}/assets/img/0/23/0231.png)

Dengan menggunakan bahasa pemrograman Python dapat dituliskan suatu list sebagai berikut ini

```python
neuron = [
	[0.5, 0.2, 0.3, 1],
	[0, 1, 0, 1],
	[0, 0, 0, 1, 1],
	[1, 0, 0],
	[1]
]
```

yang terkait dengan gambar arsitektur JST di atas. Bila $x_{21} = 0$, $x_{35} = 1$, dan $x_{42} = 0$, maka yang benar adalah

<ol type="A">
<li>$x_{11} = 1$.
<li>$x_{51} = 0$.
<li>$x_{41} = 0$.
<li>$x_{43} = 1$.
<li>$x_{24} = 1$.
