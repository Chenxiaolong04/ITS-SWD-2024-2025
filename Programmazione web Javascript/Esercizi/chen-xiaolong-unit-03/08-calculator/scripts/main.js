/**
 * Description placeholder
 *
 * @param {number} num 
 * @returns 
 */
function squareNumber(num) {
    console.log("The result of squaring the number " + num + " is " + (num * num));
    return num * num;
}
/**
 * Description placeholder
 *
 * @param {number} num 
 * @returns 
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
 * @returns 
 */
function percentOf(num1, num2) {
    console.log(num1 + " is " + ((num1 / num2) * 100) + "% of " + num2);
    return (num1 / num2) * 100;
}
/**
 * Description placeholder
 *
 * @param {number} radius 
 * @returns 
 */
function areaOfCircle(radius) {
    let area = Math.PI * radius*radius;
    console.log("The area for a circle with radius " + radius + " is " + area.toFixed(2));
    return area;
}
/**
 * Description placeholder
 *
 * @param {number} num 
 */
function calculator(num) {
    let half = halfNumber(num);
    let squared = squareNumber(half);
    let area = areaOfCircle(squared);
    let percent=percentOf(area, squared);
}
calculator(10);