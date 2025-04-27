# 08-timed-conversion
**Author**: Chen Xiaolong  
**Contact**: xiao.chen@edu-its.it

## Exercise Requirements

We will modify ‘Temperature conversion’ exercise from the lesson about
functions

* Call celsiusToFahrenheit on temperatures from 0 to 100 so that one
temperature is printed to the console every second

    * Use setInterval to achieve this goal.

    * Do the same thing using setTimeout.

## Approach to Solution

1. **`celsiusToFahrenheit` Function**:
    - This function accepts a Celsius temperature as input and calculates its Fahrenheit equivalent using the formula:  
      `Fahrenheit = (Celsius * 9 / 5) + 32`
    - The result is then logged to the console.

2. **`setIntervalConversion` Function**:
    - This function uses `setInterval` to call the `celsiusToFahrenheit` function every second, starting from 0°C.
    - The temperature increases by 1°C each time, and the process stops automatically when the temperature exceeds 100°C.
    - The function will repeatedly log the conversion for each temperature at 1-second intervals.

3. **`setTimeoutConversion` Function**:
    - This function uses `setTimeout` inside a loop to convert each temperature from 0°C to 99°C.
    - Each conversion is delayed by a multiple of 1000 milliseconds (1 second), starting with 0ms for the first call.
    - The function logs the conversion result for each temperature after the specified delay.

4. **Example Usage**:
    - `setIntervalConversion` will continuously convert temperatures from 0°C to 100°C every second.
    - `setTimeoutConversion` will convert temperatures from 0°C to 99°C with a 1-second delay between each conversion.
    - Each conversion result will be printed in the console as follows:  
      `0°C is 32°F`, `1°C is 33.8°F`, `2°C is 35.6°F`, and so on.

