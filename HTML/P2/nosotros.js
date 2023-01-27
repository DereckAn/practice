let cadena = "cadena de prueba";
let cadena2 = "cadena";

resultado = cadena.concat(" Hola popo");  // Esto es para juntar las cadenas.    concat() junta dos cadenas y retorna una 
startwith = cadena.startsWith(cadena2);   // Empieza con lo que dice en la cadena 2  --> retorna valor booleano. 
endswith = cadena.endsWith(cadena2);   // Termina con lo que dice en la cadena 2 --> Retorna valor booleano.
includes = cadena.includes(cadena2); // si una cadena se encuentra dentro de otra   --> Retorna valor booleano.  --> busca una cadena dentro de otra.
indexof = cadena.indexOf(cadena2);   // Hace los mismo que includes() pero nos devuleve la posicion en la que se encuntra la primera letra de la cadena que estamos buscando. Si nos devuelve -1 es que la cadena no existe
lstindexof = cadena.lastIndexOf(cadena2); // si en una cadena se repiten varias veces la cadena que estamos buscando. Con este metodo sabremos donde comienza la ultima vez que se repite la cadena que desamos. 
padstart = cadena.padStart(5, '0');   // El primer numero indica cuantos son los caracteres desados y el segundo parametro representan los caracteres con los que quieres que se rellene la cadena. Los pone en el principio. 
padend = cadena.padEnd(5, '0');     // Hace lo mismo que padStart pero este rellena al final.  
repeat = cadena.repeat(4); // Esta son las veces que el metodo va a repetir la misma cadena 


split = cadena.split(' '); //Con este metodo separaremos la cadena cuando haya espacios. Nore regresara un array
substring = cadena.substring(0,5); // Aqui estsa creando otro string el primero numero se refiere a la posisionc donde empieza en nuevo string y el segundo nuemero es pa psicion donde termina.
tolowercase = cadena.toLocaleLowerCase(); //Convierte todo en minuscula
toupperscase = cadena.toLocaleUpperCase();  //Lo converite a mayuscula
tostring = cadena.toString(); //Convierte a string 
trim = cadena.trim(); //Elimina los espacios en blanco
trimend = cadena.trimEnd(); //Elimina los espacios del final 
trinstart = cadena.trimStart(); //Elimina los espacios despues del inicio



cadena.length = cadena.length; //esta propiedad nos da cuantos caracteres tiene la cadena
document.write(resultado);

// ----------------------- modificar un array-----------------

let nombre = ["dereck", "sadie", "jabir",, "joao"];

//metodods transformadores. 
pop = nombre.pop(); // saca el ultimo elemento del array y tet lo muestra en pantalla. 
shift = nombre.shift(); //Elimina el primer elemento del array y te lo muestra en pantalla.
push = nombre.push("Marcela", "Julio"); // Para agregar elementos a un array. Retorna la cantidad de elementos que contiene --> int
reverse = nombre.reverse(); // Invierte el ordern de los elementos en el array.
unshift = nombre.unshift(1, 3); // Desde la posicion 1 quiero poner 3 .   el primer numero posicion , segundo numero indica el elemento que pondremos
sort = nombre.sort(); // Ordena alfabeticamente o numericamente el array
splice = nombre.splice(1, 3, "roberto", "maximo"); //primer parametro es la pocision , Segundo parametyro es para decir cuantos elementos vamos a eliminar. Y agregara un tercerparametro si es que hay. 

//------ metodods accesores -----------------------
join = nombre.join(' - '); // Convierte a string el array y nos lo separa   ---> "dereck - sadie - jabir - joao"     --> nos separa por cosas
slice = nombre.slice(0,2); // Muestra desde el elemento 0 hasta el elemento 2.  Es lo mismo que --> substring()
include = nombre.include("dereck") // Chacara si en el array esta el elemento "dereck"  --> retornara un booleano. 

// ------------------ metodods de repeticion --------
filter = nombre.filter((nombre) => {  // Hace lo mismo que un forEach pero es mas completo 
    document.write(numero + "<br>")
}); // es un bucle y recive como parametro una funcion 

foreach = nombre.foreach("porner una funcion aqui");  // tenemos que estudiar esto. 

document.write(resultado);


// -------------------- Objerto Math -----------------------

numero = 25;

sqrt = Math.sqrt(numero); 
cbrt = Math.cbrt(25); //raiz cubica
max = Math.max(1,2,3,4,5,6,7,8,9); //Devuelve el numero mas grande
min = Math.min(1,2,3,4,45,56,7,8,9,0); // Devuelve el numero mas pequeño
random = Math.random(); // Sin parametros nos devuelve un numero entre 0 y 1 
round = Math.round(random); // Redondea el numero 
floor = Math.floor(random); // Redondea para abajo   4.8 --> 4 
trunc = Math.trunc(9.9); // Quita la parte fraccionaria Elimina los decimales


pi = Math.PI;
sqrt1_2 = Math.SQRT1_2; //La raiz cuadrada de un medio
sqrt2 = Math.SQRT2; //La raiz cuadrada de 2

e = Math.E; //Constrante de euler
ln2 = Math.LN2; // logaritmo natural de 2
ln10 = Math.LN10; 


// ------------------ console -----------------------


console.assert(5 > 3); // No se usa  // Aparece un error en la consola si la afirmacion es falsa. 
console.clear(); // La consola se limpia 
console.error("Que hiciste menso?"); //Para que tu puedas editar el mensaje de error
console.log("hola este es un mensaje de depuracion");
console.info("hola este es un mensaje de ionformacion");
console.table([1, 2, 3, 4, 5, 6, 7, 8, 9,]);
console.warn("mensaje de advertencia");
console.dir([5,4,2,45,1,23,4]); // despliega un array en forma de lista con los valores que estan dentro del parametro.

// funciones de conteo 
console.count(); // nos puede ayudar a saber cuantas veces se ejecuto una funcion. 
console.countReset(); // para reinicias el conteo. 

// funciones de tener 
console.time(); // inicia un temporizador
console.timeEnd(); // paramos el contador. 
console.timeLog(); // podemos ver el timepo que lleva activo el metodo time()

// funciones de agrupacion
console.group(); //Crea un grupo  aparece abierto
console.groupCollapsed(); // El grupo aparecera cerrado. 
console.groupEnd(); // Remueve un grupo en linea en el redistro de la consola web. 

console.log("%cHola", "color:green;background: yellow;padding:20px; border: 3px solid blue")