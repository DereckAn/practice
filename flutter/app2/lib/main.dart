import 'package:flutter/material.dart';
import './transaction.dart';

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
  final List<Transaction> transactions = [
    Transaction(id: '01', title: "Water", amount: 10.00, date: DateTime.now()),
    Transaction(id: '02', title: "Coca", amount: 15.36, date: DateTime.now()),
  ]; //Aqui estamos haciendo una lista de transacciones.

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Flutter app"),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
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
          Column(
            children: transactions.map((tx) {
              return Card(
                child: Row(
                  children: [
                    Container(
                      width: 60,
                      height: 60,
                      color: Colors.amber,
                      child:Text(tx.amount.toString())
                    ),
                    Column(children: [
                      Text(tx.id),
                      Text(tx.title),
                      Text(tx.date.toString())
                    ])
                  ],
                ),
              );
            }).toList(),
          ), // Aqui estamos generando los widgets que vayamos a necesitar. Con un map.
          const Card(
            color: Colors.red,
            child: Text("List of Tx"),
          )
        ],
      ),
    );
  }
}
