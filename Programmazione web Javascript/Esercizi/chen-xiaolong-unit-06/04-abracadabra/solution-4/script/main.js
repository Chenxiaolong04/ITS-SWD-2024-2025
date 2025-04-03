/**
 * @file: main.js
 * @author: Chen Xiaolong 
 */
const str = "Abracadabra";
const result = [...str];
result[3] = "X";
console.log(result.join("")); 