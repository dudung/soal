---
layout: post
author: viridi
title: abm station
mathjax: true
ptext: false
x3dom: false
threejs: false
oo: true
category: physics
tags: ["topics"]
date: 2020-09-26 18:34:00 +07
permalink: /abm/station
---
An object of type station used in an agent-based model (ABM) will be discussed in this article. It still a proposal.


## Station information
A key value array in JavaScript (JS) is proposed to have the following format

```javascript
var StationInfoPTKCI = {
	TNG:  {gmap:"yDn1Bf2Fkwpz9bdc6", la:-6.1768038, lo:106.6152237, name:"Tangerang", },
	JAKK: {gmap:"jdfQ2CRSdt1AMN2p8", la:-6.1375739, lo:106.8124393, name:"Jakarta Kota", },
	BOO:  {gmap:"w1bEwatPYaaN17et5", la:-6.5956098, lo:106.7882263, name:"Bogor", },
	RK:   {gmap:"kpuPGe49DFcBfVzSA", la:-6.3526599, lo:106.2427967, name:"Rangkasbitung", },
};
```

which is, this time, only for PT KCI stations. There are about 74 stations according to [[1](#ref1)], with additionally two unused stations [[2](#ref2)].

The information can be obtained using station `id` as the key, e.g.

```javascript
console.log("" + StationInfoPTKCI["JAKK"]);
```

will produce

```javascript
{gmap: "jdfQ2CRSdt1AMN2p8", la: -6.1375739, lo: 106.8124393, name: "Jakarta Kota"}
```

where `https://goo.gl/maps/` + `gmap` will produce Google Maps short url to the location, `la` and `lo` are the Goole Maps coordinates (latitude and longitude), and `name` is the station name.  

<script src="https://rawcdn.githack.com/butiran/butiran.github.io/e091db33db7d5885481704c0a18be3922fcb24b4/src/js/abm/station.js">
</script>


## Coordinate transformation
A simple and very rough formulation in the form of [[3](#ref3)]

\begin{equation}
\label{eqn:abms-lalo-y}
y = 110.574 \ la
\end{equation}

and

\begin{equation}
\label{eqn:abms-lalo-x}
x = (111.320 \cos \ la) \ lo
\end{equation}

will be used to transform $(la, lo)$ to $(x, y)$ for drawing. Notice that $la$ and $lo$ should be in $\rm rad$ and produced $x$ and $y$ will be in $\rm km$. In the `StationInfoPTKCI` values of $la$ and $lo$ are still in $^\circ$. Use

\begin{equation}
\label{eqn:abms-deg-rad}
\theta = \left( \theta \ {\rm ^\circ} \times \frac{2\pi \ \rm rad}{180 ^\circ} \right) \ {\rm rad}
\end{equation}

for the conversion from $^\circ$ to $\rm rad$.

 
## References
1. <a name="ref1"></a>Kontributor Wikipedia, "KRL Commuter Line", Wikipedia, Ensiklopedia Bebas, 24 September 2020, 15.47 UTC, url <https://id.wikipedia.org/w/index.php?oldid=17435179> [20200926].
2. <a name="ref2"></a>Bramantiyo Marjuki, "Jalur Kereta Api SS/KAI Tanah Abang - Rangkasbitung (1899 - sekarang)", 23 Oct 2017, url <https://javarailmaps.blogspot.com/2017/10/jalur-kereta-api-sskai-tanah-abang.html> [20200926].
3. <a name="ref3"></a>Jim Lewis, "Answer to 'Simple calculations for working with lat/lon and km distance?'", StackOverflow, 10 Aug 2009, url <https://stackoverflow.com/a/1253545> [20200926].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/abm/2020-09-26-abm-station.md)
