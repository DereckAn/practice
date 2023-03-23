
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