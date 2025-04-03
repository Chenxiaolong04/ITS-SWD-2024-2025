/**
 * @file: main.js
 * @author: Chen Xiaolong 
 */
let word=['S','M','A','R','T','P','H','O','N','E'];
let guessWord=['_','_','_','_','_','_','_','_','_','_'];
let maxAttempt=6;
let triedLetter=[];

function guessLetter(letter){
    let flag=false;

    if(maxAttempt==0){
        console.log(`You lose the game`);
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
    if(flag==true){
        console.log(`You guessed the letter ${letter}`);
        console.log(`Attempt left: ${maxAttempt}`);
        console.log(guessWord.join(' '))  
        }
    if(flag==false){
        console.log(`Letter ${letter} wrong`);
        maxAttempt--;
        console.log(`Attempt left: ${maxAttempt}`);
        console.log(guessWord.join(' '))  
    }


    if(guessWord.includes("_")==false){
        console.log(`You win the game`);
        return;
    }
}

guessLetter('s');
guessLetter('m');
guessLetter('m');
guessLetter('r');
guessLetter('t');
guessLetter('p');
guessLetter('h');
guessLetter('o');
guessLetter('n');
guessLetter('e');

