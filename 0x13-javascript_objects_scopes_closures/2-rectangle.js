#!/usr/bin/node

const Rectangle = class {
  constructor (w, h) {
    this.width = parseInt(w) > 1 ? w : undefined;
    this.height = parseInt(h) > 1 ? h : undefined;
  }
};

module.exports = Rectangle;
