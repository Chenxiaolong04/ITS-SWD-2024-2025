/**
 * @file: main.js
 * @author: Chen Xiaolong 
 */
let word=['S','M','A','R','T','P','H','O','N','E'];
let guessWord=['_','_','_','_','_','_','_','_','_','_'];
let maxAttempt=6;
function guessLetter(letter){
    let flag=false;
    if(guessWord.includes("_")==false){
        console.log(`You win the game`);
        return;
    }
    for(let i=0;i<word.length;i++){
        if(word[i].toUpperCase()==letter.toUpperCase()){
            guessWord[i]=word[i];
            flag=true;
        }
    }
    if(flag==true){
        console.log(`You guessed the letter ${letter}`);
        console.log(`Attempt left: ${maxAttempt}`);
        console.log(guessWord)
    }
    if(flag==false){
        console.log(`Letter ${letter} wrong`);
        maxAttempt--;
        console.log(`Attempt left: ${maxAttempt}`);
        console.log(guessWord)
        if(maxAttempt==0){
            console.log(`You lose the game`);
        }
    }
    if(guessWord.includes("_")==false){
        console.log(`You win the game`);
        return;
    }
}

guessLetter('s');
guessLetter('m');
guessLetter('a');
guessLetter('r');
guessLetter('t');
guessLetter('p');
guessLetter('h');
guessLetter('o');
guessLetter('n');
guessLetter('e');
