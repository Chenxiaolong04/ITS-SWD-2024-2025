/**
 * Description placeholder
 *
 * @param {string} language 
 * @returns {("Ciao, mondo" | "안녕하세요, 세계" | "こんにちは世界" | "Bonjour, le monde" | "你好世界")} 
 */
function helloWorld(language){
    switch(language){
        case "it":
            return "Ciao, mondo";
        case "kr":
            return "안녕하세요, 세계";
        case "jp":
            return "こんにちは世界";
        case "fr":
            return "Bonjour, le monde"
        case "ch":
            return "你好世界";
    }
}
console.log(helloWorld("it"))
console.log(helloWorld("kr"))
console.log(helloWorld("jp"))
console.log(helloWorld("fr"))
console.log(helloWorld("ch"))

