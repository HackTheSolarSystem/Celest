var sunFacts = [
	'One million Earths could ift inside the Sun!',
	'The Sun contains 99.86% of the mass in the Solar System!',
	'The Sun is an almost perfect sphere.',
	'The temperature inside the Sun can reach 15 million degrees Celsius!',
	'Light from the Sun takes eight minutes to reach Earth.',
	'The Sun travels at 220 kilometres per second.',
	'Becuase the Earth travels on an elliptcal orbit around the Sun, the distance from the Sun to Earth changes throughout the year.',
	'At around 4.5 billion years old, the Sun is middle-aged.'
	]
	
var factTimer = setInterval(loadFact, 2000);
	
function loadFact() {
	var randomNumber = Math.floor(Math.random() * sunFacts.length);
	$("#factDisplay")[0].innerHTML = sunFacts[randomNumber];
}


	