#!/usr/bin/node

const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films';

request(starWarsUri, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  body = JSON.parse(body);
  const results = body.results;
  let numberOfApperarances = 0  
  for (const film in films){
    if (isinArray(film.characters,'https://swapi-api.alx-tools.com/api/people/18'){

      numberOfAppearances += 1;
}
}
  console.log(numberOfAppearances);
});
