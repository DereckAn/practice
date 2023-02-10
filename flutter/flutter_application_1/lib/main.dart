import 'package:flutter/material.dart';
// import 'package:audioplayer/audioplayer.dart';
import 'screens/pagina1.dart';
import 'screens/pagina2.dart';
// import 'a.dart';
// import 'dart:_interceptors';
// import 'package:parse_server_sdk_flutter/parse_server_sdk_dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
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
