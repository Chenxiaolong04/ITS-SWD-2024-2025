/**
 * @file Main game file for Hangman game
 * @author Chen Xiaolong
 */
function cashRegister (cart){
  let sumCart=0;
  arrayCart=Object.values(cart)
  for(let i=0;i<arrayCart.length;i++){
    sumCart+=parseFloat(arrayCart[i]);
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

