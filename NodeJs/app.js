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



// nom i <packagename>  esto es para installar  paquetes de npm

// global dependency  - use it in any project 
// npm install -g <packagename>
//sudo npm install -g <packagename>  (mac, linux)

// package.json - manifest file (store important info about project/package)
// manual approach (create package.json in the root, create properties etc)
// npm init (step by step, press ener to skip)
// npm init -y (everything default)

//------------------------------------------  Este es un ejemplo de las cosas asyncoronas 
// const http = require("http");

// const server = http.createServer((req, res) => {
//     if(req.url === "/"){
//         res.end("home page");
//     } else if(req.url === "/about"){
        
//         for(let i = 0; i<100; i++){
//             for(let j = 0; j<100; j++){
//                 console.log(`${i} ${j}`)
//             }
//         }
//         res.end("<h1>About</h1>");
//     } else {
//         res.end("<h1>Page not found</h1>");
//     }
// })

// server.listen(5000, () => {
//     console.log("Server running on port 5000");
// });

//-------------------------------  Aqui estamos usando promesas

const {readFile} = require("fs");

const getText = (path) => {
    return new Promise((resolve, reject) => {
        readFile(path, "utf-8", (err, data) => {
            if(err){
                reject(err);
            } else{
                resolve(data);
            }
        })
    })
}

getText(`./content/first.txt`).then(result => console.log(result)).catch(err => console.log(err));