/*
	nucleon.js
	Agent of nucleon for liquid drop model with ABM
	
	url https://butiran.github.io/
	
	Sparisoma Viridi | GS _HjSaE0AAAAJ
	
	20201207
	1633 Start designing class of Nucleon.
	1722 Finish class of Nucleon, only simple structure.
*/

class Nucleon {
	constructor() {
		if(arguments.length == 0) {
			this.neutron = true;
			console.warn("Nucleon is set to neutron");
			this.type = "neutron";
		} else {
			if(arguments[0] == "proton") {
				this.proton = true;
				this.type = "proton";
			} else if(arguments[0] == "neutron") {
				this.neutron = true;
				this.type = "proton";
			}
		}
	}	
}
