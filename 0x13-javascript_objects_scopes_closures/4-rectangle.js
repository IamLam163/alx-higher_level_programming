#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
    // could also be written as this.width *= 2;
  }
}
module.exports = Rectangle;
