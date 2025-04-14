/**
 * @file Main game file for Hangman game
 * @author Chen Xiaolong
 */
function moviesPrint(movies){
    for(let i in movies) {
        console.log(`${movies[i].title} lasts for ${movies[i].duration} minuter. Stars: ${movies[i].stars}`)
    }
} 
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
console.log(movies[0]);
moviesPrint(movies);

