/**
 * @file: main.js
 * @author: Chen Xiaolong
 */

/**
 * Squares a number and logs the result.
 * @param {number} num - The number to square.
 * @returns {number} The squared value.
 */
function squareNumber(num) {
    console.log("The result of squaring the number " + num + " is " + (num * num));
    return num * num;
}

/**
 * Returns half of a number and logs the result.
 * @param {number} num - The number to halve.
 * @returns {number} Half of the input number.
 */
function halfNumber(num) {
    console.log("Half of " + num + " is " + (num / 2));
    return num / 2;
}

/**
 * Calculates what percentage num1 is of num2 and logs it.
 * @param {number} num1 - The part value.
 * @param {number} num2 - The total value.
 * @returns {number} The percentage value.
 */
function percentOf(num1, num2) {
    console.log(num1 + " is " + ((num1 / num2) * 100) + "% of " + num2);
    return (num1 / num2) * 100;
}

/**
 * Calculates the area of a circle given a radius and logs it.
 * @param {number} radius - The radius of the circle.
 * @returns {number} The area of the circle.
 */
function areaOfCircle(radius) {
    let area = Math.PI * radius * radius;
    console.log("The area for a circle with radius " + radius + " is " + area.toFixed(2));
    return area;
}

/**
 * @param {number} num - The number to process.
 */
function calculator(num) {
    let half, squared, area, percent;
    setTimeout(() => {
        half = halfNumber(num);
    }, 3000);  
    setTimeout(() => {
        squared = squareNumber(half);
    }, 6000);
    setTimeout(() => {
        area = areaOfCircle(squared);
    }, 9000);
    setTimeout(() => {
        percent = percentOf(area, squared);
    }, 12000);
}

// Example usage
calculator(10);
