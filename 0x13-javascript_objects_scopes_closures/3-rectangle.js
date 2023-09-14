#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      return {};
    } else {
	this.width = w;
	this.wheight = h;
    }
  }
print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) { process.stdout.write('X'); }
      console.log('');
    }
  }
};
module.exports = Rectangle;
