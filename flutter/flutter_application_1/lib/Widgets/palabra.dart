import 'package:flutter/material.dart';
// import 'package:english_words/english_words.dart';

class Palabra extends StatelessWidget {
  // const Palabra({super.key});
  final String pala;

  const Palabra(this.pala);

  @override
  Widget build(BuildContext context) {
    return Card(
      color: const Color.fromARGB(221, 70, 183, 42),
      child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Text(
            pala,
            style: const TextStyle(
                fontSize: 100, color: Color.fromARGB(173, 255, 255, 255)),
          )),
    );
  }
}
