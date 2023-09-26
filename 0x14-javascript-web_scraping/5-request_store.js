#!/usr/bin/node

const fs = require('fs');
const request = require('request');

async function requestStore (uri, destination) {
  request(uri, function (error, response, body) {
    if (error) {
      console.log(error);
    }
    fs.writeFileSync(destination, body, 'utf-8', function (err) {
      console.log(err);
    });
  });
}

requestStore(process.argv[2], process.argv[3]);
