import 'package:flutter/material.dart';
import 'screens/pagina1.dart';
import 'screens/pagina2.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Hola Princesa',
      theme: ThemeData(
        fontFamily: "dereck-agneles",
        primarySwatch: Colors.red,
      ),
      // home: MyHomePage(),
      initialRoute: "/",
      routes: {
        "/":(BuildContext context) => MyHomePage(),
      "/second":(BuildContext context) => SecondPage(),},
    );
  }
}
