#!/usr/bin/node
// Script that reads and prints contents in a file
const fs = require('fs');

const fileName = process.argv[2];

fs.readFile(fileName, 'utf8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
