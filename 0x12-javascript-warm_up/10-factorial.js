#!/usr/bin/node
function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
if (isNaN(process.argv[2])) {
  process.argv[2] = 1;
}
console.log(factorial(process.argv[2]));
