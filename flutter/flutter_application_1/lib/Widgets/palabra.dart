import 'package:flutter/material.dart';

class Palabra extends StatefulWidget {
// var current = WordPair.random();
  const Palabra({super.key});

  @override
  State<Palabra> createState() => _PalabraState();
}

class _PalabraState extends State<Palabra> {
  

  @override
  Widget build(BuildContext context) {

     
    return const Card(
      color: Color.fromARGB(221, 70, 183, 42),
      child: Padding(
          padding: EdgeInsets.all(8.0),
          child: Text(
            "hola",
            style: TextStyle(
                fontSize: 100, color: Color.fromARGB(173, 255, 255, 255)),
          )),
    );
  }
}
