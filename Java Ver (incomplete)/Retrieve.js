const Retrieve = {

};

const axios = require('axios');
const CSVToJSON = require('csvtojson');

// csv particulate matter data
Retrieve.PMdata = async function() {
	csvPMdata = await CSVToJSON().fromFile('epaPM2016.csv') //csv file name
  var i;
  for (i = 0; i < 121; i++) {
    rawPM[i] = PMdata[i].Conc;  //index = row number, .Conc = column header
  }
	return rawPM;
}

module.exports = Retrieve;
