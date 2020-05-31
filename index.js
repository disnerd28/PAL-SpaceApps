// Import all packages
const prompt = require('prompt-sync')();
const axios = require('axios');
const CSVToJSON = require('csvtojson');
const Retrieve = require('./Retrieve.js');



async function gradeAirQuality() {
  //get data from csv file

  // compare user input to calculated csv total and return grade for pesticides

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
