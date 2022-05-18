#!/usr/bin/node
// Displays status code of GET request

const axios = require('axios').default;
const url = process.argv[2];

axios.get(url).then(function (response) {
  console.log('code: ' + response.status);
}).catch(function (error) {
  console.log('code: ' + error.response.status);
});
