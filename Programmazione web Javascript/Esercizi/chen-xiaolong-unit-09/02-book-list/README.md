# My Book List

This project dynamically generates a list of books and displays them with their titles, authors, and cover images. It also changes the appearance of the books based on whether they have been read or not.

## Features

- **Dynamically Generated List**: The list of books is generated dynamically using JavaScript from an array of book objects.
- **Book Details**: For each book, the title, author, and cover image are displayed.
- **Read/Unread Status**: Books that have been read are styled with a green background and green text, while unread books have a red background and red text.
- **Image Support**: Each book has a cover image that is displayed next to its title and author.
- **Delayed CSS Load**: The external CSS file is loaded 5 seconds after the page is loaded.

## How It Works

### HTML Structure
The main structure consists of a list (`<ul>`) with list items (`<li>`) for each book. Each `<li>` contains:
- The book's title and author
- An image element displaying the book's cover
- The background color and text color based on whether the book has been read or not

### JavaScript
1. The `books` array contains the book data (title, author, read status).
2. The JavaScript iterates through the array and dynamically creates `<li>` elements for each book.
3. The cover image for each book is dynamically set based on its index in the array.
4. The book's read status is used to assign the appropriate CSS class (`read` or `not-read`).
5. The external CSS file is loaded after a delay of 5 seconds to apply additional styling.

### CSS
The styling is handled through a CSS file that:
- Applies a green background and green text for books marked as read (`.read` class).
- Applies a red background and red text for books marked as not read (`.not-read` class).

## Files

- `index.html`: The main HTML file containing the structure of the page.
- `main.js`: The JavaScript file responsible for dynamically creating the list of books and managing their styles.
- `css/style.css`: The external CSS file that applies the styles for read and unread books.
- `images/`: The folder containing the book cover images.


