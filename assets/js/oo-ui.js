/*
	oo-ui.js
	User Interface for oo in designing some SVG objects
	
	Sparisoma Viridi | https://github.com/dudung
	
	20201010
	1827 Start this file after confused with right directory.
	1838 It must be included first before called.
	1936 Test displaySimpleUI and it works.
*/


// An UI



// Display button than can show message when it is clicked
function displaySimpleUI() {
	var msg = arguments[0];
	var div = document.createElement("div");
	div.style.border = "1px solid #fcc";
	div.style.background = "#fffafa";
	
	var btn = document.createElement("button");
	btn.innerHTML = "Click me!";
	var span = document.createElement("span");
	
	document.body.append(div);
	div.append(btn);
	div.append(span);
	
	btn.addEventListener("click", function() {
		span.innerHTML = "      " + msg;
	});
}


// Display message in console
function displayHelloWorldInConsole() {
	console.log("Hello, World!");
}
