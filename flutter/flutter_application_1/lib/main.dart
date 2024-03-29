import 'package:flutter/material.dart';
import 'screens/mobethas.dart';
import 'screens/pagina1.dart';
import 'screens/pagina2.dart';
import 'screens/pagina3.dart';
import 'screens/palabraCambiante.dart';


void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Hola Princesa',
      theme: ThemeData(
        fontFamily: "DancingScript-VariableFont_wght.ttf",
        primarySwatch: Colors.red,
      ),
      // home: MyHomePage(),
      initialRoute: "/",
      routes: {
        "/":(BuildContext context) => MyHomePage(),
      "/second":(BuildContext context) => const SecondPage(),
      "/third":(BuildContext context) => const CambioPalabra(),
      "/fouth":(BuildContext context) => const Mobetas(),
      "/fifth":(BuildContext context) => const ExpansionPanelListExample()},
    );
  }
}
