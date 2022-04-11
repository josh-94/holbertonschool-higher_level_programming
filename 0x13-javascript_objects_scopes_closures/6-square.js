#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    if (c === undefined) {
      this.print('C');
    } else {
      this.print(c);
    }
  }
}
module.exports = Square;
