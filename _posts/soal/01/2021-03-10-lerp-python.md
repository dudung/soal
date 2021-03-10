---
layout: soal
author: viridi
title: "0011"
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["linear interpolation", "python"]
date: 2021-03-10 12:48:00 +07
permalink: /soal/0011
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/00/2021-03-10-linear-interpolation.md
ref: https://en.wikipedia.org/w/index.php?oldid=1004343292
---
Suatu program sederhana dalam bahasa pemrograman Python berikut

```python
x1 = 1
y1 = 8
x2 = 5
y2 = 20

print("Known points")
print("x1 = ", x1, ", y1 = ", y1, sep="")
print("x2 = ", x2, ", y2 = ", y2, sep="")
print()

def f(x):
	m = (y2 - y1) / (x2 - x1)
	y = m * (x - x1) + y1
	return y

def g(y):
	m = (x2 - x1) / (y2 - y1)
	x = m * (y - y1) + x1
	return x

x = 3
y = f(x)
print("Interpolate y")
print("x = ", x, ", y = ", y, sep="")
print()

y = 11
x = g(y)
print("Interpolate x")
print("y = ", y, ", x = ", x, sep="")
```

berfungsi untuk menghitung nilai $x$ dan $y$ dari dua titik yang diketahui, yaitu $(1, 8)$ dan $(5, 20)$, dengan menggunakan metode interpolasi linier.

Bila kedua titik yang diketahui ingin diganti menjadi $(0, 10)$ dan $(10, 110)$, maka bagian program yang perlu diganti adalah

<ol type="A">
<li>x1 = 0, y1 = 10, x2 = 10, y2 = 110.
<li>x1 = 10, y1 = 10, x2 = 10, y2 = 110.
<li>x1 = 0, y1 = 10, x2 = 0, y2 = 110.
<li>x1 = 0, y1 = 110, x2 = 10, y2 = 0.
<li>x1 = 10, y1 = 10, x2 = 10, y2 = 0.