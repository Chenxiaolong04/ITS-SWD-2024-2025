/**
 * @file: main.js
 * @author: Chen Xiaolong
 */

/**
 * Calculates the number of seconds that have passed since midnight of the current day.
 * 
 * @function
 * @param {Date} currentDate - The current date object from which to calculate seconds.
 * @returns {number} The total number of seconds that have passed since midnight.
 */
function getSecondsToday(currentDate) {
    let currentHours = currentDate.getHours() * 3600;
    let currentMinutes = currentDate.getMinutes() * 60;
    let currentSeconds = currentDate.getSeconds();
    let result = currentHours + currentMinutes + currentSeconds;
    return result;
};

/**
 * Calculates the number of seconds remaining until midnight.
 * 
 * @function
 * @param {number} currentSeconds - The number of seconds passed since midnight.
 * @returns {number} The number of seconds remaining until midnight.
 */
function getSecondsToTomorrow(currentSeconds) {
    let secondsInDay = 86400; // Total number of seconds in a day
    return secondsInDay - currentSeconds;
}

let currentDate = new Date();
let nowInS = getSecondsToday(currentDate);

console.log("Seconds passed since midnight:", nowInS);
console.log("Seconds until midnight:", getSecondsToTomorrow(nowInS));
