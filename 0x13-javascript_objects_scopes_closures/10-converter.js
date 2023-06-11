#!/usr/bin/node

module.exports.converter = (base) => {
  function myConverter (n) {
    n.toString(base);
  }
  return myConverter;
};
