#!/usr/bin/node
// Prints number of movie Wedge Antilles is present

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log('code: ', error);
  }

  let count = 0;
  const content = JSON.parse(body).results;
  for (const film of content) {
    for (const j of film.characters) {
      if (j.includes('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
