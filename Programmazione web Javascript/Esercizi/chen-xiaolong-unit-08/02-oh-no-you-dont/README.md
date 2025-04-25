# 02-oh-no-you-dont

**Author**: Chen Xiaolong  
**Contact**: xiao.chen@edu-its.it  

---

## Exercise Requirements

● Write a function “useful” that does something useful in Javascript

● Schedule it to run after 10 seconds

● Write another function that cancels the 
scheduling of the first function

● Use the second function to cancel the first one
after 5 seconds and output
‘function cancelled’ to the console


---

## Approach to Solution

1. **Function Definitions**:
   - `useful()`: Logs numbers 1 through 10.
   - `cancelUseful(timeoutId)`: Cancels the scheduled timeout using `clearTimeout`.

2. **Timer Management**:
   - A timeout is stored in `usefulFunction` with `setTimeout`.
   - Another `setTimeout` invokes `cancelUseful` before `useful()` executes.

3. **Behavior**:
   - If the cancel function executes before the delay finishes, `useful()` will not run.
   - A message confirms the function was cancelled.

---

## Technologies Used

- JavaScript (ES6+)
- Node.js (if running in a local environment)

---

## Sample Output

