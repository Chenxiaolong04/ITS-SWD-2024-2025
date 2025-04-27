# 09-format-date

**Author**: Chen Xiaolong  
**Contact**: xiao.chen@edu-its.it

## Exercise Requirements

Write a function formatDate(date) that accepts a date and outputs it as follows:
+ If less than a second has passed since the date, output "right now"
+ If less than a minute has passed since the date, output "n sec. ago"
+ If less than an hour has passed since the date, output "m min. ago"
+ Otherwise, output the date in this format "DD.MM.YY HH:mm"
    + e.g. 17.04.16 10:00

## Approach to Solution

1. **`formatDate` Function**:
    - The function calculates the difference between the current date and the given date in milliseconds.
    - It then uses this difference to determine which format to return:
        - If less than a second has passed, it returns `"right now"`.
        - If less than a minute has passed, it returns the number of seconds passed, formatted as `"n sec. ago"`.
        - If less than an hour has passed, it returns the number of minutes passed, formatted as `"m min. ago"`.
        - For longer intervals, it formats the date in the format `"DD.MM.YY HH:mm"`.
    
2. **Constants**:
    - Constants for seconds, minutes, hours, and days are defined to simplify the calculation of time differences.




