import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    var questions = [
      "What's your favorite color?",
      "What is your favorite animal?"
    ];
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text("Hola?"),
        ),
        body: Column(
          children: const <Widget>[
            Text("Questions:"),
            ElevatedButton(
              onPressed: null,
              child: Text("Answer 1"),
            ),
            ElevatedButton(
              onPressed: null,
              child: Text("Answer 2"),
            ),
            ElevatedButton(
              onPressed: null,
              child: Text("Answer 3"),
            )
          ],
        ),
      ),
    );
  }
}
