function mixUp(str1, str2) {
    let firstPart1 = str1.slice(0, 2);
    let firstPart2 = str2.slice(0, 2);

    let lastPest1 = str1.slice(2);
    let lastPart2 = str2.slice(2);

    return firstPart2 + lastPest1 + " " + firstPart1 + lastPart2;
}

console.log(mixUp("hello", "world")); 
   
