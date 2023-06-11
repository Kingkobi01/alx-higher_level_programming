#!/usr/bin/node

let numOfLogs = 0;

module.exports.logMe = (item) => {
  console.log(`${numOfLogs}: ${item}`);
  numOfLogs += 1;
};
