const {readFileSync, readFile} = require("fs");

console.log("First task started");

readFile("../content/first.txt", "utf8", (err, result) => {
    if (err){
        console.log(err);
        return
    }
    console.log(result);
    console.log("Second task started");
})

console.log("Third task started");