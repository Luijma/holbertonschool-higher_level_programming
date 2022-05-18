#!/usr/bin/node
// prints all characters of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(url, function (error, response, body) {
  if (error) {
    console.log('code: ', error);
  }
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; ++i) {
    request(characters[i], function (err, res, bdy) {
      if (err) {
        console.log('code: ', err);
      }
      console.log(JSON.parse(bdy).name);
    });
  }
});
