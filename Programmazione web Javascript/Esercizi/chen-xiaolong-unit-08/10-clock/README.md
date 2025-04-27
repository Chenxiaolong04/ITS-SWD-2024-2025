# 10-clock

**Author**: Chen Xiaolong  
**Email**: xiao.chen@edu-its.it  

## Exercice Requirement  

● Implement a javascript clock that prints the current time to the console
every second

● The output should be in the format HH:mm:ss e.g. 17:03:06

## Approach to Solution

1. **Get the Current Time**:
   - The `new Date()` function is used to retrieve the current date and time.
   - Using the `getHours()`, `getMinutes()`, and `getSeconds()` methods, we extract the hours, minutes, and seconds of the current time.

2. **Format the Time**:
   - To ensure that hours, minutes, and seconds are always displayed as two digits, we use the `padStart(2, '0')` method. This adds a leading zero if the value is less than 10.
     - For example, `5` becomes `05`.

3. **Output Every Second**:
   - The `setInterval()` function is used to print the current time every 1000 milliseconds (1 second).
   - Inside the `setInterval`, we create a formatted time string (`HH:mm:ss`) using the formatted hours, minutes, and seconds.
   - The formatted time is then logged to the console using `console.log()`.

4. **Continuous Execution**:
   - This process repeats every second due to the `setInterval`, and it will continue indefinitely unless manually stopped.

