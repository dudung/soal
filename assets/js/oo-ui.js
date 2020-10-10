/*
	oo-ui.js
	User Interface for oo in designing some SVG objects
	
	Sparisoma Viridi | https://github.com/dudung
	
	20201010
	1827 Start this file after confused with right directory.
	1838 It must be included first before called.
*/


function displayDiv() {
	var div = document.createElement("div");
	div.style.border = "1px solid #fcc";
	div.style.background = "#fffafa";
	div.style.height = "20px";
	document.body.append(div);
}


// Display message in console
function displayHelloWorldInConsole() {
	console.log("Hello, World!");
}
