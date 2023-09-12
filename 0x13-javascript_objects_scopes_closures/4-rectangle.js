#!/usr/bin/node

class Rectangle{
		constructor(w, h)
		{
			if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0)
			{
		         this.width = w;
			this.height = h;
			}
		}

	print() {
			for (let i = 0; i < this.height; i++)
			{
				let line = "";
				let y = 0;

				while (y < this.width)
				{
			 	line += "X";
		         	y++;
				}
				console.log(line);
			}
	        }

	rotate() {
		let temp = this.height;
		this.height = this.width;
		this.width = temp;
	}

	double() {
		this.height = this.height * 2;
		this.width = this.width *2;

	}
}

module.exports = Rectangle;

