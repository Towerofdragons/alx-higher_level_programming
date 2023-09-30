#!/usr/bin/node
const v = process.argv[2];

if (!parseInt(v)) {
	  console.log('Missing number of occurrences');
} else {
	  for (let i = 0; i < v; i++) {
		      console.log('C is fun');
		    }
}
