/**
 * Day 2:Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
 */

// ? For taking input from terminal
// npm install prompt-sync
const prompt = require('prompt-sync')();
// input the max size, array and the input number from user
const max_size = prompt("Input Max Size Of Array: ");
const input_array = [];
console.log(`Input ${max_size} elements for array: `);
for (let i = 0; i < max_size; i++){
    input_array.push(Number(prompt(`Element ${i+1} : `)));
}
let new_array = [];

// normal c way
for (let i = 0; i < input_array.length; i++) {
    let tempProduct = 1;
    for (let j = 0; j < input_array.length; j++) { 
    if (i !== j) {
        tempProduct *= input_array[j];
    }
    }
    new_array[i] = tempProduct;
}

// using division way 
// let totalProduct = 1;
// input_array.forEach(number => {
//     totalProduct *= number;
// });

// for (let i = 0; i < input_array.length; i++){
//     new_array[i] = totalProduct / input_array[i];
// }


console.log(`Result = ${new_array}`);