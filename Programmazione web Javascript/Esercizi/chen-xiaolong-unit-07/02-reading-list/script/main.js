/**
 * @file main.js
 * @author Chen Xiaolong
 */

/**
 * Array containing a list of books, each with a title, author, and reading status.
 * @type {Array<{title: string, author: string, alreadyRead: boolean}>}
 */
const books = [
    {
        title: "Se questo è un uomo",
        author: "Primo Levi",
        alreadyRead: true
    },
    {
        title: "Il settimo giorno",
        author: "Yu Hua",
        alreadyRead: true
    },
    {
        title: "1984",
        author: "George Orwell",
        alreadyRead: false
    }
];

/**
 * Iterates through the array of books and logs whether each book has been read or still needs to be read.
 * @param {Array<{title: string, author: string, alreadyRead: boolean}>} books - Array of book objects with title, author, and reading status.
 */
for (let i in books) {
    if (books[i].alreadyRead)
        console.log(`You already read ${books[i].title} by ${books[i].author}`);
    else
        console.log(`You still need to read ${books[i].title} by ${books[i].author}`);
}
