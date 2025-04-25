/**
 * @file main.js
 * @author Chen Xiaolong
 */

/** 
 * An array containing various food items to be displayed.
 * @type {Array<string>}
 */
let list = [
    "Pizza", "Sushi", "Pasta", "Burger", "Tacos",
    "Ramen", "Falafel", "Risotto", "Curry", "Paella",
    "Sandwich", "Hot Dog", "Kebab", "Dumplings", "Burrito",
    "Pho", "Lasagna", "Tempura", "Chili", "Gnocchi",
    "Steak", "Quesadilla", "Pierogi", "Croissant", "Tortilla",
    "Waffle", "Donut", "Miso Soup", "Ceviche", "Baklava"
  ];
  
  /**
   * Current index tracking the position in the food items array.
   * @type {number}
   */
  let index = 0;
  
  /**
   * Displays food items from the list at 1-second intervals using setInterval.
   * Clears the interval when all items have been displayed.
   * @function
   */
  function showItemInterval() {
    if (index < list.length) {
      console.log(list[index]);
      index++;
    } else {
      clearInterval(timerInterval); 
    }
  }
  
  /**
   * Displays food items from the list at 1-second intervals using setTimeout.
   * Recursively calls itself until all items have been displayed.
   * @function
   */
  function showItemTimeOut() {
    if (index < list.length) {
      console.log(list[index]);
      index++;
      timerTimeout = setTimeout(showItemTimeOut, 1000);
    } 
  }

let timerInterval = setInterval(showItemInterval, 1000);
//setTimeout(showItemTimeOut, 1000);
