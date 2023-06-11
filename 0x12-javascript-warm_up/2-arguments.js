#!/usr/bin/node

const args = process.argv;

const result = args.length <= 2 ? 'No argument' : 'Argument found';

console.log(result);
