/**
 * Capitalizes the first letter of a given string.
 * @param {string} string - The input string.
 * @returns {void} - The function prints the result.
 */
function capital(string) {
    let letter = string[0].toUpperCase(); 
    let newString = letter + string.slice(1); 
    console.log(newString);
}

/**
 * Capitalizes the first letter of each word in a given string.
 * @param {string} string - The input string.
 * @returns {void} - The function prints the result.
 */
function capital2(string) {
    let words = string.split(" ");
    for (let i = 0; i < words.length; i++) {
        let letter = words[i][0].toUpperCase(); 
        words[i] = letter + words[i].slice(1); 
    }
    let newString = words.join(" "); 
    console.log(newString);
}

capital("hello world");  
capital2("hello world"); 
