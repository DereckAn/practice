import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  // const MyApp({super.key});
  void answerQuestions() {
    setState(() {
      questionIndex += 1;
    });
    
    print("Answer chosen!");
  }

  var questionIndex = 0;

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
          children: <Widget>[
            Text(questions[questionIndex]),
            ElevatedButton(
              onPressed: answerQuestions,
              child: const Text("Answer 1"),
            ),
            ElevatedButton(
              onPressed: () => print("Hola como estas?"),
              child: const Text("Answer 2"),
            ),
            const ElevatedButton(
              onPressed: null,
              child: Text("Answer 3"),
            )
          ],
        ),
      ),
    );
  }
}
