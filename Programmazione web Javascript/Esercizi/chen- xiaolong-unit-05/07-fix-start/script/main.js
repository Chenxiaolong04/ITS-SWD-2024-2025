function fixStart(str) {
    let firstChar = str[0]; 
    let restOfString = str.slice(1); 

    let modifiedString = restOfString.replaceAll(firstChar, '*');

    return firstChar + modifiedString; 
}

console.log(fixStart("babble")); 

