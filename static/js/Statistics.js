$.getJSON("https://api.rootnet.in/covid19-in/hospitals/beds",function(data){
	console.log(data);

	var bedStats=data.data.regional;
	console.log(bedStats);

	
		for(var i=0;i<bedStats.length;i++){
			document.write("State: "+bedStats[i].state+" Total Hospitals: "+bedStats[i].totalHospitals+" Total Beds: "+bedStats[i].totalBeds);
		}
	

	// $('.con').html(collector);
	



	// var confirmedCases=data.data.summary.confirmedCasesIndian;
	// console.log(confirmedCases);

	// $('.case').append(confirmedCases);

});