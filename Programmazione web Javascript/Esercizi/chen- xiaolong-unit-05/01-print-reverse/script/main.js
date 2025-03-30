/**
 * @file: main.js
 * @author: Chen Xiaolong
 * Reverses a string and prints it to the console.
 * 
 * @param {string} x - The string to be reversed.
 * @returns {string} The reversed string.
 */
function printReverse(x) {
    let y = "";
    for (let i = x.length - 1; i >= 0; i--) {
        y += x[i];
    }
    console.log(y);

}

printReverse("0123456789");
