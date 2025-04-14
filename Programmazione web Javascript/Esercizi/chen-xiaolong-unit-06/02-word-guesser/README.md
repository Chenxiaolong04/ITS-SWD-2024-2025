## 02-word-guesser
Autor: Chen Xiaolong  
Contact: xiao.chen@edu-its.it
___
### Exercise Requirements

Create two arrays:
○ one for the letters of the word (e.g. 'C', 'A', 'T')
○ Another for the current guessed letters (start with '_', '_', '_' and add the correct letters to it).
● Write a function called guessLetter that should:
○ Take one parameter, a letter.
○ Have a maximum number of guesses (e.g. 6)
○ Check if the letter is in the word array.
○ If the letter matches, add it in the correct position of the guessed array.
○ Show the user the current guessed letters.
○ Tell the user if they guessed a correct letter.
○ Tell the user how many guesses remain.
○ Tell the user if they won or lost the game.

### Approach to Solution

- Define the secret word as an array of characters.
- Create a placeholder array (`_`) for unguessed letters.
- Keep track of already tried letters.
- Implement the `guessLetter(letter)` function:
  - Check if the letter was already guessed.
  - Verify if it's in the word.
  - Update the game state (attempts, revealed letters).
  - Check for win or loss conditions.