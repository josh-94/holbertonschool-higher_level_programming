#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    let suma = 0;
    for (let i of list) {
        if (i == searchElement) suma += 1;
    } return (suma);
}
