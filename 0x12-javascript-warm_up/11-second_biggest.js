#!/usr/bin/node
const myArgv = process.argv.slice(2);
const size = myArgv.length;
if (size === 0 || size === 1) {
  console.log(0);
} else {
  myArgv.sort(function (a, b) {
    return (b - a);
  });
  console.log(myArgv[1]);
}
