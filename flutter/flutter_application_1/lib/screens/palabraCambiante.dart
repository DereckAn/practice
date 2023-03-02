import 'package:flutter/material.dart';

class CambioPalabra extends StatefulWidget {
  const CambioPalabra({super.key});

  @override
  State<CambioPalabra> createState() => _CambioPalabraState();
}

class _CambioPalabraState extends State<CambioPalabra> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ListView(
        children: [
          Container(
            color: Colors.amber,
            width: 50,
            height: 50,
          ),
          Container(
            color: Color.fromARGB(255, 32, 143, 111),
            width: 50,
            height: 50,
          ),
        ],
      ),
    );
  }
}
