#!/usr/bin/node
// computes and prints a factorial

// Recursive function to calculate factorial
function factorial (number) {
  if (!number) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

const arg = parseInt(process.argv[2]);
console.log(factorial(arg));
