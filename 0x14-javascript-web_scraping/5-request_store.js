#!/usr/bin/node
// Get the contents of a webpage and stores it in a file

const url = process.argv[2];
const filename = process.argv[3];
const fs = require('fs');
const request = require('request');

request(url, (error, response) => {
  if (error) {
    console.log('code: ', error);
  }

  const content = response.toJSON().body;

  fs.writeFile(filename, content, 'utf-8', error => {
    if (error) {
      console.log(error);
    }
  });
});
