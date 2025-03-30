/**
 * @param {string} str 
 * @returns {string} 
 */
function notBad(str) {
    let notIndex = str.indexOf('not');
    let badIndex = str.indexOf('bad');
    if (notIndex<badIndex) {
        console.log(notIndex, badIndex);
        return str.slice(0, notIndex) + 'good' + str.slice(badIndex + 3);
    }
    return str;
}
console.log(notBad('This dinner is not that bad!'));
