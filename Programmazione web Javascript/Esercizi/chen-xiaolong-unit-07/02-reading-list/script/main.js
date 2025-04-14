/**
 * @file Main game file for Hangman game
 * @author Chen Xiaolong
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
for(let i in books) {
    if(books[i].alreadyRead)
        console.log(`You already read ${books[i].title} by ${books[i].author}`)
    else
        console.log(`You still need to read ${books[i].title} by ${books[i].author}`)
}
