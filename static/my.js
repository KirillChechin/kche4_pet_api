
function coinFlip() {
	document.getElementById("one").innerHTML = "Hello JavaScript!";
	var img = document.createElement("img");
	img.src = "http://www.google.com/intl/en_com/images/logo_plain.png";
	var src = document.getElementById("one");
	src.appendChild(img);
}

function coinFlip() {
    var img = document.createElement("img");
    call = fetch("/coin").then((response) => response.json()).then((json) => console.log(json));
    img.src = call["file"]
     src.appendChild(img);
}