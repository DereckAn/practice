import 'package:flutter/material.dart';

class Palabra extends StatelessWidget {
  const Palabra({super.key});

  @override
  Widget build(BuildContext context) {
    return const Card(
      color: Color.fromARGB(221, 70, 183, 42),
      child: Padding(
        padding: EdgeInsets.all(8.0), 
        child: Text("hola", style: TextStyle(fontSize: 100),)),
    );
  }
}
