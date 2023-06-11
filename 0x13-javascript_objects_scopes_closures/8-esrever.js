#!/usr/bin/node

module.exports.esrever = (list) => {
  const reversedList = [];
  while (list.length !== 0) {
    reversedList.push(list.pop());
  }
  return reversedList;
};
