#!/usr/bin/node

module.exports.converter = (base) => {
  const myConverter = (n) => n.toString(base);
  return myConverter;
};
