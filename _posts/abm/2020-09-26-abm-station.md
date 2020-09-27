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

which is, this time, only for PT Kereta Commuter Indonesia (KCI) stations. There are about 74 stations according to [[1](#ref1)], with additionally two unused stations [[2](#ref2)].

The information can be obtained using station `id` as the key, e.g.

```javascript
console.log("" + StationInfoPTKCI["JAKK"]);
```

will produce

```javascript
{gmap: "jdfQ2CRSdt1AMN2p8", la: -6.1375739, lo: 106.8124393, name: "Jakarta Kota"}
```

where `https://goo.gl/maps/` + `gmap` will produce Google Maps short url to the location, `la` and `lo` are the Goole Maps coordinates (latitude and longitude), and `name` is the station name.  

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

for the conversion from $^\circ$ to $\rm rad$. After testing the results from some pairs of stations and compare it Google Maps, it is already in $^\circ$. Conversion to $rad$ is not necessary.


## Result
Using the stations data from PT KCI (only the name) and positions (from Google Maps and Wikipedia) a map of commuter network can be produced as shown in following Fig. <a href="#fig:ambs-stations-position">1</a>.

<oo>
svg 600 305 #fafafa fig:ambs-stations-position|Position of all stations supervised by PT KCI.
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa

style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 415 209 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 420 219 NMO
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 405 212 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 410 222 GPI
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 385 208 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 390 218 CBN
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 370 206 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 375 216 PDRG
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 352 280 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 357 290 BOO
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 357 244 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 362 254 CLT
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 354 223 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 359 233 BJD
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 358 199 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 363 209 CTA
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 366 175 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 371 185 DP
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 369 167 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 374 177 DPB
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 375 155 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 380 165 POC
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 375 151 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 380 161 UI
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 376 139 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 381 149 UP
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 376 134 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 381 144 LNA
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 379 122 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 384 132 TNT
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 382 109 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 387 119 PSM
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 386 97 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 391 107 PSMB
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 388 93 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 393 103 DRN
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 386 86 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 391 96 CW
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 389 77 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 394 87 TEB
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 385 68 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 390 78 MRI
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 380 62 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 385 72 CKI
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 375 55 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 380 65 GDD
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 374 50 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 379 60 GMR
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 374 44 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 379 54 JUA
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 372 41 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 377 51 SWL
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 372 35 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 377 45 MGB
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 366 30 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 371 40 JAYL
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 365 28 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 370 38 JAKK
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 400 14 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 405 24 TPK
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 379 20 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 384 30 AC
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 373 25 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 378 35 KPB
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 396 71 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 401 81 JNG
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 392 68 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 397 78 POK
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 370 59 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 375 69 KMT
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 386 55 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 391 65 GST
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 383 49 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 388 59 PSE
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 381 42 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 386 52 KMO
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 378 32 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 383 42 RJW
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 359 38 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 364 48 DU
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 352 42 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 357 52 GGL
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 342 41 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 347 51 PSG
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 315 40 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 320 50 TKO
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 323 41 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 328 51 BOI
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 311 42 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 316 52 RW
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 305 44 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 310 54 KDS
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 292 46 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 297 56 PI
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 284 47 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 289 57 BPR
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 273 49 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 278 59 TTI
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 256 50 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 261 60 TNG
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 371 64 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 376 74 SUD
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 367 63 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 372 73 KAT
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 379 66 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 384 76 MPG
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 363 55 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 368 65 THB
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 357 67 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 362 77 PLM
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 349 83 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 354 93 KBY
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 338 93 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 343 103 PDB
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 308 104 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 313 114 PDJ
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 318 111 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 323 121 JRU
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 309 116 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 314 126 SDM
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 288 126 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 293 136 RU
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 283 128 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 288 138 SRP
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 269 131 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 274 141 CSK
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 257 134 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 262 144 CCY
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 230 142 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 235 152 PRP
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 209 148 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 214 158 CKP
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 196 147 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 201 157 CJT
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 187 138 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 192 148 DAR
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 169 132 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 174 142 TEJ
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 155 133 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 160 143 TGS
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 141 137 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 146 147 CKY
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 133 136 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 138 146 MJ
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 98 136 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 103 146 CTR
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 50 146 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 55 156 RK
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 405 70 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 410 80 CPN
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 413 70 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 418 80 KLD
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 425 73 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 430 83 BUA
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 436 72 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 441 82 KLDB
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 443 73 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 448 83 CUK
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 443 73 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 448 83 RWB
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 458 76 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 463 86 KRI
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 469 83 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 474 93 BKS
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 460 88 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 465 98 BKST
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 500 95 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 505 105 TB
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 516 97 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 521 107 CIT
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 521 94 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 526 104 MTM
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 550 93 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 555 103 CKR
style lc:#a00 ls:0 lw:1 lo:1 fc:#faa
circle 358 32 4
style lw:0 fc:#000 fo:1 ts:normal tw:normal tf:Times tz:10px
text 363 42 AK
</oo>

Unfortunately, the density of stations per area is not the same at different places. Perhaps an illustratif network [[1](#ref1)] is preferable.


## JS file
Content of `station.js` is as for

```javascript
```

which can be a subject of modification by the team.


## Note
Converstion from $(la, lo)$ to $(x, y)$ using Eqns. \eqref{eqn:abms-lalo-y} and \eqref{eqn:abms-lalo-x} should be further tested, since the current test (27/9) is only roughly using Google Maps ruler between two points. Some differences about $1-2 \ km$ are still obtained. 


## References
1. <a name="ref1"></a>Kontributor Wikipedia, "KRL Commuter Line", Wikipedia, Ensiklopedia Bebas, 24 September 2020, 15.47 UTC, url <https://id.wikipedia.org/w/index.php?oldid=17435179> [20200926].
2. <a name="ref2"></a>Bramantiyo Marjuki, "Jalur Kereta Api SS/KAI Tanah Abang - Rangkasbitung (1899 - sekarang)", 23 Oct 2017, url <https://javarailmaps.blogspot.com/2017/10/jalur-kereta-api-sskai-tanah-abang.html> [20200926].
3. <a name="ref3"></a>Jim Lewis, "Answer to 'Simple calculations for working with lat/lon and km distance?'", StackOverflow, 10 Aug 2009, url <https://stackoverflow.com/a/1253545> [20200926].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/abm/2020-09-26-abm-station.md)
