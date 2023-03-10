//para correr el programa se debe de ejecutar el archivo app.js 
// y para eso tienes que entrar a la terminar y poner "node app.js"
//  "node {nombre de tu archivo}"

// console.log("Hello World");

// const amount = 12;
// if (amount<10){
//     console.log("Less than 10");
// } else {
//     console.log("Greater than 10");
// }

// console.log("It is my first node app");

// Global - No window

// __dirname - Path to current directory
// __filename - Path to current file
// require - Function to use module (CommonJS)
// module - info about current module (file)
// process - info about env where the program is being executed

// console.log(__dirname);
// console.log(__filename);

// setInterval(() => {
//     console.log("Hello World");
// }, 1000); // esto improme un hello world cada 1 segundo


// Modules - Encapsulated Code (only share minimum)
// CommonJs - every files is module (by default)

const names = require("./4-names"); //esto es para importar el archivo 4-names.js
const sayHello = require("./5-utils"); //esto es para importar el archivo 5-utils.js
const people = require("./6-alternative"); 
require("./7-mind-granade") // otra manera de importar un documento. De esta manera importaremos todo el docuemnto. 
console.log(names);

console.log(people)

sayHello("Dereck");
sayHello(names.pedro);
sayHello(names.juan);
