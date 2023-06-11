#!/usr/bin/node

const Rectangle = class {
  constructor (w, h) {
    if (parseInt(w, 10) && parseInt(h, 10) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      let y = 0;
      while (y < this.width) {
        myVar += 'X';
        y++;
      }
      console.log(myVar);
    }
  }
};

module.exports = Rectangle;
