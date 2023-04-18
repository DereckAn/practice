import 'dart:io';

import 'package:app2/widgets/chart.dart';
import 'package:app2/widgets/new_transaction.dart';
// import 'package:flutter/cupertino.dart';
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

  void _addNewtransaction(
      String txTitle, double txAmount, DateTime chosenDate) {
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

  void _deleteTransaction(String id) {
    setState(() {
      _transactions.removeWhere((tx) => tx.id == id);
    });
  }

  @override
  Widget build(BuildContext context) {
    final mediaQuety = MediaQuery.of(context);
    final isLandscape = mediaQuety.orientation == Orientation.landscape;

    //  final PreferredSize appBar = Platform.isIOS
    //     ? CupertinoNavigationBar(
    //         middle: const Text("Flutter app"),
    //         trailing: Row(
    //           mainAxisSize: MainAxisSize.min,
    //           children: [
    //             GestureDetector(
    //                 onTap: () => startAddNewTransaction(context),
    //                 child: const Icon(CupertinoIcons.add))
    //           ],
    //         ),
    //       )
    //     : AppBar(
    //         title: Text("Flutter app"),
    //         actions: <Widget>[
    //           IconButton(
    //               onPressed: () => startAddNewTransaction(context),
    //               icon: const Icon(Icons.add))
    //         ],
    //       );

    final appBar = AppBar(
      title: const Text("Flutter app"),
      actions: <Widget>[
        IconButton(
            onPressed: () => startAddNewTransaction(context),
            icon: const Icon(Icons.add))
      ],
    );

    final listBuy = SizedBox(
        height: (mediaQuety.size.height -
                appBar.preferredSize.height -
                mediaQuety.padding.top) *
            0.6,
        child: ListTrans(_transactions, _deleteTransaction));

    final maini = SafeArea(
      child: SingleChildScrollView(
        child: Column(
          // mainAxisAlignment: MainAxisAlignment.spaceBetween,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            if (isLandscape)
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Text("Show chart"),
                  Switch.adaptive(
                      // Esto es para que el switch se adapte al sistema operativo
                      value: _showChart,
                      onChanged: (val) {
                        setState(() {
                          _showChart = val;
                        });
                      }),
                ],
              ),
            if (!isLandscape)
              SizedBox(
                  height: (mediaQuety.size.height -
                          appBar.preferredSize.height -
                          mediaQuety.padding.top) *
                      .3,
                  child: Chart(_recentTransactions)),
            if (!isLandscape) listBuy,
            if (isLandscape)
              _showChart
                  ? SizedBox(
                      height: (mediaQuety.size.height -
                              appBar.preferredSize.height -
                              mediaQuety.padding.top) *
                          .7,
                      child: Chart(_recentTransactions))
                  : listBuy,
            const Card(
              color: Colors.red,
              child: Text("List of Tx"),
            )
          ],
        ),
      ),
    );
  return  Scaffold(
            appBar: appBar,
            body: maini,
            floatingActionButtonLocation: FloatingActionButtonLocation
                .centerFloat, // Esto es para controlar la ubicacion del boton flotante.
            floatingActionButton: Platform.isIOS
                ? Container()
                : // Esto es para que el boton flotante solo se muestre en android
                FloatingActionButton(
                    onPressed: () => startAddNewTransaction(context),
                    child: const Icon(Icons.add)),
          );
    // return Platform.isIOS
    //     ? CupertinoPageScaffold(
    //         navigationBar: appBar,
    //         child: maini,
    //       )
  
  }
}
