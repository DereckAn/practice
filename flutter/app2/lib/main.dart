import 'package:app2/widgets/chart.dart';
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
      title: 'Perosnal Expenses',
      theme: ThemeData(
          // textTheme: ,
          appBarTheme: AppBarTheme(
            toolbarTextStyle: ThemeData.light()
                .textTheme
                .copyWith(
                  titleLarge: const TextStyle(
                    fontFamily: "OpenSans",
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                  ),
                )
                .bodyMedium,
            titleTextStyle: ThemeData.light()
                .textTheme
                .copyWith(
                  titleLarge: const TextStyle(
                    fontFamily: "OpenSans",
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                  ),
                )
                .titleLarge,
          ),
          fontFamily: "Quicksand",
          colorScheme: ColorScheme.fromSwatch(primarySwatch: Colors.green)
              .copyWith(secondary: Colors.amber)),
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
    // Transaction(id: '01', title: "Water", amount: 10.00, date: DateTime.now()),
    // Transaction(id: '02', title: "Coca", amount: 15.36, date: DateTime.now()),
  ];

  List<Transaction> get _recentTransactions {
    return _transactions.where((tx) {
      return tx.date.isAfter(
        DateTime.now().subtract(
          const Duration(days: 7),
        ),
      );
    }).toList();
  }

  void _addNewtransaction(String txTitle, double txAmount, DateTime chosenDate) {
    final newTx = Transaction(
        title: txTitle,
        amount: txAmount,
        date: chosenDate,
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
          return GestureDetector(
            onTap: () {},
            behavior: HitTestBehavior.opaque,
            child: NewTransaction(_addNewtransaction),
          );
        });
  }

  void _deleteTransaction(String id){
    setState((){
      _transactions.removeWhere((tx) => tx.id == id);
    });
  }
   
  

  @override
  Widget build(BuildContext context) { 
    final appBar =  AppBar(
        title: const Text("Flutter app"),
        actions: <Widget>[
          IconButton(
              onPressed: () => startAddNewTransaction(context),
              icon: const Icon(Icons.add))
        ],
      );
    return Scaffold(
      appBar: appBar,
      body: SingleChildScrollView(
        child: Column(
          // mainAxisAlignment: MainAxisAlignment.spaceBetween,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            SizedBox(
              height: (MediaQuery.of(context).size.height - appBar.preferredSize.height - MediaQuery.of(context).padding.top) * 0.3,
              child: Chart(_recentTransactions)),
            SizedBox(
              height: (MediaQuery.of(context).size.height - appBar.preferredSize.height - MediaQuery.of(context).padding.top) * 0.6,
              child: ListTrans(_transactions, _deleteTransaction)),
            const Card(
              color: Colors.red,
              child: Text("List of Tx"),
            )
          ],
        ),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation
          .centerFloat, // Esto es para controlar la ubicacion del boton flotante.
      floatingActionButton: FloatingActionButton(
          onPressed: () => startAddNewTransaction(context),
          child: const Icon(Icons.add)),
    );
  }
}
