/**
 * @file: main.js
 * @author: Chen Xiaolong
 */

/**
 * Custom implementation of setInterval that stops after 15 executions.
 * Calls a function repeatedly with a specified delay between each call.
 *
 * @function
 * @param {Function} func - The function to execute repeatedly.
 * @param {number} [delay=0] - Delay in milliseconds between executions.
 * @param {...any} args - Arguments to pass to the function being executed.
 * @returns {void}
 */
let count = 0;
function mySetInterval(func, delay = 0, ...args) {
    count++;
    if (count >= 15) {
        return;
    }
    setTimeout(() => {
        func(...args);
        mySetInterval(func, delay, ...args);
    }, delay);
}

/**
 * Sample function to be passed into mySetInterval.
 * Logs "Hello World!" to the console.
 * @function
 * @returns {void}
 */
function test() {
    console.log("Hello World!");
};

// Start the custom interval
mySetInterval(test, 1000);
