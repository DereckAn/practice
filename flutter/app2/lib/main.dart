import 'package:app2/widgets/user_transactions.dart';
import 'package:flutter/material.dart';



void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {

  // late String titleInput;  Estas variables son de una manera de caputar el input.
  // late String amounInput;

  

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Flutter app"),
      ),
      body: Column(
        // mainAxisAlignment: MainAxisAlignment.spaceBetween,
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: <Widget>[
          Card(
            color: Colors
                .yellowAccent, // para cambiar el tamaño del texto necesitamos romper las dependencias que el texto tiene con el papa y el papa del hijo. Para eso usaremos un container.
            elevation: 5,
            child: Container(
                width: double.infinity,
                child: const Text(
                    "Chart")), // Eleevation es para de tenga el efecto visial como de que un boton esta sobresaliendo.
          ),
          const UserTransaction(),
          const Card(
            color: Colors.red,
            child: Text("List of Tx"),
          )
        ],
      ),
    );
  }
}
