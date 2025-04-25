/**
 * @file main.js
 * @author Chen Xiaolong
 */

/**
 * Function that logs numbers from 1 to 10 with a delay.
 * It uses a `for` loop to log the numbers.
 */
function useful() {
    for (let i = 0; i < 10; i++) {
        console.log(i + 1);
    }
};

/**
 * Function that cancels the execution of a setTimeout function.
 * It uses `clearTimeout` to cancel the `usefulFunction` timeout.
 * @param {NodeJS.Timeout} usefulFunction - The timeout reference to cancel.
 */
function cancelUseful(usefulFunction) {
    clearTimeout(usefulFunction);
    console.log("Function cancelled");
}

/**
 * Sets a timeout for the `useful` function to run after 10 seconds.
 * @type {NodeJS.Timeout}
 */
let usefulFunction = setTimeout(useful, 10000);

/**
 * Sets another timeout to cancel the `useful` function after 5 seconds.
 * @type {NodeJS.Timeout}
 */
setTimeout(() => cancelUseful(usefulFunction), 5000);
