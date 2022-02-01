#!/usr/bin/node

let url = process.argv[2];
const request = require('request');

request(url, (err, response) =>{
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});