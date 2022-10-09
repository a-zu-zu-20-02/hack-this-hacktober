/**
 * Given a List of numbers and a  number k, return whether any two numbers from list will add up to k
 * Eg; for array [10,15,3,7] and k of 17, return true since 10+7=17
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
const input_number = Number(prompt("Input the number: "));
console.log("-----------------------------------------------");
console.log("Given Array: ", input_array);
console.log("Given Number: ", input_number);
console.log("-----------------------------------------------");
// Using two passes
// const checkSum = (input_array, input_number) => {
//    // check for single element array
//     if (input_array.length === 1) {
//         return input_array[0] === input_number;
//     }
//     //When we use two loops the first loop loops through all the numbers in array
//     for (let i = 0; i < input_array.length; i++) {
//      // The second loop will loop through higher index in array
//         for (let j = i + 1; j < input_array.length; j++) {
//      // Check if sum of the numbers equal to the given input number
//             if (input_array[i] + input_array[j] === input_number) {
//                 return true;
//             }
//         }
//     }
//     return false;
// }



// without using two loops
const checkSum = (input_array, input_number) => {
    // if array consists of a single element check if the input number is the number in array
    if (input_array.length === 1) {
        return input_array[0] == input_number;
    }
    // default answer will be false
    let answer = false;
    // loop through each elements of the array
    input_array.forEach(number => {
        // if the number is less than the input number then find its corresponding pair whose sum equals input number
        if (number < input_number) {
            let secondNumber = input_number - number;
            // check if the second number is present in array or not. If yes change default answer to yes
            if (input_array.includes(secondNumber)) {
                //! return deoesn't work inside foreach loops as array#foreach simply doesn't care for the return value of its worker function. It will simply execute the loop for each worker element
                // return true;
                answer = true;
            }
        }
    });
    return answer;
}

console.log('Result: ',checkSum(input_array, input_number));