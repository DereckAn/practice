const http = require('http');

const server = http.createServer((req, res) => {
    console.log('request even');
    res.end('Hello World');
})

server.listen(5000, () => {
    console.log('Server running on port 5000');
})