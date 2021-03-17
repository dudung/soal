---
layout: soal
author: viridi
title: "0012"
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: physics
tags: ["discriminant", "quadratic equation", "python"]
date: 2021-03-10 13:46:00 +07
permalink: /soal/0012
src: https://github.com/butiran/butiran.github.io/commits/master/_posts/soal/01/2021-03-10-discriminant-python.md
ref: https://www.britannica.com/science/discriminant
---
Suatu program sederhana dalam bahasa pemrograman Python berikut

```python
a = 1
b = -6
c = 5

print("Equation\n", a, "x^2 + ", b, "x + ", c, sep="")
print();

D = b * b - 4 * a * c

print("Discriminant\nD = ", D)
print()

print("Comment")
if D > 0:
	print("There are two roots")
else:
	if D == 0:
		print("There is one double root")
	else:
		print("There is not any real root")
```

berfungsi untuk menghitung diskriminan dari suatu persamaan kuadrat $ax^2 + bx + c = 0$. Bila ingin diperoleh hasil sebagai berikut

```batch
Equation
1x^2 + -4x + 4

Discriminant
D =  0

Comment
There is one double root
```

nilai-nilai $c$, $a$, $b$ adalah 

<ol type="A">
<li> $5$, $1$, $-6$.
<li> $1$, $-6$, $-5$.
<li> $2$, $-4$, $4$.
<li> $4$, $1$, $-4$.
<li> $1$, $-4$, $4$.
