/**
 * @file Function to get weekday abbreviation in different languages
 * @author Chen Xiaolong
 */

/**
 * Returns and displays the weekday abbreviation for a given date and language
 * @function
 * @param {number} date - Numeric representation of the day (0-6 where 0 is Sunday)
 * @param {string} language - Language code ('en' for English, 'it' for Italian)
 * @returns {void}
 */
function getWeekDay(date, language) {
    let dayNames;
    if (language == 'en') {
        dayNames = ['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA'];
    } else if (language == 'it') {
        dayNames = ['DO', 'LU', 'MA', 'ME', 'GI', 'VE', 'SA'];
    } else {
        console.log('Unsupported language');
        return;
    }

    console.log(dayNames[date]);
}

/**
 * Current day object
 * @type {Date}
 */
let day = new Date();

/**
 * Numeric representation of current weekday (0-6 where 0 is Sunday)
 * @type {number}
 */
let weekday = day.getDay();

getWeekDay(weekday, 'it');
