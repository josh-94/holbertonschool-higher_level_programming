#!/usr/bin/node
// script that prints the title of a Star Wars movie where the
// episode number matches a given integer.
const axios = require('axios');
const ID = process.argv[2];
const url = (`https://swapi-api.hbtn.io/api/films/${ID}`);
axios.get(url)
  .then(response => {
    console.log(response.data.title);
  });
