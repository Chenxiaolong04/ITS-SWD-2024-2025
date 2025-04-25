# 06-date-ago

**Author**: Chen Xiaolong  
**Contact**: xiao.chen@edu-its.it

## Exercise Requirements

● Create a function getDateAgo(date, days) that returns the day of the month
n days ago from the given date

● For instance, if today is the 20th, then getDateAgo(new Date(), 1) should be
19th and getDateAgo(new Date(), 2) should be 18th

● Test the function to make sure it works reliably with any valid Date object

● Decide what to do with a negative 'days' parameter

* e.g. getDateAgo(new Date(), -2)
## Approach to Solution

1. **Input Validation**  
   The function first checks if the `days` argument is a valid non-negative number. If not, an error message is logged.

2. **Date Calculation**  
   The function uses `getDate()` to obtain the current day of the month and subtracts the given number of days. If the resulting day is valid, it is returned. Otherwise, an error message is logged.

3. **Edge Case Handling**  
   If the number of days to subtract would result in a date that is less than or equal to 0, an error message is logged to indicate that the argument is too large.



