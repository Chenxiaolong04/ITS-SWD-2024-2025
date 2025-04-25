# 03-movie-database

**Author**: Chen Xiaolong  
**Email**: xiao.chen@edu-its.it  

## Exercise Requirements
● Create an object to store the following information about a movie: title (a
string), duration (a number), and stars (an array of strings).

● Create an Array of objects that can hold several movies.
● Create a function to print out the movie information like so: "Puff the Magic
Dragon lasts for 30 minutes. Stars: Puff, Jackie, Living Sneezes."

● Test the function by printing one movie.

● Use the function to print all the movies in the Array.

## Problem Description

The goal of this project is to:
1. Store details about movies in an array.
2. Iterate through the array to print the movie's title, duration, and main actors in a human-readable format.
3. Print the details of a specific movie (in this case, the first movie in the array).

### Requirements:
- JavaScript knowledge for array iteration and basic console logging.
- Understanding of JSDoc annotations for documenting code.

## Approach to Solution

1. **Data Representation**:
   - The `movies` array holds multiple movie objects. Each movie object contains:
     - A `title` (string) representing the movie's name.
     - A `duration` (number) representing how long the movie is, in minutes.
     - A `stars` (array of strings) listing the movie's main actors.

2. **Iterating Through Movies**:
   - We use a `for` loop to iterate over each movie in the `movies` array.
   - For each movie, the details (title, duration, and stars) are printed in a formatted string.

3. **Logging the First Movie**:
   - The code includes a direct `console.log` statement to print the details of the first movie in the array.

4. **JSDoc Comments**:
   - The code is documented using JSDoc comments to describe the purpose and expected data types of variables, functions, and parameters. This provides clarity and helps with code maintenance and readability.

## Code Example

```javascript
/**
 * @file main.js
 * @author Chen Xiaolong
 */

/**
 * Logs details of each movie including title, duration, and stars.
 * 
 * @param {Array<{title: string, duration: number, stars: string[]}>} movies - Array of movie objects. Each movie object contains:
 * - `title`: The name of the movie (string).
 * - `duration`: The duration of the movie in minutes (number).
 * - `stars`: An array of strings containing the names of the main actors in the movie.
 */
function moviesPrint(movies) {
    for (let i in movies) {
        console.log(`${movies[i].title} lasts for ${movies[i].duration} minutes. Stars: ${movies[i].stars.join(", ")}`);
    }
}

/**
 * Array of movie objects.
 * Each object represents a movie with a title, duration, and an array of stars (actors).
 * @type {Array<{title: string, duration: number, stars: string[]}>}
 */
const movies = [
    {
      title: "Inception",
      duration: 148,
      stars: ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"]
    },
    {
      title: "La vita è bella",
      duration: 116,
      stars: ["Roberto Benigni", "Nicoletta Braschi", "Giorgio Cantarini"]
    }
  ];

/**
 * Logs the details of the first movie in the array.
 * This is a simple demonstration of logging an individual object from the movies array.
 */
console.log(movies[0]);

// Prints details of all movies
moviesPrint(movies);
