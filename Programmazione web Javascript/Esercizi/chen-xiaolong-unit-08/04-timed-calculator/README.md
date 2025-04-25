# 04-timed-calculator

**Author**: Chen Xiaolong  
**Contact**: xiao.chen@edu-its.it

## Exercise Requirements
● We will modify ‘Calculator’ exercise from the lesson about functions

● Rewrite the last function that performs all 4 operations so that there is a
delay of 3 seconds between one operation and the next
Create several functions to perform basic math operations:
- `squareNumber()`: squares a number.
- `halfNumber()`: returns half a number.
- `percentOf()`: returns what percentage one number is of another.
- `areaOfCircle()`: calculates the area of a circle given the radius.

Create a `calculator()` function that:
- Takes a number as input.
- Halves it, squares the result, uses that squared number as the radius of a circle to get the area.
- Then calculates what percent the area is of the squared number.
- Each step is delayed using `setTimeout()`.

## Approach to Solution

1. **Modular Functions**  
   Each math operation is implemented in a separate function, making the code clean and reusable.

2. **Logging and Return Values**  
   Each function logs its result to the console and returns the computed value.

3. **Timed Sequence**  
   The `calculator()` function runs the operations in sequence with a 3-second interval between each, using `setTimeout()` to demonstrate asynchronous logic.


