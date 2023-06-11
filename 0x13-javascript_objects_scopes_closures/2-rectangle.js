#!/usr/bin/node

const Rectangle = class {
  constructor (w, h) {
    if (parseInt(w, 10) && parseInt(h, 10) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};

module.exports = Rectangle;
