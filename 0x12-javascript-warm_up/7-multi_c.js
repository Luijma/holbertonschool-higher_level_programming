#!/usr/bin/node
// prints x times 'C is fun'

const reps = process.argv[2];

if (!isNaN(reps)) {
  for (let i = 0; i < reps; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
