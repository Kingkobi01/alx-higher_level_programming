#!/usr/bin/node
const callMeMoby = (a, anotherFunc) => {
  for (a <= 0; a--; ) {
    anotherFunc();
  }
};

module.exports = { callMeMoby };
