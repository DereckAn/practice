import 'package:flutter/material.dart';

class SecondPage extends StatefulWidget {
  const SecondPage({super.key});
  // final String name;

  @override
  State<SecondPage> createState() => _SecondPageState();
}

class _SecondPageState extends State<SecondPage> {
  @override
  Widget build(BuildContext context) {
    // SecondPageArguments arguments = ModalRoute.of(context).settings.arguments;
    return Scaffold(
      appBar: AppBar(
        title: Text("Sedunga pantalla"),
      ),
      body: Center(
        child: Text("hola a la pagina dos"),
      ),
    );
  }
}

// class SecondPageArguments {
//   String name;
//   String lastName;
//   SecondPageArguments({String name, String lastName});
// }
