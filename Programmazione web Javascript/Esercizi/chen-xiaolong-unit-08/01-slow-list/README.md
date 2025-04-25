# 01-slow-list

Author: Chen Xiaolong  
Contact: xiao.chen@edu-its.it  

## Exercise Requirements

* Create an array that holds a list of 30 items (food, books, etc.)

* Print one item of the list every second until the list is completely printed

    * Use setInterval to achieve this goal

    * Do the same thing using setTimeout

## Problem Description

The goal of this project is to demonstrate two different timing approaches in JavaScript for displaying a sequence of items. The program works with a fixed array of 30 international food items.

The implementation shows:
- How to manage intervals in JavaScript
- How to track progress through an array
- How to clean up timers when done
- Alternative approaches to timed execution

## Approach to Solution

### Implementation Details:

1. **Data Structure**: Uses a predefined array containing 30 food items.
2. **Index Tracking**: Uses a counter variable to track current position in the array.
3. **Interval Approach**:
   - Uses `setInterval` to trigger display every second
   - Clears interval when all items are shown
4. **Timeout Approach** (commented out):
   - Uses recursive `setTimeout`
   - Each display schedules the next one
   - Automatically stops when done

### Key Functions:

- `showItemInterval()`: Displays items using interval approach
- `showItemTimeOut()`: Displays items using timeout approach (alternative)

### Example Usage:

```javascript
// Using setInterval (active implementation)
let timerInterval = setInterval(showItemInterval, 1000);

// Alternative using setTimeout (commented out)
// let timerTimeout = setTimeout(showItemTimeOut, 1000);