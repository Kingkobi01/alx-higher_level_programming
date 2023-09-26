#!/usr/bin/node

const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films';

request(starWarsUri, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  body = JSON.parse(body);
  const results = body.results;
  let numberOfAppearances = 0;
  for (const film of results) {
    const characters = film.characters;

    for (const character of characters) {
      const id = character.split('/')[5];
      if (id === 18) {
        numberOfAppearances += 1;
      }
    }
  }
  console.log(numberOfAppearances);
});
