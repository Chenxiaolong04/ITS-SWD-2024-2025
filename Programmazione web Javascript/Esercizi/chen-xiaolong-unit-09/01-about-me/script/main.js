/**
 * @file: main.js
 * @author: Chen Xiaolong 
 */

//Change the body style so it has a font-family of "Arial, sans-serif"
let bodyStyle = document.body;
bodyStyle.style.fontFamily = "Arial, sans-serif";

//Replace each of the spans (nickname, favorites, hometown) with your own information
let nickname = document.getElementById("nickname");
let favorites = document.getElementById("favorites");
let homeTown = document.getElementById("hometown");

nickname.textContent = "Chen Xiaolong";
favorites.textContent = "JavaScript";
homeTown.textContent = "Aosta";

//Iterate through each li and change the class to "list-item"
let listItems = document.querySelectorAll("li");
for (let i = 0; i < listItems.length; i++) {
    listItems[i].className = "list-item";
}

//Create a new img element and set its src attribute to a picture of you
let img = document.createElement("img");
img.src = "https://i.imgur.com/ONcRJzA.jpeg"; 
img.style.width = "200px";  

//Append that element to the page
document.body.appendChild(img);

//The external css file should make items with the .list-item class white, bold and with an orange background
//The external css file should be applied after 4 seconds

setTimeout(() => {
  let link = document.createElement("link");
  link.rel = "stylesheet";
  link.href = "css/style.css";  
  document.head.appendChild(link);
}, 4000);