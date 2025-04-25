/**
 * @file main.js
 * @author Chen Xiaolong
 */

/**
 * Calculates the total sum of the values in a shopping cart.
 * This function iterates through the cart and sums up the prices of all items.
 * 
 * @param {Object<string, string>} cart - An object representing a shopping cart where the keys are item names (strings)
 * and the values are their prices (strings).
 * 
 * @returns {void} This function prints the total sum of the cart items to the console.
 */
function cashRegister(cart) {
  let sumCart = 0;
  let arrayCart = Object.values(cart);

  for (let i = 0; i < arrayCart.length; i++) {
    sumCart += parseFloat(arrayCart[i]);
  }

  console.log(sumCart);
} 

let cartForParty = {
  banana: "1.25",
  handkerchief: ".99",
  Tshirt: "25.01",
  apple: "0.60",
  nalgene: "10.34",
  proteinShake: "22.36"
};

cashRegister(cartForParty);
