#!/usr/bin/node

module.exports.converter = (base) => {
  function myConverter (n) {
    return n.toString(base);
  }
  return myConverter;
};
