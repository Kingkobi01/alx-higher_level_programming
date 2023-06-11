#!/usr/bin/node

const Rectangle = class {
  constructor (w, h) {
    if (parseInt(w, 10) && parseInt(h, 10) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = this.height; i > 0; i--){
      console.log('x'.repeat(this.width));
    }
  }
};

module.exports = Rectangle;
