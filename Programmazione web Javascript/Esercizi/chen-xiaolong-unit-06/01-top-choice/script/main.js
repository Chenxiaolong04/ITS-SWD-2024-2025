/**
 * @file: main.js
 * @author: Chen Xiaolong 
 * @param {array} array 
 */
const array = [
    "Apple", "Banana", "Cat", "Dog", "Elephant", "Fish", "Giraffe", "House", "Ice", "Jupiter",
    "Kite", "Lion", "Moon", "Notebook", "Orange", "Pizza", "Quiet", "Rain", "Sun", "Tree",
    "Umbrella", "Violin", "Water", "Xylophone", "Yellow", "Zebra", "Ant", "Bear", "Coffee", "Door",
    "Earth", "Fire", "Guitar", "Hat", "Italy", "Japan", "Keyboard", "Lemon", "Mountain", "Night",
    "Ocean", "Pasta", "Queen", "Rock", "Sky", "Travel", "University", "Video", "Window", "Yoga",
    "Airplane", "Butterfly", "Cloud", "Diamond", "Eagle", "Flower", "Green", "Happy", "Internet", "Journey",
    "King", "Love", "Music", "Nature", "Olympics", "Peace", "Quality", "River", "Star", "Time",
    "Universe", "Victory", "Wonder", "X-ray", "Year", "Zen", "Art", "Beach", "Camera", "Dream",
    "Energy", "Future", "Game", "Health", "Island", "Joy", "Knowledge", "Light", "Magic", "Novel",
    "Open", "Power", "Quest", "Rose", "Smile", "Truth", "Unique", "Vision", "Wisdom", "Yacht",
    100, 42, 7, 33, 999, 123, 777, 55];
    for (let i = 0; i < array.length; i++){
    check=(i+1).toString();
    if(check[check.length-1]=="1")
        console.log(`My ${i+1}st choice is ${array[i]}`);
    else if(check[check.length-1]=="2")
        console.log(`My ${i+1}nd choice is ${array[i]}`);
    else if(check[check.length-1]=="3")
        console.log(`My ${i+1}rd choice is ${array[i]}`);
    else
        console.log(`My ${i+1}th choice is ${array[i]}`);
    //if(check[check.length-1]=="1")
        //console.log(My ${i+1}st choice is ${array[i]});
}
    