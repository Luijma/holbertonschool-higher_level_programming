#!/usr/bin/node
// prints a square of given size

const size = process.argv[2];

if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
