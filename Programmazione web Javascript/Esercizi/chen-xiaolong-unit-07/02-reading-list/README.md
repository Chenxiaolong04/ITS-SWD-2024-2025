# 02-reading-list
**Author**: Chen Xiaolong  
**Contact**: xiao.chen@edu-its.it

## Exercise requirements
● Create an array of objects, where each object describes a book and has
properties for the title (a string), author (a string), and alreadyRead (a
boolean indicating if you read it yet).

● Iterate through the array of books. For each book, log the book title and
book author like so: "The Hobbit by J.R.R. Tolkien".

● Now use an if/else statement to change the output depending on whether
you read it yet or not. If you read it, log a string like 'You already read "The
Hobbit" by J.R.R. Tolkien', and if not, log a string like 'You still need to read
"The Lord of the Rings" by J.R.R. Tolkien.'


## Problem Description
The goal of this project is to manage a list of books and their reading status. The properties of each book include:
- **title**: The name of the book.
- **author**: The author of the book.
- **alreadyRead**: A boolean indicating if the book has been read or not.

The program should:
- Iterate through the list of books and print a message indicating whether the book has been read or still needs to be read.

## Approach to Solution
1. **Data Representation**:
   - The books are represented as an array of objects. Each object has the properties `title`, `author`, and `alreadyRead` to store information about a book's title, the author, and its reading status.

2. **Iterating Through Books**:
   - A `for...in` loop is used to iterate over each book in the `books` array.
   - For each book, a check is made on the `alreadyRead` property.
     - If `alreadyRead` is `true`, the program prints a message saying the book has been read.
     - If `alreadyRead` is `false`, the program prints a message saying the book still needs to be read.

3. **Logging Information**:
   - The program uses `console.log()` to display whether the book has been read or needs to be read, displaying both the book's title and author.

4. **JSDoc Comments**:
   - The code is documented using JSDoc comments to explain the purpose and type of each variable and function. This ensures the code is clear and maintainable.

