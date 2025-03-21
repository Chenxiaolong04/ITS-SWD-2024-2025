/**
 * Description placeholder
 *
 * @type {*}
 */
let globalResult;
/**
 * Description placeholder
 *
 * @param {number} num1 
 * @param {number} num2 
 */
function addNumbers(num1, num2) {
    let localResult=1;
    globalResult = num1 + num2;
    localResult += num1 + num2;
}
addNumbers(5, 7);
console.log(globalResult); 
console.log(localResult); 
