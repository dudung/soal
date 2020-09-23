---
layout: post
author: viridi
title: lissajour pattern generator
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: python
date: 2020-09-23 06:29:00 +07
tags: ["topics"]
permalink: /code/py/lissajous-pattern-generator
---
A simple program writen in Python to produce Lissajous curve [[1](#ref1)] is presented here.


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




## References
1. <a name="ref1"></a>Wikipedia contributors, "Lissajous curve", Wikipedia, The Free Encyclopedia, 17 Aug 2020, 12:46 UTC, <https://en.wikipedia.org/w/index.php?oldid=973478979> [20200923].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/code/py/2020-09-23-lissajous-pattern-generator.md)

{% comment %}
An example of Python 3 code is discussed in here. It is named in lower case [[1](#ref1)] and uses suggested comment style [[2](#ref2)]. The program is called from command line [[3](#ref3)] and is able to process the arguments [[4](#ref4)] providing a filename to be opened [[5](#ref5)] showing its content without addition newline [[6](#ref6)].


## Parameters file
A plain text file containing parameters, named `params.txt` in this case, has following content.

```javascript
TITL 2d-Lissajous-pattern-generator

AMPX 1
TPEX 1
PHAX 0

AMPY 1
TPEY 1
PHAY 1.57

TBEG 0
TEND 2
TSTP 0.1
```

The file will be read and its content will be displayed. First the program has to know what is the filename.


## Python file
A Python file named `rdpf.py` is made and has content as follow.

```python
# 
# rdpf.py
# Read parameters file and show its content
# 
# Sparisoma Viridi | https://github.com/dudung
# 
# Execute: python3 rdpf.py params.txt
# 
# 20200922
# 1637 Start this example.
# 1723 Collect references [1-4].
# 1735 Test simple args and add [5].
# 1751 Get newline problem in printing output.
# 1828 Solve it using Python 3 [6].
# 1916 Finalize comments.
# 
# References
# 1. agold, "Asnwer to 'Python file naming convention?'", 
#    Software Engineering, 6 Jun 2019, url https:// 
#    softwareengineering.stackexchange.com/a/308976 [20200922].
# 2. Dan Bader, "Python Multi-line Comments: Your Two Best
#    Options", url https://dbader.org/blog/python-multiline
#    -comment [20200922].
# 3. -,"1. Command line and environment", Python, 22 Sep 2020, 
#    url https://docs.python.org/3/using/cmdline.html
#    [20200922].
# 4. Sayak Paul, "Argument Parsing in Python", DataCamp, 16 May
#    2019, url https://www.datacamp.com/community/tutorials
#    /argument-parsing-in-python [20200922].
# 5. -, "Open a File on the Server", W3Schools, url https://www
#    .w3schools.com/python/python_file_open.asp [20200922].
# 6. codelogic, "Answer to 'How to print without newline or
#    space?'", StackOverflow, 29 Jan 2009, url https://
#    stackoverflow.com/a/493399 [20200922].
# 

# Import necessary modules
import sys

# Get command line arguments
argv = sys.argv

# Get parameters filename
fn = argv[1]

# Open parameters file
fp = open(fn, "r")

# Show parameters line by line
for line in fp:
	print(line, end="")

# Close file
fp.close()
```

The last 18 lines is the implementation part of the program, while the preceeded lines are for comments and documentation. You can copy, adapt, and modify it.


## Output
The `rdpf.py` is executed from command line

```batch
$ python3 rdpf.py params.txt
```

and will produce

```javascript
TITL 2d-Lissajous-pattern-generator

AMPX 1
TPEX 1
PHAX 0

AMPY 1
TPEY 1
PHAY 1.57

TBEG 0
TEND 2
TSTP 0.1
```

as expected.


## Exercises
1. Modify `params.txt` and see the output result.
2. Type following code and show the result.
```python
import sys
argv = sys.argv
fn = argv[1]
fp = open(fn, "r")
params = []
for line in fp:
	line2 = line.rstrip("\n")
	params.append(line2)
fp.close()
for p in params:
	b = p.split();
	if b:
		print("Name = ", b[0])
		print("Value = ", b[1])
```
3. Explain the last 6 lines from previous code. Modify it in order to produce
```batch
TITL = 2d-Lissajous pattern generator
AMPX = 1
TPEX = 1
..
TSTP = 0.1
```
4. Following equations is necessary for creating 2-d Lissajous pattern.
\begin{equation}
\label{eqn:pyrdpf-x}
x(t) = A_x \sin \left( \frac{2\pi}{T_x} t + \phi_x \right)
\end{equation}
and
\begin{equation}
\label{eqn:pyrdpf-y}
y(t) = A_y \sin \left( \frac{2\pi}{T_y} t + \phi_y \right).
\end{equation}
Map the relation beween parameters in Eqns. \eqref{eqn:pyrdpf-x} and \eqref{eqn:pyrdpf-y}, e.g. $A_x$, $\dots$, $\phi_y$, to parameters in `params.txt` file., e.g. `AMPX`, $\dots$, `PHAY`.
5. Design your own parameters file and explain the use of each line in that file.


## References
1. <a name="ref1"></a>agold, "Asnwer to 'Python file naming convention?'", Software Engineering, 6 Jun 2019, url <https://softwareengineering.stackexchange.com/a/308976> [20200922].
2. <a name="ref2"></a>Dan Bader, "Python Multi-line Comments: Your Two Best Options", url <https://dbader.org/blog/python-multiline-comment> [20200922].
3. <a name="ref3"></a>-,"1. Command line and environment", Python, 22 Sep 2020, url <https://docs.python.org/3/using/cmdline.html> [20200922].
4. <a name="ref4"></a>Sayak Paul, "Argument Parsing in Python", DataCamp, 16 May 2019, url <https://www.datacamp.com/community/tutorials/argument-parsing-in-python> [20200922].
5. <a name="ref5"></a>-, "Open a File on the Server", W3Schools, url <https://www.w3schools.com/python/python_file_open.asp> [20200922].
6. <a name="ref6"></a>codelogic, "Answer to 'How to print without newline or space?'", StackOverflow, 29 Jan 2009, url <https://stackoverflow.com/a/493399> [20200922].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/code/py/2020-09-22-read-params-file.md)

{% endcomment %}
 