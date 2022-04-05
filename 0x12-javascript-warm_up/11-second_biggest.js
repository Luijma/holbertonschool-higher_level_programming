#!/usr/bin/node
// finds second biggest number in integers
const args = process.argv.slice(2);
const argc = process.argv.length;

if (argc <= 3) {
  console.log(0);
} else {
  args.sort((a, b) => { return b - a; });
  const second = args[1];
  console.log(second);
}
