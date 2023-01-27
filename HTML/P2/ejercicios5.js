let materias = {
    fisica:[95,6,3], 
    matematicas: [75,8,2],
    quimica:[80,8,4],
    logica:[45,5,3],
    algebra: [69,6,3],
    programacion: [96,9,2],
    bbdd: [70,9,1],
    calculo: [100,10,4]
}

const asistencia = ()=>{
    for (materia in materias){
        let asssitencias = materias[materia][0];
        let promedio = materias[materia][1];
        let trabajos = materias[materia][2];
        
        console.log(` ${materia}`);

        if (asssitencias >= 90){
            console.log(`%c   Asistencias en orden`, `color: green`);            
        } else {
            console.log(`%c   Falta de asistencias `, `color: red`);            
        }

        if (promedio >= 7){
            console.log(`%c   Promedio en orden`, `color: green`);
        } else {
            console.log(`%c   Promedio reprovado `, `color: red`);
        }

        if (trabajos >= 3){
            console.log(`%c   Trabajos practicos en orden`, `color: green`);
        } else{
            console.log(`%c   Faltantrabajos practicos `, `color: red`);
        }
    }
}

asistencia();


let trabajo = "240 minutos de trabajo";
let stuio = "100 minutos de estudio";
let tp = " 100 minutos de trabajos practicos";
let homework = "30 minutos de cosas de la casa";
let descanso = "10 minutos de descanso";

console.log("TAREAS");
for (i = 0; i <= 14; i++){
    if (i == 0){
        console.groupCollapsed("Semana 1");
    }
    if (i == 7){
        console.groupEnd();
        console.groupCollapsed("Semana 2");
    }
    console.groupCollapsed("Dia" + (1 + i));
    console.log(trabajo);
    console.log(descanso);
    console.log(stuio);
    console.log(tp);
    console.log(homework);
    console.groupEnd();
}

console.groupEnd();


// let parrafo = "Hola soy dereck ";
// document.write(parrafo);


// parrafo  = document.getElementById("parrafo");
// elementsbytag = document.getElementsByTagName("p");
// queryselector = document.querySelector(".rancio");
// document.write(queryselector);

document.write("holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa");

document.addEventListener("DOMContentLoaded", function(event) {
    const titulo = document.querySelector(".titulo");
    const hola = document.querySelector(".hola");

    hola.setAttribute("type", "color");
    titulo.setAttribute("contentEditable", "true");
    titulo.setAttribute("dir", "rtl"); // para cambiar de direccion el texto, tambien lopodemos hacer con css
    titulo.setAttribute("hidden", "true"); // Para oculatar el elemento.  no importa si esta false o true mientras tenga este atributo se cultaigual 
    titulo.setAttribute("tabindex", "0"); // esto nos permite seleccionar
    titulo.setAttribute("title", "jajajajaj xd"); // cuando tengamos el mouse sobre el elemento nos saldra jajaaj xd
        titulo.setAttribute("title", "hola"); // esto nos permite seleccionar

});





