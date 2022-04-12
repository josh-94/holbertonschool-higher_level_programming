#!/usr/bin/node
const list = require('./100-data').list;
const nlist = list.map((e, i) => e * i);
console.log(list);
console.log(nlist);
