#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (size !== 0 && !size) {
  console.log('Missing size');
} else {
  for (let s1 = size; s1 > 0; s1--) {
    console.log('x'.repeat(size));
  }
}
