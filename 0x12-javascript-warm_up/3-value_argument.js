#!/usr/bin/node
// Prints argv value

const argc = process.argv.length;
const args = process.argv;

if (argc >= 3) {
  console.log(args[2]);
} else {
  console.log('No argument');
}
