#!/usr/bin/node

module.exports.nbOccurences = (list, searchElement) => {
  return list.filter(element => element === searchElement).length;
};
