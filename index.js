// Import all packages
const prompt = require('prompt-sync')();
const axios = require('axios');
const CSVToJSON = require('csvtojson');
const Retrieve = require('./Retrieve.js');



async function gradeAirQuality() {
  //get data from csv file
  csvPMdata = await CSVToJSON().fromFile('epaPM2016.csv') //csv file name
  var i;
  for (i = 0; i < 121; i++) {
    rawPM[i] = csvPMdata[i].Conc;  //index = row number, .Conc = column header
  }

  // compare NASA data to set air quality standard
  if (rawPM[i] < 10)
		return "C"; //
	else if (rawPM[i] >= 10  & rawPM[i] < 50)
		return "B"; //
	else if (rawPM[i] >= 50)
		return "A"; //

}

async function typeOfAir() {
	const name = prompt('Enter contaminant to analyze: ');
	let input;
	switch (name) {
		case "Particulate Matter":
			//
			break;
		case "Carbon Dioxide":
			//
			break;
		default: // For user help
			//
			break;
	}
}
