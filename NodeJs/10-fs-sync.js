
const {readFileSync, writeFileSync} = require('fs');
// es lo mismo que si pusieramos 
// const fs = require('fs');
// fs.readFileSync

const first = readFileSync('./content/first.txt','utf-8');
const second = readFileSync('./content/second.txt','utf-8');
const third = readFileSync('./content/third.txt','utf-8');

// Esto codigo creara otro file juntando first, second , third. Y si no esta el docmuento lo creara. 
 // El segundo parametro sera la primera linea en el nuevo documento. 
 // El tercer parametro es para escribir dos veces el texto. Es para override lo que esta escrito 
writeFileSync('./content/fuccion-sync.txt', `Here is the result : ${first}, ${second}, ${third}`, {flag:'a'}); 

console.log(first, second, third)