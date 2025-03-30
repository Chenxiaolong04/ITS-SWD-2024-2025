/**
 * @file main.js
 * @author Chen Xiaolong
 * @description Functions to check if a word is a palindrome.
 *
 * 
/**
 * Checks if a word is a palindrome without using built-in functions.
 *
 * @param {string} word - The word to check.
 * @returns {boolean} True if the word is a palindrome, otherwise false.
 */
function reverseWithoutFunction(word) {
    let reverse = "";
    for (let i = word.length - 1; i >= 0; i--) {
        reverse += word[i];
    }
    return word === reverse;
}

/**
 * Checks if a word is a palindrome using built-in functions.
 *
 * @param {string} word - The word to check.
 * @returns {boolean} True if the word is a palindrome, otherwise false.
 */
function reverseWithFunction(word) {
    let temp = word.split("").reverse().join("");
    return word === temp;
}

let resultReverseWithoutFunction = reverseWithoutFunction("madam");
let resultReverseWithFunction = reverseWithFunction("madame");

console.log(resultReverseWithoutFunction); // true
console.log(resultReverseWithFunction);    // false
