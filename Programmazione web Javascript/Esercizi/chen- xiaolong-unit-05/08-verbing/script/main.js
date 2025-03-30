/**
 * Modifies a word by adding "ing" or "ly" based on specific conditions.
 * @param {string} str - The input word to modify.
 * @returns {string} - The modified word.
 */
function verbing(str) {
    if (str.length < 3) {
        return str;
    } 
    if (str.endsWith("ing")) {
        return str + "ly";
    } 
    return str + "ing";
}

console.log(verbing("run"));      
