# 01-top-choice
Autor: Chen Xiaolong  
Contact: xiao.chen@edu-its.it
___
### Exercise Requirements

Create an array to hold your top choices (colors, pets, books, whatever).
For each choice, log to the screen a string like: "My #1 choice is blue."
Bonus: Change it to add the correct number suffix, e.g. "My 1st choice, "My 2nd
choice", "My 3rd choice", "My 4th choice", etc.

### Approach to Solution

- Create an array of words and numbers.
- Use a `for` loop to iterate over the array.
- Compute each item's position (`i + 1`).
- Determine the correct suffix based on the last digit of the number.
- Print the result to the console.