

const {readFile, writeFile} = require('fs');
// es lo mismo que si pusieramos 
// const fs = require('fs');
// fs.readFile

readFile('./content/first.txt', 'utf-8',(err, result)=> { // si no ponemos el "utf-8" aparecen numeros raros
    if(err){
        console.log("Error");
    }
    // console.log(result);
    const first = result;
    readFile('./content/second.txt', 'utf-8', (err, result)=>{
        if(err){
            console.log("Error");
        }

        const second = result;
        readFile('./content/third.txt','utf-8', (err, result)=>{
            if(err){
                console.log("Error");
            }

            const third = result;
            writeFile('./content/fourth-async.txt',`Here is the result : ${first}, ${second}, ${third}`, ()=>{
                if(err){
                    console.log("Error");
                }
                console.log(result);
            } );;
        });
    });
});