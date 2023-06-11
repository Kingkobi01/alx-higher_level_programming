#!/usr/bin/node
exports.callMeMoby = (a, anotherFunc) => {
  for (let i = 0; i < a; i++) anotherFunc();
};
