---
layout: soal
author: viridi
title: "0175"
mathjax: true
chartjs: false
ptext: false
x3dom: false
threejs: false
3dmol: false
oo: false
svgphys: false
category: physics
tags: ["genetic algorithm", "terminology", "decoding", "nonsolution", "fi3201", "2020-2"]
date: 2021-04-07 11:03:00 +07
permalink: /0175
src: https://github.com/dudung/soal/commits/master/_posts/0/17/2021-04-07-ga-terminology-5.md
ref: https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_fundamentals.htm
---
Saat mencari solusi dalam ruang genotip pada algoritma genetik, perlu diseleksi kromosom yang lebih baik dibandingkan dengan sejumlah yang telah ada sebelumnya pada populasi, termasuk di dalamnya kedua induk penghasil kromosom tersebut.

Untuk menilai kecocokan kromosom atau solusi dalam ruang genotip dengan hasil yang diharapkan perlu dibuat suatu fungsi yang disebut fitness function. Secara sederhana fungsi ini akan memberi nilai pada suatu kromosom dan selanjutnya adalah membiarkan kromosom unggul (dengan nilai tertinggi) untuk berada dalam populasi sementara kromosom kurang dan tidak unggul akan dikeluarkan dari ruang populasi.

Selain itu fitness function juga dapat digunakan untuk memberikan nilai amat rendah untuk kromosom atau solusi dalam ruang genotip dan tidak memiliki arti dalam ruang fenotip atau tidak ada representasinya dalam keadaan sebenarnya.

![]({{site.baseurl}}/assets/img/0/17/0175.png)

Gambar di atas merupakan ilustrasi pelapisan, misalnya saja kue, dengan bahan A, B, dan C. Dengan masing-masing bahan memiliki ketebalan tertentu. Tebal kue dibatasi harus tepat tujuh satuan.

Sel R1C5 bukan merupakan solusi yang diharapkan di ruang fenotip sehingga representasinya dalam ruang genotip seharusnya dapat dieliminasi dengan memberinya nilai rendah melalui fitness function.

Permasalahan pada solusi yang diberikan oleh sel R1C5 adalah

<ol type="A">
<li>Tidak terdapat bahan jenis A ($\color{red} \blacksquare$).
<li>Ketebalan lapisan terakhir kurang satu satuan. 
<li>Harus selalu terdapat bahan jenis A ($\color{red} \blacksquare$), B ($\color{green} \blacksquare$), dan C ($\color{blue} \blacksquare$).
<li>Jenis bahan memiliki urutan yang salah.
<li>Bahan jenis A ($\color{red} \blacksquare$) harusnya dua lapis akan tetapi tidak berurutan.
