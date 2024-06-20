#!/usr/bin/node
const x = process.argv[2];
let i = 0;
if (x === null || x === undefined) {
  console.log('Missing number of occurrences');
}
for (i; i < x; i++) {
  console.log('C is fun');
}
