#!/usr/bin/node
class Rectangle{
	constructor(w,h)
	{
		if (typeof h === 'number' && h > 0 && typeof w === 'number' && w > 0)
		{
			this.width = w;
			this.height = h;
		}
	}
}

module.exports = Rectangle;
