#!/usr/bin/node

const newArr = require('./100-data').list;

console.log(newArr);
console.log(newArr.map((x, idx) => x * idx));
