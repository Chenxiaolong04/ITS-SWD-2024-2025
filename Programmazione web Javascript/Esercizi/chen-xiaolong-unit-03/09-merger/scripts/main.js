function merger(num1,num2){
    if(typeof(num1)=="number"&&typeof(num2)=="number")
        return num1+num2;
    else if(typeof(num1)=="string"&&typeof(num2)=="string")
        return num1+num2;
    else 
        return null;
}
result=merger("1","2");
console.log(result)