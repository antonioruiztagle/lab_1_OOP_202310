//Funcion isEven que recibe un numero y retorna true si el numero es impar

// function isEven(numero){
//     return numero % 2 !== 0;

// }

// console.log(isEven(3));


const isEven = number => number  % 2 === 0;

console.log(isEven(2));
console.log(isEven(3));


const isOdd = number => number % 2 !== 0;

console.log(isOdd(2));
console.log(isOdd(3));


//una forma de escribir la funcion
/*const evenNumbers = numbers => {
    return numbers.filter(number => isEven(number));
}*/
//otra forma de escribir la funcion
const evenNumbers = numbers => numbers.filter(isEven);
const oddNumbers = numbers => numbers.filter(isOdd);
const sqrtNumbers = numbers => numbers.map(number => number ** 2);
numberArray = [1,2,3,4,5,6,7,8,9,10];
console.log(evenNumbers(numberArray));
//console.log(numberArray);
console.log(oddNumbers(numberArray));
console.log(sqrtNumbers(numberArray));









