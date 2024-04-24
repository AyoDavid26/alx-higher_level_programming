#!/usr/bin/node
class Rectangle {
  constructor (x, y) {
    if ((x > 0) && (y > 0)) {
      this.width = x;
      this.height = y;
    }
  }

  print () {
    for (let i =0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
