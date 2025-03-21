/**
 * Description placeholder
 *
 * @param {number} num 
 * @returns {number} 
 */
function squareNumber(num) {
    console.log("The result of squaring the number " + num + " is " + (num * num));
    return num * num;
}
/**
 * Description placeholder
 *
 * @param {number} num 
 * @returns {number} 
 */
function halfNumber(num) {
    console.log("Half of " + num + " is " + (num / 2));
    return num / 2;
}
/**
 * Description placeholder
 *
 * @param {number} num1 
 * @param {number} num2 
 * @returns {number} 
 */
function percentOf(num1, num2) {
    console.log(num1 + " is " + ((num1 / num2) * 100) + "% of " + num2);
    return (num1 / num2) * 100;
}
/**
 * Description placeholder
 *
 * @param {number} radius 
 * @returns {number} 
 */
function areaOfCircle(radius) {
    let area = Math.PI * radius*radius;
    console.log("The area for a circle with radius " + radius + " is " + area.toFixed(2));
    return area;
}
squareNumber(5);
halfNumber(5);
percentOf(2, 10);
areaOfCircle(2);