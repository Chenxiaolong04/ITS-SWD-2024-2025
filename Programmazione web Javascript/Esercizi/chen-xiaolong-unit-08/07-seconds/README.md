# 07-seconds
**Author**: Chen Xiaolong  
**Contact**: xiao.chen@edu-its.it

## Exercise Requirements

Write two functions that based on the current date and time output the number
of seconds:
● getSecondsToday() returns the number of seconds from the beginning of
today
● getSecondsToTomorrow() returns the number of seconds till tomorrow
## Approach to Solution

1. **`getSecondsToday` Function**:
    - This function takes the current date as an input and extracts the hours, minutes, and seconds from it.
    - It then converts each unit (hours, minutes, seconds) into seconds and sums them up to return the total number of seconds passed since midnight.

2. **`getSecondsToTomorrow` Function**:
    - This function calculates the number of seconds remaining in the current day by subtracting the seconds passed (`currentSeconds`) from the total number of seconds in a day (86,400 seconds).

3. **Example Usage**:
    - The program first calls `getSecondsToday` with the current date and time to get the number of seconds passed since midnight.
    - Then, it calls `getSecondsToTomorrow` to calculate the remaining seconds until midnight.



