string = "hola";
num = 3;
boolenao = false;

prompt("Te gusto, perro?"); //esta funcion es como un input o como un scanner 
document.write(num); //Esta funcion hace que se escriba el numero en el documento. 

saludo = "Hola Perro";
pregunta = "Como estas?";

numero1 = 5;
numero2  = 24;

nombre = "Dereck Angeles"

// Concatenacion

frase = "" + numero2 + numero1;  // Cundo detecta un string convierte todo, TODO a string. 
// frase = numero1.concat(numero2); Esta funcion es para juntar dos cadenas. Hace casi lo mismo que el metodo anterior pero solo funciona con strings. 
frase_final = `Mi nombre es ${nombre} y tengo ${numero2} años`  // Esto se parece a las f"{}" de python. Podemos escribir codigo html con esto mas facilmente.   

document.write(frase_final);


//   ==  compara si son iguales. No importa si son diferentes tipos de datos. 
//   === Compara si  son estrictamente iguales.   Deben de tener el mismo valor y el mismo tipo de datos(int, string, boolean) 


//camel case
// la primer letra de la priemr palabra es minisculo y la primer letra de la segunda palaras es mayuscula ex:      holaDereck();  holaDereckAngelesMartinez();

// condicionales  if, else, else if

// if(numero == 10){
//     alert("hola");
// }
//  else if (numero1 == 1) {
//     alert(numero1)
// }
// else{
//     alert(numero2)
// }


// '''---------------------------------------------------------------------------------------------------------'''
// dineroCo = prompt("Cuando dinero tienes Cofla?");
// dineroRo = prompt("Cuanto dinero tienes Roberto?");
// dineroPe = prompt("Cuanto dinero tienes Pedro?");

// dineroCo = parseInt(dineroCo);
// dineroPe = parseInt(dineroPe);
// dineroRo = parseInt(dineroRo);

// const definirCompra = (n)=>{
//     let din = prompt(`Dinero de ${n}`);
//     if (din >= 0.6 && din < 1) return (`${n}: helado de agua`);
//     if (din >= 1 && din < 1.6) return (`${n}: helado de crema`);
//     if (din >= 1.6 && din < 1.7) return (`${n}: helado de haldix`);
//     if (din >= 1.7 && din < 1.8) return (`${n}: helado de heladovich`);
//     if (din >= 1.8 && din < 2.9) return (`${n}: helado de helardo`);
//     if (din >= 2.9) return (`${n}: helado de confites o pote de 1/4 kg`);
//     else return (`${n}: No te alcanza para ningun helado pobre de mierda`)
// }

// console.log(definirCompra("Cofla"))
// console.log(definirCompra("Pedro"))
// console.log(definirCompra("Roberto"))


///'''------------------------------------------------------------------------------------------------------'''

// arrays

frutas = ["banana", "sandia", "peras", "naranjas"];

document.write(frutas);


// Arrays asociativos    -----  >  Esto es como los diccionarios en python. 
let pc = {
    nombre: "Dereck A",
    procesador: "ryzen 5950",
    ram: "32 gb",
    memory: "1 Tb"
}

document.write(pc["nombre"]);  // Tiene que ser con texto. 



// Do -- While    -- Se hace primero el "do" y luego se ejecutara el bucle while. 

do {  // Lo ejecuta una vez y si el while es falso no vuelve a ejecutarlo

    numero++
    document.write(numero + "<br>")
}

while(numero < 6 );


//  for 

for (i = 0; i > 0; i++){

    if (i == 12){
        continue;  //Esto es como un break. Solo que este si deja continuar el bucle for      --  No imprimira el numero 12 pero si todods los demas numeros
    }

    document.write(i + "<br>")
}



// for in 

let animales = ["perro", "gatos", "elefantes"]

for (animal in animales){  // nos devuelve la posicion 
    document.write(animel + "<br>")

}

for (animal of animales){  // nos devuelve los elementos de la lista
    document.write(animal + "<br>")
}




//label 

forRancio:
for (let array in arra2){
    if(array==2){

        for (let array of array1){
            document.write(array + "<br>");
            break forRancio;   // Esto es para acabar el bucle completo.   si el label solo acabariamos con el primero for. 
        }

    } else {
        document.write(array2[array] + "<br>");
    }
}


//funciones


function saludar(){
    respuesta = prompt("Hola dime uno o dos ");
    if (respuesta == "uno"){
        alert("hola 1");
    } else {
        alert("hola 2");
    }
}
saludar();


decirhola = function(){  //esta es otra manera de crear una funcion. 
    alert("Hola");
}
decirhola();



//fuciones flecha   => 


const decir = nombre=>{   // en lugar de escribir "function" solo ponemos una flecha     tiene muchisisismas funciones. 
    let frase = `Hola ${nombre}, Como has estado hoy?`;
    document.write(frase);
}

decir("Dereck");

const sal = (nombre, edad)=>{
    let frase = `Hola ${nombre}, Como has estado hoy?`;
    document.write(frase);
}


const salu = nombre => document.write(frase); // Esto es para resumir lo mas posible las funciones. 


/**-------------------------------------------------------------------------------------------------------------------------------------- ejercicios------------------------------------------------------------- */
// este es un ejkercicio 

let free = false;

const validarCliente = (time) => {
    let edad = prompt("Cual es tu edad?");
    if (edad >= 18){
        if (time >= 2 && time <  7 && free == false){
            alert("Pasas gratis papu")
            free = true;
        } else{
            alert("pasas pero pagas con culo papu")
        }
    } else {
        alert("No pasas papu");
    }
        
    
}


// segundo ejercicio 

let cantidad = prompt("cuantos alumnos hay?")
let alumnosTotales = []

for (i=0; i < cantidad; i++){
    alumnosTotales[i] = [prompt("nombre del alumno:" + (i+1)), 0];
}

const asistencia = (nombre, p) => {
    let presencia = prompt(nombre);
    if (presencia == "p" || presencia == "P"){
        alumnosTotales[p][1]++;
    }
}

for (i = 0; i < 30; i++){
    for (alumn in alumnosTotales){
        asistencia(alumnosTotales[alumn][0], alumn);
    }
}

for (alumns in alumnosTotales){
    let resultado = `${alumnosTotales[alumns][0]}:<br>
    _______Assistencias: ${alumnosTotales[alumns][1]} <br>
    _______Ausencias: ${30 - parseInt(alumnosTotales[alumns][1])}`;
    if (30 - alumnosTotales[alumns][1] > 18){
        resultado += "Reprobado por inasistencias";
    } else {
        resultado +=  "<br><br>";
    } document.write(resultado);
}


// ejercicio 3

const sumar = (num1, num2)=>{
    return parseInt(num1)+parseInt(num2);
}

const restar = (num1, num2) => {
    return parseInt(num1) - parseInt(num2);
}

const multi = (num1, num2) => {
    return parseInt(num1) * parseInt(num2);
}

const dividir = (num1, num2) => {
    return parseInt(num1) / parseInt(num2);
}

let operacion = prompt("Que operacion deseas realizar.<br> 1) suma<br> 2) resta<br> 3) multiplicacion<br> 4) divicion.");

if (operacion == 1){
    let numero1 = prompt("Primer numero a sumar?");
    let numero2 = prompt("Segundo numero a sumar?");
    let resultado = suma(numero1, numero2);
    alert(`Tu resulatdop es: ${resultado}`)
}
else if (operacion == 2){
    let numero1 = prompt("Primer numero a restar?");
    let numero2 = prompt("Segundo numero a restar?");
    let resultado = resta(numero1, numero2);
    alert(`Tu resulatdop es: ${resultado}`)
}
else if (operacion == 3){
    let numero1 = prompt("Primer numero a multiplicar?");
    let numero2 = prompt("Segundo numero a multiplicar?");
    let resultado = multi(numero1, numero2);
    alert(`Tu resulatdop es: ${resultado}`)
}
else if (operacion == 4){
    let numero1 = prompt("Primer numero a dividir?");
    let numero2 = prompt("Segundo numero a dividr?");
    let resultado = dividir(numero1, numero2);
    alert(`Tu resulatdop es: ${resultado}`)
}
else{
    aler("No se ha encontrado la operacion deseado. ")
}



