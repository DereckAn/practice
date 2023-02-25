import 'package:flutter/material.dart';
import './questions.dart';
import './answer.dart';

void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  // const MyApp({super.key});
  void _answerQuestions() {
    setState(() {
      _questionIndex += 1;
    });

    print("Answer chosen!");
  }

  var _questionIndex = 0;

  @override
  Widget build(BuildContext context) {
    const questions = [
      {
        "Question": "What's your favorite color?", // Esto es un mapa
        "Answers": ["Red", "Green", "Blue", "Black"]
      },
      {
        "Question": "What's your favorite animal?",
        "Answers": ["Rabbit", "Gale", "Bird", "Dog"]
      },
      {
        "Question": "What's your favorite Food?",
        "Answers": ["Burger", "Salad", "Pizza", "Raise", "Ham"]
      },
    ];
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text("Hola?"),
        ),
        body: Column(
          children: <Widget>[
            Question(questions[_questionIndex]['Question'] as String),


            ...(questions[_questionIndex]['Answers'] as List<String>) // Este codigo es para las respuestas. Se generara un boton para cada posible respuesta localizada en el map
                .map((answer) {
              return asnwer(_answerQuestions, answer);
            }),
          ],
        ),
      ),
    );
  }
}
