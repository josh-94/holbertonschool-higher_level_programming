#!/bin/usr/node
exports.esrever = function (list) {
  const new_list = [];
  list.forEach(value => new_list.unshift(value));
  
  return(new_list);
};
