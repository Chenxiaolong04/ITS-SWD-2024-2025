/**
 * @file main.js
 * @author Chen Xiaolong
 */

/**
 * Validates a credit card number based on various criteria.
 * The validation checks the following:
 * 1. The card number length is exactly 16 characters (excluding dashes).
 * 2. The card number contains only digits.
 * 3. The card number does not consist of the same digit repeated.
 * 4. The last digit of the card number is even.
 * 5. The sum of the digits is greater than 16.
 * 
 * Additionally, the result is printed in a formatted style using padEnd.
 * 
 * @param {string} cardNumber - The credit card number in string format (with or without dashes).
 * @returns {Object} An object containing the validation result:
 * - `valid`: A boolean indicating whether the card number is valid or not.
 * - `number`: The original input card number (including dashes).
 * - `error`: A string representing the error type if the card is invalid, or an empty string if valid.
 */
function validateCreditCard(cardNumber) {
  let cleaned = cardNumber.split('-').join('');
  let result = {
    number: cardNumber,
    valid: true,
    error: ''
  };

  // 1. Check if the length is exactly 16
  if (cleaned.length !== 16) {
    result.valid = false;
    result.error = 'wrong_length';
  }

  // 2. Check that all characters are digits
  if (result.valid) {
    for (let i = 0; i < cleaned.length; i++) {
      let c = cleaned[i];
      if (c < '0' || c > '9') {
        result.valid = false;
        result.error = 'invalid_character';
        break;
      }
    }
  }

  // 3. Check for at least two different digits
  if (result.valid) {
    let allSame = true;
    for (let i = 1; i < cleaned.length; i++) {
      if (cleaned[i] !== cleaned[0]) {
        allSame = false;
        break;
      }
    }
    if (allSame) {
      result.valid = false;
      result.error = 'all_the_numbers_are_the_same';
    }
  }

  // 4. Check if the last digit is even
  if (result.valid) {
    let lastDigit = parseInt(cleaned[cleaned.length - 1]);
    if (lastDigit % 2 !== 0) {
      result.valid = false;
      result.error = 'last_digit_not_even';
    }
  }

  // 5. Check if the sum is greater than 16
  if (result.valid) {
    let sum = 0;
    for (let i = 0; i < cleaned.length; i++) {
      sum += parseInt(cleaned[i]);
    }
    if (sum <= 16) {
      result.valid = false;
      result.error = 'wrong_sum';
    }
  }

  // Formatted output
  let line = '='.repeat(33);
  console.log(line);
  console.log(`= number : ${cardNumber.padEnd(20)} =`);
  console.log(`= valid : ${String(result.valid).padEnd(21)} =`);
  console.log(`= error : ${result.error.padEnd(21)} =`);
  console.log(line);

  return result;
}

// Esempio d'uso
let res1 = validateCreditCard('9999-9999-8888-0000');
let res2 = validateCreditCard('a923-3211-9c01-1112');
