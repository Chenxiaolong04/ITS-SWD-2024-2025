# 05-my-setinterval

**Author**: Chen Xiaolong  
**Contact**: xiao.chen@edu-its.it

## Exercise Requirements

● Pretend that setInterval() doesn't exist

● Re-create it using setTimeout naming your 
function mySetInterval

● Test your new function

● Modify your function so that it automatically stops after 15 intervals

## Approach to Solution

1. **Recursive Timeout**  
   The `mySetInterval` function uses `setTimeout` recursively to emulate interval behavior.

2. **Execution Counter**  
   A global `count` variable is incremented on each call to keep track of executions and stop after 15 iterations.

3. **Spread Operator for Arguments**  
   The use of `...args` allows passing an arbitrary number of arguments to the callback function.

4. **Example Function**  
   A `test` function is used as an example, logging "Hello World!" every second for 15 seconds.



