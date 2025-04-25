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
//console.log(movies[0]);

// Prints details of all movies
moviesPrint(movies);
