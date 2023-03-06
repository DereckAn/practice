import 'package:flutter/material.dart';
import '../Widgets/palabra.dart';

class CambioPalabra extends StatefulWidget {
  const CambioPalabra({super.key});

  @override
  State<CambioPalabra> createState() => _CambioPalabraState();
}

class _CambioPalabraState extends State<CambioPalabra> {
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
              const Palabra(),
              const SizedBox(height: 10),
              ElevatedButton(
                  style: ButtonStyle(
                    backgroundColor: MaterialStateProperty.all(
                        const Color.fromARGB(255, 25, 63, 95)),
                  ),
                  onPressed: () {
                    print("hola princesa");
                  },
                  child: const Text("Next")),
            ],
          ),
        ));
  }
}
