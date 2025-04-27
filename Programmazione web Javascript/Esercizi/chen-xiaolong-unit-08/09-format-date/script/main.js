/**
 * @file: main.js
 * @author: Chen Xiaolong
 */
/**
 * Formats the given date based on how much time has passed since it.
 *
 * @param {Date} date - The date to be formatted.
 * @returns {string} - The formatted date string.
 */
function formatDate(date) {
    let now = new Date();
    let diff = now - date; // Difference in milliseconds

    // Defining time constants in milliseconds
    let SECOND = 1000;
    let MINUTE = 60 * SECOND;
    let HOUR = 60 * MINUTE;
    let DAY = 24 * HOUR;

    // Switch case to handle different time intervals
    switch (true) {
        case (diff < SECOND):
            return "right now"; // Less than a second
        case (diff < MINUTE):
            let sec = Math.floor(diff / SECOND);
            return `${sec} sec. ago`; // Less than a minute
        case (diff < HOUR):
            let min = Math.floor(diff / MINUTE);
            return `${min} min. ago`; // Less than an hour
        default:
            let day=date.getDate();
            let month = (date.getMonth() + 1).toString().padStart(2, '0');
            let year=date.getFullYear().toString().slice(-2); 
            let hours=date.getHours().toString().padStart(2, '0'); 
            let minutes=date.getMinutes().toString().padStart(2, '0'); 
            return `${day}.${month}.${year} ${hours}:${minutes}`; 
    }
}   

let now = new Date();
console.log(formatDate(now));

let threeSecondsAgo = new Date(now - 6000);
console.log(formatDate(threeSecondsAgo));

let oneMinuteAgo = new Date(now - 60000);
console.log(formatDate(oneMinuteAgo));

let twoHoursAgo = new Date(now - 7200000);
console.log(formatDate(twoHoursAgo));



