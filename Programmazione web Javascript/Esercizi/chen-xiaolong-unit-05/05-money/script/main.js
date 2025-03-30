function money(number) {
    if(typeof number !== 'number') {
        return 'Please enter a number';
    }
    if(number < 0) {
        return 'Please enter a positive number';
    }
    if(number == 0) {
        return 'You have no money';
    }
    if(number ==1000000)
        return `${number} dollars :)`+` = ${number*0.93} euros`;
    else
        return `${number} dollars`+` = ${number*0.93} euros`;
}        
let result=money(132); 
console.log(result); 