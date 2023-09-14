#!/usr/bin/node
let square = require("./5-square.js");

class Square extends square{
	charPrint(c){
		let print_char = "";
		if (c === undefined){
			print_char = 'X';
		}
		else
		{
			print_char = c;
		}

		for(let h = 0; h < this.height; h++){
			let line = "";
			for (let w = 0; w < this.width; w++){
				line += print_char;
			}
			console.log(line);
		}
	}
}

module.exports = Square
