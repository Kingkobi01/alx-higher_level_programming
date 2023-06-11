#!/usr/bin/node

const args = process.argv;

console.log(args[2] === undefined ? 'No argument' : args[2]);
