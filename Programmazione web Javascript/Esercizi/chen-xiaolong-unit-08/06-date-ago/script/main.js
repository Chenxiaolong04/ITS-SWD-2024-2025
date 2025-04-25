/**
 * @file: main.js
 * @author: Chen Xiaolong
 */

/**
 * Returns the date of a given day in the past.
 * The function calculates a past date by subtracting a specified number of days from the current date.
 * If the number of days is invalid or the result would be a date before the start of the current month, it logs an error.
 *
 * @function
 * @param {Date} date - The current date from which to subtract days.
 * @param {number} days - The number of days to subtract from the date.
 * @returns {number|void} The calculated day of the month if valid, or logs an error if invalid.
 */
function getDateAgo(date, days) {
    if (typeof days != 'number' || days < 0) {
        console.log("Argument not valid");
        return;
    }
    let n = date.getDate() - days;
    if (n <= 0)
        console.log('The argument is higher than the current day ');
    else {
        console.log(n);
        return n;
    }
};

let date = new Date();
result = getDateAgo(date, 5);
