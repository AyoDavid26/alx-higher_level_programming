#!/usr/bin/node
class Rectangle {
  constructor (x, y) {
    if ((x > 0) && (y > 0)) {
      this.width = x;
      this.height = y;
    }
  }
}

module.exports = Rectangle;
