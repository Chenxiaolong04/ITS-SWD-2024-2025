/**
 * @param {string} str1 - The main string.
 * @param {string} str2 - The substring to search for.
 * @returns {boolean} - True if str1 contains str2, false otherwise.
 */
function aContainsb(str1, str2) {
    return str1.includes(str2);
}
console.log(aContainsb("Another hello world", "hell"));