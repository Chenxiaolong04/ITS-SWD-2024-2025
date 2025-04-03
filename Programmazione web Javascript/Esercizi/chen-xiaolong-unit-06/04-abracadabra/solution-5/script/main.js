const str = "Abracadabra";
const arr = [...str];
arr[3] = "X"; 
const result = arr.join('');

console.log(result); 