/**
 * @file main.js
 * @author Chen Xiaolong
 * @description Dynamically generates a list of books, adds images, and styles the books
 * based on whether they have been read or not.
 */

// List of books with properties title, author, and read status
let books = [
  {
    title: 'The Design of Everyday Things',
    author: 'Don Norman',
    alreadyRead: false
  },
  {
    title: 'The Most Human Human',
    author: 'Brian Christian',
    alreadyRead: false
  },
  {
    title: 'Se questo è un uomo',
    author: 'Primo Levi',
    alreadyRead: false
  },
  {
    title: 'Il settimo giorno',
    author: 'Yu Hua',
    alreadyRead: true
  }
];

// Get the <ul> element to append the books
let list = document.getElementById("book-list");

// Create an image element for the book cover (you can replace this with actual URLs if available)
books.forEach((book, index) => {
  let li = document.createElement("li");
  li.textContent = `${book.title} by ${book.author}`;
  let img = document.createElement("img");

  // Set book cover images
  if (index == 0) {
    img.src = "https://m.media-amazon.com/images/I/619ncDeLijL.jpg"; // Don Norman
  } else if (index == 1) {
    img.src = "https://m.media-amazon.com/images/I/71HMyqG6MRL.jpg"; // Brian Christian
  } else if (index == 2) {
    img.src = "https://m.media-amazon.com/images/I/41Br50iP2ZL._SY445_SX342_.jpg"; // Primo Levi - Se questo è un uomo
  } else if (index == 3) {
    img.src = "https://m.media-amazon.com/images/I/71BXNQD6K6L._AC_UL600_SR600,600_.jpg"; // Yu Hua - Il settimo giorno
  }

  img.style.width = "100px";
  img.style.display = "block";
  
  // Add the class based on whether the book is read or not
  li.classList.add(book.alreadyRead ? "read" : "not-read");

  li.appendChild(img);
  list.appendChild(li);
});

// Load external CSS after 5 seconds
setTimeout(() => {
  let link = document.createElement("link");
  link.rel = "stylesheet";
  link.href = "css/style.css"; // Adjust path to your external CSS
  document.head.appendChild(link);
}, 5000);
