const str = "Abracadabra";
const arr = [...str];
arr.splice(3, 1, "X"); 
const result = arr.join('');

console.log(result); 