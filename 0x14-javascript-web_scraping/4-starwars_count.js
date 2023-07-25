#!/usr/bin/node
const request = require('request');
const charId = 18;

request
  .get(process.argv[2], (e, response, body) => {
    if (e) {
      console.log(e);
    }
    const cont = JSON.parse(body).results.filter((elem) => {
      return elem.characters.filter((url) => { return url.includes(charId); }).length;
    }).length;
    console.log(cont);
  });
