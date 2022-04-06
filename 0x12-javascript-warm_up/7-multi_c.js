#!/usr/bin/node
const MyVar = 'C is fun';
let n = parseInt(process.argv[2]);
if (n) {
  for (; n > 0; n--) {
    console.log(MyVar);
  }
} else {
  console.log('Missing number of occurrences');
}
