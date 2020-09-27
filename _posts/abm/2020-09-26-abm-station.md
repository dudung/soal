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

for the conversion from $^\circ$ to $\rm rad$. After testing the results from some pairs of stations and compare it with Google Maps, it is already in $^\circ$. Conversion to $rad$ is not necessary.


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
Content of `station.js` is as follow

```javascript
/*
	station.js
	Information about train stations
	
	Sparisoma Viridi | https://github.com/dudung
	
	20200926
	1907 Advance StationInfo from abm-com-seir.js file.
	1949 Complete until JNG, search for Pondok Betung abvr. (x).
	2000 Accomplish CKY, MJ, CTR, RK stations.
	2226 Find information about Cilangkap and Pondok Bitung [1].
	2303 Create Google Maps link for CKP and PDB.
	2306 Note the base url for Google Maps https://goo.gl/maps/.
	2310 Add reference for commuter map [2].
	2319 Add reference for simple conversion (la,lo)->(x,y) [3].
	20200927
	0508 Rename the key value array to StationInfoPTKCI.
	0631 Create transformToXY function.
	0641 Calculate avarage of la and lo for all stations.
	0814 Miss stations to Cikarang, add stations id.
	0910 Assume [3] already in deg as checked with Google Maps.
	0946 Finish all 87 stations and draw all in canvas.
	1005 Add AK and ask team to make illustration as in [2].
	1236 Make SVG text for viewing stations with oo.
	1302 Close this version and update related article.
	
	References
	1. Bramantiyo Marjuki, "Jalur Kereta Api SS/KAI Tanah Abang
	   - Rangkasbitung (1899 - sekarang)", 23 Oct 2017, url
		 https://javarailmaps.blogspot.com/2017/10/jalur-kereta-api
		 -sskai-tanah-abang.html [20200926].
	2. Kontributor Wikipedia, "KRL Commuter Line", Wikipedia,
	   Ensiklopedia Bebas, 24 September 2020, 15.47 UTC, url
	   https://id.wikipedia.org/w/index.php?oldid=17435179
	 	 [20200926].
	3. Jim Lewis, "Answer to 'Simple calculations for working
	   with lat/lon and km distance?'", StackOverflow, 10 Aug
		 2009, url https://stackoverflow.com/a/1253545 [20200926]. 
*/


// Stations of PT Kereta Commuter Indonesia
var StationInfoPTKCI = {
	NMO:  {gmap:"9cF3yJYsegh5WwTn7", la:-6.4662291, lo:106.9040266, name:"Nambo", },
	GPI:  {gmap:"HrVo9GoqmtdKxemr9", la:-6.4718045, lo:106.8863609, name:"Gunung Putri", },
	CBN:  {gmap:"KWGWQmEbWJNW2Ae37", la:-6.4642644, lo:106.8502809, name:"Cibinong", },
	PDRG: {gmap:"P6rx1Cd8uSiEBcCb6", la:-6.4606999, lo:106.8223982, name:"Pondok Rajeg", },
	BOO:  {gmap:"w1bEwatPYaaN17et5", la:-6.5956098, lo:106.7882263, name:"Bogor", },
	CLT:  {gmap:"vHe3j22FCUkPrzYL7", la:-6.5305389, lo:106.7983720, name:"Cilebut", },
	BJD:  {gmap:"zA2zQNr6G4jX17Tu8", la:-6.4932483, lo:106.7927070, name:"Bojonggede", },
	CTA:  {gmap:"C4H9wZSGKVXh1jDKA", la:-6.4487951, lo:106.8003074, name:"Cityam", },
	DP:   {gmap:"gfrjQ4L6TPq5CdLw5", la:-6.4050057, lo:106.8150619, name:"Depok", },
	DPB:  {gmap:"7xj3ZnpMXWNjFqnx5", la:-6.3911285, lo:106.8195145, name:"Depok Baru", },
	POC:  {gmap:"LVV1fvW3QBzStuzX6", la:-6.3690785, lo:106.8300194, name:"Pondok Cina", },
	UI:   {gmap:"CBBtvMPsG9NTMJPD7", la:-6.3607541, lo:106.8295594, name:"Universitas Indonesia", },
	UP:   {gmap:"n3JSiSen85yob3Vi8", la:-6.3389397, lo:106.8322411, name:"Universitas Pancasila", },
	LNA:  {gmap:"57boEP5EXmqn3aRv7", la:-6.3306601, lo:106.8327927, name:"Lenteng Agung", },
	TNT:  {gmap:"B53E6wY42X3WxZnu8", la:-6.3075900, lo:106.8364913, name:"Tanjung Barat", },
	PSM:  {gmap:"5ShUGaya1TSjM1tHA", la:-6.2842455, lo:106.8423577, name:"Pasar Minggu", },
	PSMB: {gmap:"WoFavFzSXqnanvzH7", la:-6.2627837, lo:106.8496685, name:"Pasar Minggu Baru", },
	DRN:  {gmap:"NLaKRH3dRZpRztxB9", la:-6.2553411, lo:106.8528508, name:"Duren Kalibata", },
	CW:   {gmap:"GFsU4qWfdgEGsYiDA", la:-6.2427599, lo:106.8497567, name:"Cawang", },
	TEB:  {gmap:"Qi3PCyqRbzqk3ZBH7", la:-6.2255900, lo:106.8558813, name:"Tebet", },
	MRI:  {gmap:"NVgeKAcwzh3RwW7C7", la:-6.2098913, lo:106.8480260, name:"Manggarai", },
	CKI:  {gmap:"NemacqYZCSdn1JLZA", la:-6.1985563, lo:106.8390746, name:"Cikini", },
	GDD:  {gmap:"Ekd8fcB891AEZv6g9", la:-6.1860836, lo:106.8303993, name:"Gondangdia", },
	GMR:  {gmap:"N9VtKAy1yYacDnCt7", la:-6.1767112, lo:106.8284640, name:"Gambir", },
	JUA:  {gmap:"jLhdMKPAwqrba3K96", la:-6.1667216, lo:106.8282843, name:"Juanda", },
	SWL:  {gmap:"PbWuzKKRj858Czkr8", la:-6.1606407, lo:106.8254472, name:"Sawah Besar", },
	MGB:  {gmap:"tdTMqTbUh1PbKrNB8", la:-6.1496813, lo:106.8248376, name:"Mangga Besar", },
	JAYL: {gmap:"9GASV9arbiApx5Wk7", la:-6.1412853, lo:106.8143993, name:"Jayakarta", },
	JAKK: {gmap:"jdfQ2CRSdt1AMN2p8", la:-6.1375739, lo:106.8124393, name:"Jakarta Kota", },
	TPK:  {gmap:"ukrDFNA474KvtMNAA", la:-6.1120380, lo:106.8760139, name:"Tanjung Priok", },
	AC:   {gmap:"edYKjSTnMVUqjXfd7", la:-6.1215668, lo:106.8382612, name:"Ancol", },
	KPB:  {gmap:"Qno5GFA2tw1nM88L9", la:-6.1322199, lo:106.8265271, name:"Kampung Bandan", },
	JNG:  {gmap:"PNJ7GPh4xPwSMN19A", la:-6.2152144, lo:106.8680843, name:"Jatinegara", },
	POK:  {gmap:"h55E65hXhtCyxTKfA", la:-6.2091590, lo:106.8600711, name:"Pondok Jati", },
	KMT:  {gmap:"zH7rKyT1c3aZ8bh59", la:-6.1938028, lo:106.8215123, name:"Kramat", },
	GST:  {gmap:"AYKg6CrDnqefxHmBA", la:-6.1860203, lo:106.8506583, name:"Gang Sentiong", },
	PSE:  {gmap:"7omGiWtnJ7NXDtLe7", la:-6.1747891, lo:106.8442321, name:"Pasar Senen", },
	KMO:  {gmap:"WQuwSDtYuKttQidp8", la:-6.1618700, lo:106.8415700, name:"Kemayoran", },
	RJW:  {gmap:"of6GskMbDJciaJFn7", la:-6.1450470, lo:106.8367089, name:"Rajawali", },
	DU:   {gmap:"wXrGfEQeNjUHpBuQ7", la:-6.1552740, lo:106.8012554, name:"Duri", },
	GGL:  {gmap:"uGYD8B3f7Vu6HZ5C7", la:-6.1620267, lo:106.7893716, name:"Grogol", },
	PSG:  {gmap:"1MYo3mPrJsZ4XseFA", la:-6.1612657, lo:106.7714667, name:"Pesing", },
	TKO:  {gmap:"wx1LS5yr4nspTNcP9", la:-6.1585400, lo:106.7213411, name:"Taman Kota", },
	BOI:  {gmap:"7Y3CzQ33gfiHASdG6", la:-6.1601350, lo:106.7362047, name:"Bojong Indah", },
	RW:   {gmap:"xh7MBDR74nPikM8S9", la:-6.1627496, lo:106.7148621, name:"Rawa Buaya", },
	KDS:  {gmap:"VF6XhTtFyF8qqUJd9", la:-6.1660731, lo:106.7038006, name:"Kalideres", },
	PI:   {gmap:"3BjmujNuq8fqd19c9", la:-6.1699387, lo:106.6800057, name:"Poris", },
	BPR:  {gmap:"zjDgBHZf2R77CNBm8", la:-6.1717870, lo:106.6653337, name:"Batuceper", },
	TTI:  {gmap:"bizHhndZb8i7JVZ27", la:-6.1754527, lo:106.6454906, name:"Tanah Tinggi", },
	TNG:  {gmap:"yDn1Bf2Fkwpz9bdc6", la:-6.1768038, lo:106.6152237, name:"Tangerang", },
	SUD:  {gmap:"kmw913gjDvR1Mzxa6", la:-6.2024167, lo:106.8234654, name:"Sudirman", },
	KAT:  {gmap:"v6PyPL8Ss6Lnty2k7", la:-6.2008350, lo:106.8158467, name:"Karet", },
	MPG:  {gmap:"CN3LdNZQmHBFZqtF7", la:-6.2060495, lo:106.8378906, name:"Mampang", },
	THB:  {gmap:"B78J523EpkKseCjn6", la:-6.1856968, lo:106.8086649, name:"Tanahabang", },
	PLM:  {gmap:"7mt6GDcvqQyzrLzB6", la:-6.2074111, lo:106.7974382, name:"Palmerah", },
	KBY:  {gmap:"TKUzBSSoUPDLYC4K6", la:-6.2372475, lo:106.7825225, name:"Kebayoran", },
	PDB:  {gmap:"wXpgWDdQsdMBTjMQA", la:-6.2563450, lo:106.7635690, name:"Pondok Betung", },
	PDJ:  {gmap:"PKeWP1ymJMDXbX1E8", la:-6.2763674, lo:106.7099001, name:"Pondok Ranji", },
	JRU:  {gmap:"csg7dNTLXoXnYhUc6", la:-6.2887778, lo:106.7269200, name:"Jurumangu", },
	SDM:  {gmap:"w2mJ5GMUjaUxF6ry5", la:-6.2974329, lo:106.7103651, name:"Sudimara", },
	RU:   {gmap:"Q5eQ24p2r1h3N4YN6", la:-6.3150197, lo:106.6740118, name:"Rawabuntu", },
	SRP:  {gmap:"NE6JY1Y1DVsRWLhv7", la:-6.3200539, lo:106.6634312, name:"Serpong", },
	CSK:  {gmap:"hsXtcnuLpdTHhsVK8", la:-6.3252912, lo:106.6381084, name:"Cisauk", },
	CCY:  {gmap:"ZsNYJjW5S7p66ntAA", la:-6.3295787, lo:106.6167364, name:"Cicayur", },
	PRP:  {gmap:"bBNqqw79GkngkVjs9", la:-6.3442188, lo:106.5677077, name:"Parungpanjang", },
	CKP:  {gmap:"oQQSBSrWtoKpFyEt8", la:-6.3564370, lo:106.5297690, name:"Cilangkap", },
	CJT:  {gmap:"4VEKCpPSrP1Dd9Mm7", la:-6.3543538, lo:106.5073881, name:"Cilejit", },
	DAR:  {gmap:"tPu6yKrbkJWJZxUk9", la:-6.3380127, lo:106.4902432, name:"Daru", },
	TEJ:  {gmap:"wrjbYDWQCR4sEkkC8", la:-6.3272565, lo:106.4591702, name:"Tenjo", },
	TGS:  {gmap:"AirdtDdGjVmB98mN6", la:-6.3284349, lo:106.4324708, name:"Tigaraksa", },
	CKY:  {gmap:"Z2kix8S4pKdCLfZF9", la:-6.3348065, lo:106.4080310, name:"Cikoya", },
	MJ:   {gmap:"RmUBCq9hpxHq66mq6", la:-6.3338860, lo:106.3941802, name:"Maja", },
	CTR:  {gmap:"Tgy2s9A6QwqZmdHT8", la:-6.3338452, lo:106.3302688, name:"Citeras", },
	RK:   {gmap:"kpuPGe49DFcBfVzSA", la:-6.3526599, lo:106.2427967, name:"Rangkasbitung", },
	CPN:  {gmap:"kbz7JyBW9zLNuxVJ7", la:-6.2143352, lo:106.8844360, name:"Cipinang", },
	KLD:  {gmap:"FDyterC5JWrXi4mm8", la:-6.2135200, lo:106.8986500, name:"Klender", },
	BUA:  {gmap:"uEXuQueR9jKLW7xW9", la:-6.2182466, lo:106.9203397, name:"Buaran", },
	KLDB: {gmap:"V2SKe5hLcC8oYSEE6", la:-6.2176471, lo:106.9401219, name:"Klender Baru", },
	CUK:  {gmap:"SeAQp2PzMFQggbXk7", la:-6.2191346, lo:106.9523570, name:"Cakung", },
	RWB:  {gmap:"1viKG1Yd2TS9tE5C6", la:-6.2190921, lo:106.9525856, name:"Rawabebek", },
	KRI:  {gmap:"ivoRyMiodGNjtS4E7", la:-6.2245125, lo:106.9798459, name:"Kranji", },
	BKS:  {gmap:"LsBokmQ8w4RQbChe6", la:-6.2366208, lo:106.9992014, name:"Bekasi", },
	BKST: {gmap:"jdS3bEHpkDnUAQUbA", la:-6.2468343, lo:106.9830389, name:"Bekasi Timur", },
	TB:   {gmap:"UXiWYqqoCF4Pnk8U8", la:-6.2587119, lo:107.0558270, name:"Tambung", },
	CIT:  {gmap:"ZZjJ4cYhSRALFHJQ6", la:-6.2618862, lo:107.0836313, name:"Cibitung", },
	MTM:  {gmap:"K2gpStVhScdAfPndA", la:-6.2571524, lo:107.0936672, name:"Metland Telaga Murni", },
	CKR:  {gmap:"iRXetk3PS2ncVuAn6", la:-6.2553738, lo:107.1450583, name:"Cikarang", },
	AK:   {gmap:"9xj48bECuUqyRTNL9", la:-6.1446789, lo:106.7986757, name:"Angke", },
};



// Transform to (x, y) from (la, lo)
function transformToXY() {
	var la = arguments[0];
	var lo = arguments[1];
	
	// Already in degree while checked with Google Maps
	var x = 111.320 * Math.cos(la) * lo;
	var y = 110.574 * la;
	
	return {x: x, y: y};
}


// Calculate average of la and lo as center
function getCenter() {
	var lac = 0;
	var loc = 0;
	var N = 0;
	for(var k in StationInfoPTKCI) {
		lac += StationInfoPTKCI[k].la;
		loc += StationInfoPTKCI[k].lo;
		N++;
	}
	lac /= N;
	loc /= N;
	return {la: lac, lo: loc};
}


// Class of Station
class Station {
	constructor() {
		if(arguments.length < 1) {
			console.error("Station must provide stationID");
		} else {
			if(arguments[0] in StationInfoPTKCI) {
				this.id = arguments[0];
				var s = StationInfoPTKCI[this.id];
				this.name = s.name;
				var la = s.la;
				var lo = s.lo;
				var c = getCenter();
				var r = transformToXY(la - c.la, lo - c.lo);
				this.position = {x: r.x, y: r.y};
			} else {
				console.error(this.id + " station does not exist");
			}
		}
	}
}


// Create array for all stations
var stations = [];
for(id in StationInfoPTKCI) {
	var s = new Station(id);
	stations.push(s);
}


// Calculate range of positition
function getXYRange() {
	var s = arguments[0];
	var N = s.length;
	
	var xmin = s[0].position.x;
	var xmax = s[0].position.x;
	var ymin = s[0].position.y;
	var ymax = s[0].position.y;
	
	for(var i = 1; i < N; i++) {
		var x = s[i].position.x;
		if(x < xmin) xmin = x;
		if(x > xmax) xmax = x;

		var y = s[i].position.y;
		if(y < ymin) ymin = y;
		if(y > xmax) ymax = y;
	}
	
	var xrange = xmax - xmin;
	var yrange = ymax - ymin;
	
	var padx = 0.1 * xrange;
	var pady = 0.1 * yrange;
	
	xmax += padx;
	xmin -= padx;
	
	ymax += pady;
	ymin -= pady;
	
	return {xmin: xmin, ymin: ymin, xmax: xmax, ymax: ymax};
}


// Set global coordinates
var coord = getXYRange(stations);
coord.dx = coord.xmax - coord.xmin;
coord.dy = coord.ymax - coord.ymin;
var zoom = 5;
var XMIN = 0;
var XMAX = XMIN + zoom * Math.round(coord.dx);
var YMAX = 0;
var YMIN = YMAX + zoom * Math.round(coord.dy);


// Create canvas
var can = document.createElement("canvas");
can.width = XMAX - XMIN;
can.height = YMIN - YMAX;
can.style.width = can.width + "px";
can.style.height = can.height + "px";
can.style.background = "#fcfcfc";
document.body.append(can);


function transformX() {
	var x = arguments[0];
	var X = (x - coord.xmin) / coord.dx * (XMAX - XMIN) + XMIN;
	return X;
}

function transformY() {
	var y = arguments[0];
	var Y = (y - coord.ymin) / coord.dy * (YMAX - YMIN) + YMIN;
	return Y;
}


// Draw all stations
function drawStation() {
	var s = arguments[0];
	var c = arguments[1];
	var N = s.length;
	
	var cx = can.getContext("2d");
	
	for(var i = 0; i < N; i++) {
		var x = s[i].position.x;
		var y = s[i].position.y;
		
		var X = transformX(x);
		var Y = transformY(y);
		var R = 4;
		
		cx.beginPath();
		cx.arc(X, Y, R, 0, 2 * Math.PI);
		cx.fillStyle = "#faa";
		cx.fill();
		cx.lineWidth = 1;
		cx.strokeStyle = "#a00";
		cx.stroke();
		
		cx.fillStyle = "#000";
		cx.fillText(s[i].id, X + 5, Y + 10);
	}
}


// Perform drawing all stations
drawStation(stations, can);


// Generate SVG for oo in butiran
function generateStationSVGText() {
	var s = arguments[0];
	var N = s.length;
	var ooT = "";
	
	for(var i = 0; i < N; i++) {
		var x = s[i].position.x;
		var y = s[i].position.y;
		
		var X = Math.round(transformX(x));
		var Y = Math.round(transformY(y));
		var R = 4;
		
		ooT += "style lc:#a00 ls:0 lw:1 lo:1 fc:#faa" + "\n";
		ooT += "circle " + X + " " + Y + " " + R + "\n";
		
		ooT += "style lw:0 fc:#000 fo:1 ts:normal tw:normal ";
		ooT += "tf:Times tz:10px" + "\n";
		X += 5;
		Y += 10;
		ooT += "text " + X + " " + Y + " " + s[i].id + "\n";
	}
	
	return ooT;
}

var ooText = generateStationSVGText(stations, XMAX - XMIN, YMIN - YMAX);
console.log(ooText);
```

which can be a subject of modification by the team.


## Note
Converstion from $(la, lo)$ to $(x, y)$ using Eqns. \eqref{eqn:abms-lalo-y} and \eqref{eqn:abms-lalo-x} should be further tested, since the current test (27/9) is only roughly using Google Maps ruler between two points. Some differences about $1-3 \ km$ are still obtained. 


## References
1. <a name="ref1"></a>Kontributor Wikipedia, "KRL Commuter Line", Wikipedia, Ensiklopedia Bebas, 24 September 2020, 15.47 UTC, url <https://id.wikipedia.org/w/index.php?oldid=17435179> [20200926].
2. <a name="ref2"></a>Bramantiyo Marjuki, "Jalur Kereta Api SS/KAI Tanah Abang - Rangkasbitung (1899 - sekarang)", 23 Oct 2017, url <https://javarailmaps.blogspot.com/2017/10/jalur-kereta-api-sskai-tanah-abang.html> [20200926].
3. <a name="ref3"></a>Jim Lewis, "Answer to 'Simple calculations for working with lat/lon and km distance?'", StackOverflow, 10 Aug 2009, url <https://stackoverflow.com/a/1253545> [20200926].

+ [Article history](https://github.com/butiran/butiran.github.io/commits/master/_posts/abm/2020-09-26-abm-station.md)
