---
layout: soal
author: viridi
title: "0269"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["machine learning", "classification", "tensorflow", "fi3201", "2020-2"]
date: 2021-04-21 11:58:00 +07
permalink: /0260
src: https://github.com/dudung/soal/commits/master/_posts/0/26/2021-04-20-machine-learning-9.md
ref: https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.88208&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false


ID | Inisial | Final | Layer tersembunyi (neuron)
A1 | ![]({{site.baseurl}}/assets/img/0/26/0269a.png) | ![]({{site.baseurl}}/assets/img/0/26/0269a.png) | 2 (4, 2)
A2 | ![]({{site.baseurl}}/assets/img/0/26/0269c.png) | ![]({{site.baseurl}}/assets/img/0/26/0269d.png) | 3 (3, 2, 2)


Sumbu mendatar menggambarkan nilai $x_1$ dan sumbu tegak $x_2$. Untuk menyelesaikan kasus ini cukup dibutuhkan satu layar tersebunyi yang terdiri dari $N_{\rm hidden}$ buah neuron tersembunyi. Jumlah epoch (siklus belajar menggunakan seluruh training set) yang diperlukan untuk mencapai suatu nilai training loss $\varepsilon_{\rm loss}$ tertentu akan bergantung pada nilai $N_{\rm hidden}$. Semakin kecil nilai $\varepsilon_{\rm loss}$, hasil yang diperoleh semakin baik. Dalam kasus ini pengelompokan kedua jenis data semakin baik. Nilai $\varepsilon_{\rm loss}$, $N_{\rm hidden}$, dan epoch yang terkait adalah

A | $< 0.010$, $5$, dan $< 19$. 
B | $> 0.015$, $4$, dan $> 25$.
C | $< 0.005$, $3$, dan $< 30$.
D | $< 0.020$, $2$, dan $< 10$.
E | $< 0.040$, $1$, dan $> 24$.
