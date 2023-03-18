import 'package:app2/widgets/new_transaction.dart';
// import 'package:app2/widgets/user_transactions.dart';
import 'package:flutter/material.dart';

import 'models/transaction.dart';
import 'widgets/transaction_list.dart';

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

class MyHomePage extends StatefulWidget {
  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  // late String titleInput;  Estas variables son de una manera de caputar el input.



   final List<Transaction> _transactions = [
    Transaction(id: '01', title: "Water", amount: 10.00, date: DateTime.now()),
    Transaction(id: '02', title: "Coca", amount: 15.36, date: DateTime.now()),
  ];

  void _addNewtransaction(String txTitle, double txAmount) {
    final newTx = Transaction(
        title: txTitle,
        amount: txAmount,
        date: DateTime.now(),
        id: DateTime.now().toString());
    setState(() {
      _transactions.add(newTx);
    });
  }
  
  void startAddNewTransaction(BuildContext ctx) {
    // Este metodo hace que al precionar el boton podamos agregar la informacion para el nuevo elemento
    showModalBottomSheet(
        context: ctx,
        builder: (_) {
          return  GestureDetector( onTap: () {},behavior: HitTestBehavior.opaque, child: NewTransaction(_addNewtransaction), );
        });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Flutter app"),
        actions: <Widget>[
          IconButton(onPressed: ()=> startAddNewTransaction(context), icon: const Icon(Icons.add))
        ],
      ),
      body: SingleChildScrollView(
        child: Column(
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
            ListTrans(_transactions),
            const Card(
              color: Colors.red,
              child: Text("List of Tx"),
            )
          ],
        ),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation
          .centerFloat, // Esto es para controlar la ubicacion del boton flotante.
      floatingActionButton:
          FloatingActionButton(onPressed:  ()=> startAddNewTransaction(context), child: const Icon(Icons.add)),
    );
  }
}
