#!/usr/bin/node
const x = process.argv[2];
let i = 0;
if (x === null || x === undefined || isNaN(x)) {
  console.log('Missing size');
}
for (i; i < x; i++) {
  console.log('X'.repeat(x));
}
