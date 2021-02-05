---
layout: post
author: viridi
title: simulation with python
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: false
category: code
tags: ["python", "simulation", "numpy", "scipy", "matplotlib"]
date: 2021-02-06 05:02:00 +07
permalink: /code/py/simulation-with-python
---
Python can be used in simulating population which depends on starting population, infant mortality, food, fertility x & y, healthcare, agriculture, chance of disaster, and  age of death [[1](#ref1)], a simple dynamical system like pendulum [[2](#ref2)], and random walk [[3](#ref3)]. It can visualize the data using animated graphs [[4](#ref4)] and motion of the objects [[5](#ref5)]. It is only a short introduction to do a simulation using Python.


## library
Following libraries are required to perform a simulation double pendulum with visualization [[5](#ref5)]

- numpy
- scipy.integrate
- matplotlib.pyplot
- matplotlib.animation

A short information about above libraries is as follow [[6](#ref6)]. The first library is NumPy that supports for large, multi-dimensional arrays and matrices, accompanied by a large collection of high-level mathematical functions to operate on them, which gives it functionality comparable to MATLAB. The SciPy is library that adds functionality more MATLAB-like. And the last is Matplotlib, a MATLAB-like plotting package that provides functionality for plotting.


## references
1. <a name="ref1"></a>Terence Shin, "Building Simulations in Python — A Step by Step Walkthrough: Learn the fundamentals to be able to simulate the pandemic", Towards Data Science, 29 Nov 2020, url <https://towardsdatascience.com/building-simulations-in-python-a-complete-walkthrough-3965b2d3ede0> [20210205].
2. <a name="ref2"></a>Christian Hubbs, "", Towards Data Science, 22 Feb 2020, url <https://towardsdatascience.com/a-beginners-guide-to-simulating-dynamical-systems-with-python-a29bc27ad9b1> [20210205].
3. <a name="ref3"></a>Vladimir Ilievski, "", Towards Data Science, 21 Apr 2020, url <https://towardsdatascience.com/animated-visualization-of-random-walks-in-python-dc18f01ef15e> [20210205].
4. <a name="ref4"></a>Costas Andreou, "", Towards Data Science, 5 May 2020, url <https://towardsdatascience.com/learn-how-to-create-animated-graphs-in-python-fce780421afe> [20210205].
5. <a name="ref5"></a>John Hunter, Darren Dale, Eric Firing, Michael Droettboom and the Matplotlib development team, "The double pendulum problem", Matplotlib Version 2.1.2, Feb 2018, url <https://matplotlib.org/gallery/animation/double_pendulum_animated_sgskip.html> [20210205].
6. <a name="ref6"></a>Wikipedia contributors, "NumPy", Wikipedia, The Free Encyclopedia, 25 Jan 2021, 06:18 UTC, <https://en.wikipedia.org/w/index.php?oldid=1002606585> [20210206].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/code/py/2021-02-05-simulation-with-python.md)
