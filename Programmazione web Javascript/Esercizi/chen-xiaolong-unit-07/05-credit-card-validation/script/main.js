/**
 * @file main.js
 * @author Chen Xiaolong
 */

/**
 * Validates a credit card number based on various criteria.
 * The validation checks the following:
 * 1. The card number length is exactly 16 characters.
 * 2. The card number contains only digits.
 * 3. The card number does not consist of the same digit repeated.
 * 4. The last digit of the card number is even.
 * 5. The sum of the digits is greater than 16.
 * 
 * @param {string} cardNumber - The credit card number in string format.
 * @returns {Object} An object containing the validation result:
 * - `valid`: A boolean indicating whether the card number is valid or not.
 * - `number`: The cleaned credit card number without dashes.
 * - `error`: A string representing the error type if the card is invalid, or an empty string if valid.
 */
function validateCreditCard(cardNumber) {
  // 1. Check if the length of the credit card number is exactly 16.
  console.log("===============================================================================");
  const cleaned = cardNumber.split('-').join('');
  
  if (cleaned.length > 16 || cleaned.length < 16) {
    return { valid: false, number: cleaned, error: 'wrong_length' };
  }
  
  // 2. Check if every character is a digit between 0 and 9.
  for (let i = 0; i < cleaned.length; i++) {
    let c = cleaned[i];
    if (c < '0' || c > '9') {
      return { valid: false, number: cleaned, error: 'invalid_character' };
    }
  }
  
  // 3. Check if at least 2 different numbers appear.
  let flag = true;
  for (let i = 1; i < cleaned.length; i++) {
    if (cleaned[0] != cleaned[i]) {
      flag = false;
      break;
    }
  }
  if (flag) {
    return { valid: false, number: cleaned, error: 'all_the_numbers_are_the_same' };
  }
  
  // 4. Check if the last digit is even.
  let lastDigit = parseInt(cleaned[cleaned.length - 1]);
  if (lastDigit % 2 != 0) {
    return { valid: false, number: cleaned, error: 'last_digit_not_even' };
  }
  
  // 5. Check if the sum of the digits is greater than 16.
  let sum = 0;
  for (let i = 0; i < cleaned.length; i++) {
    sum += parseInt(cleaned[i]);
  }
  
  if (sum <= 16) {
    return { valid: false, number: cleaned, error: 'wrong_sum' };
  }
  
  // If all checks pass, return valid.
  return { valid: true, number: cleaned };
} 

console.log(validateCreditCard('9999-9999-8888-0000'));
console.log(validateCreditCard('4444-4444-4444-4444'));
