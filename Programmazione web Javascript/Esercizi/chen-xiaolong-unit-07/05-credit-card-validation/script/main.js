/**
 * @file Main game file for Hangman game
 * @author Chen Xiaolong
 */
function validateCreditCard (cardNumber){
  //1. check of the lenght of the credic card is exactly 16
  console.log("===============================================================================");
  const cleaned = cardNumber.split('-').join('');
  if(cleaned.length>16 || cleaned.length<16){
    return { valid: false, number: cleaned, error: 'wrong_length' };
  }
  // 3. Check if every character is a digit between 0 and 9
  for (let i = 0; i < cleaned.length; i++) {
    let c = cleaned[i];
    if (c < '0' || c > '9') {
      return { valid: false, number: cleaned, error: 'invalid_character' };
    }
  }
  //2. check if appear al least 2 different number
  let flag=true;
  for(let i=1;i<cleaned.length;i++){
    if(cleaned[0]!=cleaned[i]){
      flag=false;
      break;
    }
  }
  if(flag){
    return { valid: false, number: cleaned, error: 'all_the_numbers_are_the_same' };
  }
  //3. check if the last digit is even
  let lastDigit = parseInt(cleaned[cleaned.length - 1]);
  if(lastDigit%2!=0){
    return { valid: false, number: cleaned, error: 'last_digit_not_even' };
  }
  //4. check if the sum is greater than 16
  let sum = 0;
  for (let i = 0; i < cleaned.length; i++) {
    sum += parseInt(cleaned[i]);
  }
  if(sum<=16){
    return { valid: false, number: cleaned, error: 'wrong_sum' };
  }
  return { valid: true, number: cleaned }
} 
console.log(validateCreditCard('9999-9999-8888-0000'));
console.log(validateCreditCard('4444-4444-4444-4444'));





