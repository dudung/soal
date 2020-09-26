/*
	StasionInfo.js
	Information about Stations of PT Kereta Commuter Indonesia
	
	Sparisoma Viridi | https://github.com/dudung
	
	Usage: StationInfo[XXX], XXX = station code, e.g. NMO
	
	20200926
	1907 Advance StationInfo from abm-com-seir.js file.
	1949 Complete until JNG, search for Pondok Betung abvr. (x).
	2000 Accomplish CKY, MJ, CTR, RK stations.
	2226 Find information about Cilangkap and Pondok Bitung [1].
	2303 Create Google Maps link for CKP and PDB.
	2306 Note the base url for Google Maps https://goo.gl/maps/.
	2310 Add reference for commuter map [2].
	
	References
	1. Bramantiyo Marjuki, "Jalur Kereta Api SS/KAI Tanah Abang
	   - Rangkasbitung (1899 - sekarang)", 23 Oct 2017, url
		 https://javarailmaps.blogspot.com/2017/10/jalur-kereta-api
		 -sskai-tanah-abang.html [20200926].
	2. Kontributor Wikipedia, "KRL Commuter Line", Wikipedia,
	   Ensiklopedia Bebas, 24 September 2020, 15.47 UTC, url
	   https://id.wikipedia.org/w/index.php?oldid=17435179
	 	 [20200926].
*/

var StationInfo = {
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
};
