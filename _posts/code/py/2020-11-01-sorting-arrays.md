---
layout: post
author: viridi
title: sorting arrays
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: python
date: 2020-11-01 12:55:00 +07
tags: ["topics"]
permalink: /code/py/sorting-arrays
---
..

{% comment %}
A simple program writen in Python to produce Lissajous curve [[1](#ref1)] is presented here.


url https://jakevdp.github.io/PythonDataScienceHandbook/02.08-sorting.html

## Equation
In order to produce a Lissajous pattern in two-dimensional space, two equations are requires

\begin{equation}
\label{eqn:pyrdpf-x}
x(t) = A_x \sin \left( \frac{2\pi}{T_x} t + \phi_x \right)
\end{equation}
and
\begin{equation}
\label{eqn:pyrdpf-y}
y(t) = A_y \sin \left( \frac{2\pi}{T_y} t + \phi_y \right)
\end{equation}

with $A$ is amplitude, $T$ is periode, and $\phi$ is initial phase, where all are for both $x$ and $y$ directions.


## Parameters file
A parameters file with the following content

```batch
TITL 2d-Lissajous-pattern-generator
OUTF lissajous-pattern.png

AMPX 100
TPEX 3
PHAX 0

AMPY 100
TPEY 2
PHAY 1.57

TBEG 0
TEND 20
TSTP 0.0001
```

is designed for the program, that will open it and use the parameters value.


## Python code
A program written in Python 3 has following content

```python
# 
# lissajous.py
# Read parameters file and process its content to produce
# Lissajous pattern in PNG format
# 
# Sparisoma Viridi | https://github.com/dudung
# 
# Execute: python3 lissajous.py params.txt
# 
# 20200922
# 2108 Derive it from redpf2.py and plan to implement [1].
# 2152 Install NumPy through Cygwin.
# 2203 Install PIL through Cygwin python37-imaging package (x).
# 2226 Install for 37 NumPy and execute with python 37, ok.
# 2229 Test the example [1] and it works.
# 2242 Create empty white image 10x10.
# 20200923
# 0501 Change output from argv[2] to OUTF in parameters file.
# 0517 Create emty white PNG image with size (2Ax)x(2Ay).
# 0543 Change pixel color in two-dimensional array [3], pixels.
# 0553 Reduce Ax and Ay with 0.98 for better Lissajous curve.
# 1704 Remove out.png from execute information.
# 
# References
# 1. Jebby, "Answer to 'How to create image from a list of
#    pixel values in Python3?'", StackOverflow, 25 Oct 2017,
#    url https://stackoverflow.com/a/46924413 [20200922].
# 2. -, "https://wiki.python.org/moin/ForLoop", Python, url
#    https://wiki.python.org/moin/ForLoop [20200923].
# 3. -, "Python - 2D Array", TutorialsPoint, url https://www.
#    tutorialspoint.com/python_data_structure/python_2darray
#    .htm [20200923].
# 

# Import necessary modules
import sys
from PIL import Image
import numpy as np
import math

# Get command line arguments
argv = sys.argv

# Get parameters filename
fn = argv[1]

# Open parameters file
fp = open(fn, "r")

# Declare array
params = []

# Iterate throug line in opened file
for line in fp:
	# Remove trailing new line
	line2 = line.rstrip("\n")
	
	# Append line to params
	params.append(line2)

# Close file
fp.close()

# Get params
for p in params:
	b = p.split();
	if b:
		if b[0] == "AMPX": Ax = float(b[1])
		if b[0] == "AMPY": Ay = float(b[1])
		if b[0] == "TPEX": Tx = float(b[1])
		if b[0] == "TPEY": Ty = float(b[1])
		if b[0] == "PHAX": phx = float(b[1])
		if b[0] == "PHAY": phy = float(b[1])
		if b[0] == "TBEG": tbeg = float(b[1])
		if b[0] == "TEND": tend = float(b[1])
		if b[0] == "TSTP": dt = float(b[1])
		if b[0] == "OUTF": fn2 = b[1]

# Define default color
o = (255, 255, 255)
i = (255, 0, 0)

# Ilustrate plus or '+' in a PNG file -- not used
pixels = [
	[o, o, o, o, i, i, o, o, o, o],
	[o, o, o, o, i, i, o, o, o, o],
	[o, o, o, o, i, i, o, o, o, o],
	[o, o, o, o, i, i, o, o, o, o],
	[i, i, i, i, i, i, i, i, i, i],
	[i, i, i, i, i, i, i, i, i, i],
	[o, o, o, o, i, i, o, o, o, o],
	[o, o, o, o, i, i, o, o, o, o],
	[o, o, o, o, i, i, o, o, o, o],
	[o, o, o, o, i, i, o, o, o, o],
]

# Create empty image
pixels = []
for row in range(int(2 * Ay)):
	rows = []
	for col in range(int(2 * Ax)):
		rows.append(o)
	pixels.append(rows)

# Iterate from tbeg to tend with step dt
N = int((tend - tbeg)/dt)
for j in range(0, N + 1):
	t = round(tbeg + j * dt, 4)
	x = 0.98 * Ax * math.sin(2 * math.pi * t / Tx + phx)
	y = 0.98 * Ay * math.sin(2 * math.pi * t / Ty + phy)
	xx = int(Ax + x)
	yy = int(Ay - y)
	if xx in range(int(2 * Ax)) and yy in range(int(2 * Ay)):
		pixels[yy][xx] = i

# Convert the pixels into an array using numpy
array = np.array(pixels, dtype=np.uint8)

# Use PIL to create an image from the new array of pixels
new_image = Image.fromarray(array)
new_image.save(fn2)
```

which will be called using command line as

```
$ python3.8 lissajous.py params.txt
```

and produce `lissajous-pattern.png` file.


## Exercise
1. What is the name of parameters file? Show which part of the code that supports your answer.
2. In which part of the parameters file and the code you can find the output filename `lissajous-pattern.png`?
3. What is the result of the code for the given parameters file? Refer it to an image in the internet as the answer.
4. Compare the default result with an internet result [[2](#ref2)]. Can you confirm that those results are the same? Compare also with [[3](#ref3)].
5. See first row and third column from left in the first figure [[4](#ref4)]. Can you determine the parameters and produce the curve using `lissajous.py` code? Specify the parameters value.


## References
1. <a name="ref1"></a>Wikipedia contributors, "Lissajous curve", Wikipedia, The Free Encyclopedia, 17 Aug 2020, 12:46 UTC, <https://en.wikipedia.org/w/index.php?oldid=973478979> [20200923].
2. <a name="ref2"></a>Lee Teschler, "Lissajous patterns: using a scope for display signals", Test & Measurement Tips -- an EE World Online Resources, 11 Aug 2016, url <https://www.testandmeasurementtips.com/using-scope-display-lissajous-patterns/> [20200923].
3. <a name="ref3"></a>-, "Lissajous curve", Desmos, url <https://www.desmos.com/calculator/tti5dasmc4?lang=de> [20200923].
4. <a name="ref3"></a>Eric W. Weisstein, "Lissajous Curve", from MathWorld--A Wolfram Web Resource, url <https://mathworld.wolfram.com/LissajousCurve.html> [20200923].
{% endcomment %}


+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/code/py/2020-11-01-sorting-arrays.md)
