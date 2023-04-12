import 'package:app2/widgets/chart.dart';
import 'package:app2/widgets/new_transaction.dart';
// import 'package:app2/widgets/user_transactions.dart';
import 'package:flutter/material.dart';
// import 'package:flutter/services.dart';

import 'models/transaction.dart';
import 'widgets/transaction_list.dart';

void main() {
  // WidgetsFlutterBinding.ensureInitialized();
  // // Esto es para que la app solo se pueda ver en modo portrait
  // // No se ppermite rotar la pantalla
  // SystemChrome.setPreferredOrientations([
  //   DeviceOrientation.portraitUp, 
  //   DeviceOrientation.portraitDown, ]);
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
      home: const MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  // late String titleInput;  Estas variables son de una manera de caputar el input.

  final List<Transaction> _transactions = [
    // Transaction(id: '01', title: "Water", amount: 10.00, date: DateTime.now()),
    // Transaction(id: '02', title: "Coca", amount: 15.36, date: DateTime.now()),
  ];

  bool _showChart = false;

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
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text("Show chart"),
                Switch(
                  value: _showChart, onChanged: (val) {
                  setState(() {
                    _showChart = val;
                  });
                }),
              ],
            ),
            _showChart ? SizedBox(
              height: (MediaQuery.of(context).size.height - appBar.preferredSize.height - MediaQuery.of(context).padding.top) * .7,
              child: Chart(_recentTransactions)) :
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
