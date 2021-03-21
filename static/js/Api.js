$.getJSON("https://api.rootnet.in/covid19-in/stats/latest",function(data){
	console.log(data);

	var confirmedCases=data.data.summary.confirmedCasesIndian;
	console.log(confirmedCases);

	$('.case').append(confirmedCases);

	var death=data.data.summary.deaths;
	console.log(death);

	$('.death').append(death);

	var recovered=data.data.summary.discharged;
	console.log(recovered);

	$('.recover').append(recovered);
});