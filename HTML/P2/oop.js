class Animal{

    constructor(especie, edad, color){
        this.especie = especie;
        this.edad = edad;
        this.color = color;
        this.info = `Soy ${this.especie}, tengo ${this.edad} años y soy de color ${this.color}`;
    }

    verInfo(){ // Las funciones flecha no pueden ser usadas para crear metodos. 
        document.write(this.info + `<br>`);
    }


}

class Perro extends Animal{  // Creando otra clase. 
    constructor(especie,edad, color, raza){
        super(especie,edad,color);
        this.raza = raza;
    }

    ladrar(){
        document.write("wowow");
    }

}





// ------------------------------------------------------------------------- Este es un ejercicio -----------------------------------------------------

class Celulares{
    constructor(color, peso, rdp, rdc, ram){
        this.color = color;
        this.peso = peso;
        this.rdp = rdp;
        this.rdc = rdc;
        this.ram = ram;
        this.on = false;
    }

    prender(){
        if(this.on == false){
            alert("Celular prendido");
            this.on = true;
        } else {
            alert("El celular apagado");
            this.on = false;

        }
    }

    reiniciar(){
        if(this.on == true){
            alert("Celular reiniciando");
        } else {
            alert("El celular no esta encendido");
        }
    }

    fotos(){
        alert(`Foto tomada con una resolucionb de ${this.rdp}`);
    }

    video(){
        alert(`El video en ${this.rdc}`);
    }

    mostrarInfo(){
        return `Color: <b>${this.color}</b><br>
        Peso: <b>${this.peso}</b><br>
        Ram: <b>${this.ram}</b><br>
        Resolucion de Camara: <b>${this.rdc}</b><br>
        Resolucion de Video: <b>${this.rdp}</b><br>`;
    }
}


class CelularAltaGama extends Celulares{
    constructor(color, peso, rdp, rdc, ram, rdce){
        super(color, peso, rdp, rdc, ram);
        this.rdce = rdce;
    }
    
    lento(){
        alert("Estas grabando en video lento");
    }

    reconFacial(){
        alert("Te estoy analizando la jeta");
    }
    info(){
        return this.mostrarInfo() + `Resolucion de camara extra ${this.rdce}`;
    }

}

















celular1 = new CelularAltaGama("rojo", "150g", "1080", "12 mega pixeles", "8 Gb",  "4k");
celular2 = new Celulares("azul", "200g", "4k", "10 mega pixeles", "4 Gb");
celular3 = new Celulares("verde", "300g", "2k", "8 mega pixeles", "6 Gb");

// celular1.prender();
// celular1.fotos();
// celular1.video();
// celular1.reiniciar();
// celular1.prender();

// celilar1.mostrarInfo(); Asi no lo muestra porque solo pusimos un return pero no se muestra nada en la pantalla porque no hay ningun alert of document.write. 
// celilar2.mostrarInfo();
// celilar3.mostrarInfo();


document.write(`${celular1.info()}<br><br>${celular2.mostrarInfo()}<br><br>${celular3.mostrarInfo()}<br><br>`);













let perroa = new Perro("perro", 10, "verde", "pug");
let avestruz = new Animal("Avestruz", 5, "gris");
let tiburon = new Animal("tiburon", 7, "azul");

// document.write(perro); // [object Object]
// document.write(perro.color+ `<br>`) //verde

// document.write(perro.info + `<br>`);
// document.write(avestruz.info + `<br>`);
// document.write(tiburon.info + `<br>`);

perroa.verInfo();
avestruz.verInfo();
tiburon.verInfo();
perroa.ladrar();

console.log(perroa);  // click derecho  e inspecionar. 