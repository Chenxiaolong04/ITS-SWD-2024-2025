# 10-weekday-abbreviation

**Author**: Chen Xiaolong  
**Contact**: xiao.chen@edu-its.it

## Exercise Requirements

Create a function that returns the abbreviation of a weekday based on the language and numeric date input.  
The function should:
- Accept a numeric input representing the weekday (0–6, where 0 is Sunday).
- Accept a language code (e.g., `'en'` or `'it'`).
- Display the corresponding day abbreviation in the console.

## Approach to Solution

1. **Understanding the Date Object**  
   JavaScript’s `Date.getDay()` method returns a number from 0 (Sunday) to 6 (Saturday). This number is stored in a variable to be used in the abbreviation logic.

2. **Language-Based Output**  
   The function `getWeekDay()` receives a language code and uses a predefined array to print the appropriate abbreviation based on the numeric day.

3. **Console Output**  
   The result is printed to the console using `console.log()`. If an unsupported language is passed, it will output `'Unsupported language'`.






