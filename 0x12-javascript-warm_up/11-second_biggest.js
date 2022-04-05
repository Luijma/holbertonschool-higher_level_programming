#!/usr/bin/node
// finds second biggest number in integers
const args = process.argv;
const argc = process.argv.length;
let biggest = args[2];
let second = args[2];

for (let i = 2; i < argc; i++) {
  if (parseInt(args[i]) > parseInt(biggest)) {
    second = biggest;
    biggest = args[i];
  }
}

if (argc <= 3) {
  console.log(0);
} else {
  console.log(second);
}
