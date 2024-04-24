#!/usr/bin/node
class Rectangle {
  constructor (x, y) {
    if ((x > 0) && (y > 0)) {
      this.width = x;
      this.height = y;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j =0; j < this.width; j++) {
        s += 'X';
      }
      console.log(S);
    }
  }
}

modlue.exports = Rectangle;
