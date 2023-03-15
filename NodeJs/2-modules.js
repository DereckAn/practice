const names = require("./4-names"); //esto es para importar el archivo 4-names.js
const sayHello = require("./5-utils"); //esto es para importar el archivo 5-utils.js
const people = require("./6-alternative"); 
require("./7-mind-granade") // otra manera de importar un documento. De esta manera importaremos todo el docuemnto. 
console.log(names);

console.log(people)

sayHello("Dereck");
sayHello(names.pedro);
sayHello(names.juan);