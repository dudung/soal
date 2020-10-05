---
layout: post
author: viridi
title: oo scatter plot
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: 
tags: ["js"]
date: 2020-09-28 18:12:00 +07
permalink: /code/js/oo-scatter-plot
---
A conversion from JavaScript (JS) array to scatter plot [[1](#ref1)], which is displayed using `oo` [[2](#ref2)] is presented in this article.


## oo tag
A scatter plot of $y$ againts $x$ with data (0, 2), (0.5, 2.5), (1, 3), (1.5, 3.125), (2, 3), (2.5, 2.5), and (3, 2) can be illustrate as follow.

<oo>
svg 200 200 #fafafa fig:osp-yx|Scatter of $y$ againts $x$.

style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 20 20 180 180 40 40
style lc:#000 ls:0 lw:1 lo:1 fc:#000
arrow 20 180 180 180
arrow 20 180 20 20
style lc:#000 ls:0 lw:1 lo:1 fc:#000
circle 20 180 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 186 183 x
text 18 12 y

style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 15 197 0
text 55 197 1
text 95 197 2
text 135 197 3
text 5 185 0
text 5 145 1
text 5 105 2
text 5 65 3

style lc:#f00 ls:0 lw:1.5 lo:1 fc:#fff
circle 20 100 3
circle 40 80 3
circle 60 60 3
circle 80 55 3
circle 100 60 3
circle 120 80 3
circle 140 100 3
</oo>

Following code are required to display Fig. <a href="#fig:osp-yx">1</a> using `oo`

```css
<oo>
svg 200 200 #fafafa fig:osp-yx|Scatter of $y$ againts $x$.

style lc:#000 ls:6-2 lw:0.3 lo:0.8
grid 20 20 180 180 40 40
style lc:#000 ls:0 lw:1 lo:1 fc:#000
arrow 20 180 180 180
arrow 20 180 20 20
style lc:#000 ls:0 lw:1 lo:1 fc:#000
circle 20 180 2
style lw:0 fc:#000 fo:1 ts:italic tw:normal tf:Times tz:16px
text 186 183 x
text 18 12 y

style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:16px
text 15 197 0
text 55 197 1
text 95 197 2
text 135 197 3
text 5 185 0
text 5 145 1
text 5 105 2
text 5 65 3

style lc:#f00 ls:0 lw:1.5 lo:1 fc:#fff
circle 20 100 3
circle 40 80 3
circle 60 60 3
circle 80 55 3
circle 100 60 3
circle 120 80 3
circle 140 100 3
</oo>
```

where the point must be determined manually by viewing it repeatedly, which is not so efficient.


## JS function
A function using JS can be constructed to automatize the process. First make an array of the data

```batch
data = `
0, 2
0.5, 2.5
1, 3
1.5, 3.125
2, 3
2.5, 2.5
3, 2
`;
```

<script>
var data = `
0, 2
0.5, 2.5
1, 3
1.5, 3.125
2, 3
2.5, 2.5
3, 2
`;




console.log(data);
</script>


## References
1. <a name="ref1"></a>Wikipedia contributors, "Scatter plot", Wikipedia, The Free Encyclopedia, 10 Sep 2020, 22:11 UTC, <https://en.wikipedia.org/w/index.php?oldid=977773986> [20201005].
2. <a name="ref2"></a>Diagram parser `oo` is developed by Sparisoma Viridi and Fiki Taufik Akbar Sobar, url <https://github.com/dudung/oo> [20201005].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/code/js/oo/2020-10-05-oo-scatter-plot.md)
