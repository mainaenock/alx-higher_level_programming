#!/usr/bin/node
const num = process.argv[2];
let intnum;
if (!isNaN(num)) {
  intnum = parseInt(num, 10);
  if (!isNaN(intnum)) {
    console.log('My number: ' + intnum);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
