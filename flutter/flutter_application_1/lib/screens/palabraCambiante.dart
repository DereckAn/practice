import 'package:english_words/english_words.dart';
import 'package:flutter/material.dart';
import '../Widgets/palabra.dart';

class CambioPalabra extends StatefulWidget {
  const CambioPalabra({super.key});

  @override
  State<CambioPalabra> createState() => _CambioPalabraState();
}

class _CambioPalabraState extends State<CambioPalabra> {
  // var current = WordPair.random();
  // String _textocambiar = "Hola";
  late WordPair _currentWord = WordPair
      .random(); // Esta linea de codigo sirve para que la variable tenga una palabra aleatoria.

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: const Color.fromARGB(210, 0, 0, 0),
        appBar: AppBar(),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                color: Colors.amber,
                width: 50,
                height: 50,
              ),
              // const Center(child: Text("hola perro")),
              Palabra(_currentWord
                  .asPascalCase), //  Esta linea es para que mande la palabra aleaotria al objeto creado. En este caso palabra.
              const SizedBox(height: 10),
              ElevatedButton(
                  style: ButtonStyle(
                    backgroundColor: MaterialStateProperty.all(
                        const Color.fromARGB(255, 25, 63, 95)),
                  ),
                  onPressed: () {
                    setState(() {
                      _currentWord =
                          WordPair.random(); // Aqui estamos creando una pa;abra nueva cada vez que se apriete el boton. 
                    });
                    print("hola princesa");
                  },
                  child: const Text("Next")),
            ],
          ),
        ));
  }
}
