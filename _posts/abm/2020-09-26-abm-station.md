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

<script src="https://rawcdn.githack.com/butiran/butiran.github.io/e091db33db7d5885481704c0a18be3922fcb24b4/src/js/abm/station.js">
</script>


## References
1. <a name="ref1"></a>Kontributor Wikipedia, "KRL Commuter Line", Wikipedia, Ensiklopedia Bebas, 24 September 2020, 15.47 UTC, url <https://id.wikipedia.org/w/index.php?oldid=17435179> [20200926].
2. <a name="ref2"></a>Bramantiyo Marjuki, "Jalur Kereta Api SS/KAI Tanah Abang - Rangkasbitung (1899 - sekarang)", 23 Oct 2017, url <https://javarailmaps.blogspot.com/2017/10/jalur-kereta-api-sskai-tanah-abang.html> [20200926].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/abm/2020-09-26-abm-station.md)
