#!/usr/bin/node
// Prints argv value

const arg = process.argv[2];

if (arg != undefined) {
  console.log(arg);
} else {
  console.log('No argument');
}
