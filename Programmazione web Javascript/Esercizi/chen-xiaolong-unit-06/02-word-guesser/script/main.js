/**
 * @file Main game file for Hangman game
 * @author Chen Xiaolong
 */

/**
 * Array of possible words for the game
 * @type {string[]}
 */
let words = ["elephant", "treasure", "mountain", "umbrella", "painting", "solution", "computer", "vacation", "sandwich", "language"];
let word=words[Math.floor(Math.random() * words.length)];
let guessWord=[];
for(let i=0;i<word.length;i++)
    guessWord.push("_")
let maxAttempt=0;
let triedLetter=[];
let draw=[
`
    +----+
    |    O
    |
    |
    |
    |
=========
`,
`
    +----+
    |    O
    |    |
    |
    |
    |
=========
`,
`
    +----+
    |    O
    |    |\\
    |
    |
    |
=========
`,
`
    +----+
    |    O
    |   /|\\
    |
    |
    |
=========
`,
`
    +----+
    |    O
    |   /|\\
    |   /
    |
    |
=========
`,
`
    +----+
    |    O
    |   /|\\
    |   / \\
    |
    |
=========
`
]
function guessLetter(letter){
    let flag=false;
    if(maxAttempt==6){
        console.log(`You lose the game the word was ${word}`);
        return;
    }
    if (triedLetter.includes(letter)) {
        console.log(`You already tried '${letter}'. Try a different letter.`);
        return;
    }
    for(let i=0;i<word.length;i++){
        if(word[i].toUpperCase()==letter.toUpperCase()){
            guessWord[i]=word[i];
            flag=true;
        }
    }
    if(flag){
        console.log(`You guessed the letter ${letter}`);
        console.log(`Attempt left: ${6-maxAttempt}`);
        console.log(guessWord.join(' ')) ;
        triedLetter.push(letter); 
        }
    if(flag==false){
        console.log(draw[maxAttempt]);
        console.log(`Letter ${letter} wrong`);
        maxAttempt++;
        console.log(`Attempt left: ${6-maxAttempt}`);
        console.log(guessWord.join(' '))  
    }
    if(maxAttempt==6){
        console.log(`You lose the game the word was ${word}`);
        return;
    }

    if(guessWord.includes("_")==false){
        console.log(`You win the game`);
        return;
    }
}

guessLetter('a');
guessLetter('b');
guessLetter('c');
guessLetter('d');
guessLetter('e');
guessLetter('f');
guessLetter('g');
guessLetter('h');
guessLetter('i');


