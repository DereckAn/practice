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

const http = require('http');
const server = http.createServer((req, res) => {
    console.log(req.url);
    if(req.url === '/'){
        res.end('Welcom to our home page');
    }

    if(req.url === '/about'){
        res.end('You are in the about page');
    }
    // res.write('Welcom to our home page');
    res.end(
   `<h1> Oops The Address does not exists</h1>
    <p>Hola perros, me duele el cuerpo. </p>
    <a href="https://www.youtube.com/">Youtube</a>`
    );
});

server.listen(5000);