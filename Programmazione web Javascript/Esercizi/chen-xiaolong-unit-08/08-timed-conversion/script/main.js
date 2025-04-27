/**
 * @file: main.js
 * @author: Chen Xiaolong
 */
/**
 * Converts a temperature from Celsius to Fahrenheit and logs the result.
 *
 * This function takes a temperature in degrees Celsius and converts it into Fahrenheit.
 * The result is logged to the console.
 *
 * @param {number} celsius - The temperature in degrees Celsius.
 * @example
 */
function celsiusToFahrenheit(celsius) {
    console.log(`${celsius}°C is ${celsius * 9 / 5 + 32}°F`);
}

let temperature = 0;

/**
 * Calls the celsiusToFahrenheit function every second for temperatures from 0 to 100.
 *
 * This function repeatedly calls the `celsiusToFahrenheit` function every 1000 milliseconds
 * (1 second), starting with 0°C and increasing by 1°C at each interval.
 * The process stops automatically when the temperature exceeds 100°C.
 *
 * @example
 * setInterval function will call celsiusToFahrenheit for temperature 0, then 1, 2, ..., 100.
 */
let intervalId = setInterval(() => {
    celsiusToFahrenheit(temperature);
    temperature++;
    if (temperature > 100) {
        clearInterval(intervalId);
    }
}, 1000);

/**
 * Calls the celsiusToFahrenheit function with temperatures from 0 to 100 using setTimeout.
 */
for (let i = 0; i <= 100; i++) {
    setTimeout(() => {
        celsiusToFahrenheit(i);
    }, 1000 * i);
}
