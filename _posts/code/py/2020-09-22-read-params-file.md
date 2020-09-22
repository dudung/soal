---
layout: post
author: viridi
title: read params file
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: python
date: 2020-09-22 19:17:00 +07
tags: ["topics"]
permalink: /code/py/read-params-file
---
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

