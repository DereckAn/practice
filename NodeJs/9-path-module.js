const path = require("path");
console.log(path.sep) // --> esto devolvera el symbolo de que separa los documentos. 

const filepath = path.join('/content','subfolder','text.txt');
console.log(filepath) // --> esto devolvera la direccion del texto que guardamos

const base = path.basename(filepath);
console.log(base) // --> Este etodo regresa el ultimo archivo de la direcion. 

const absolute = path.resolve(__dirname, 'content' ,' subfolder', 'text.txt');
console.log(absolute); // --> esto te dara la direccion completa del documento que quieras