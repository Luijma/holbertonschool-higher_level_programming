#!/usr/bin/node
// script that writes to a file

const fs = require('fs');
const fileName = process.argv[2];
const content = process.argv[3];

fs.write(fileName, content, 'utf-8', err => {
  if (err) {
    console.error(err);
  }
});
