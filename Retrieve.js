const Retrieve = {

};

const axios = require('axios');
const CSVToJSON = require('csvtojson');

// csv corn yield per acre
Retrieve.PMdata = async function() {
	csvPMdata = await CSVToJSON().fromFile('//') //csv file name
	return PMdata[5].estimate; //index = row number, .estimate = column header
}

module.exports = Retrieve;
