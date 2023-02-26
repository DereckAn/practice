import 'package:flutter/material.dart';
import 'package:quiz_app/result.dart';

import './quiz.dart';

void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  var _questionIndex = 0;
  var _totalScore = 0;

  final _questions = const [
    {
      "Question": "What's your favorite color?", // Esto es un mapa
      "Answers": [
        {"text": "Red", "score": 2},
        {"text": "Green", "score": 7},
        {"text": "Blue", "score": 9},
        {"text": "Black", "score": 10}
      ]
    },
    {
      "Question": "What's your favorite animal?",
      "Answers": [
        {"text": "Rabbit", "score": 8},
        {"text": "Duck", "score": 11},
        {"text": "Bird", "score": 9},
        {"text": "Dog", "score": 10}
      ]
    },
    {
      "Question": "What's your favorite Food?",
      "Answers": [
        {"text": "Burger", "score": 6},
        {"text": "Salad", "score": 7},
        {"text": "Pizza", "score": 10},
        {"text": "Ham", "score": 1}
      ]
    },
    {
      "Question": "What's your favorite Videogame?",
      "Answers": [
        {"text": "Metal Gear", "score": 10},
        {"text": "Mario Bros", "score": 7},
        {"text": "The last of us", "score": 10},
        {"text": "Dead Space", "score": 9}
      ]
    },
  ];

  void _answerQuestions(int score) {
    _totalScore += score;

    if (_questionIndex < _questions.length) {
      print("Wh have more questions");
    }
    setState(() {
      _questionIndex += 1;
    });

    print("Answer chosen!");
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
          appBar: AppBar(
            title: const Text("Hola?"),
          ),
          body: _questionIndex <_questions.length //Aqui estamos poniendo un if.   Si el _questionIndex es menor que la logitus de questions entonces es verdadero.
              ? Quiz(
                  answerQuestions: _answerQuestions,
                  questionIndex: _questionIndex,
                  questions: _questions,
                )
              : Result(
                  _totalScore) // Aqui estamos poniendo el else. Si no es verdadero el if que pusimo en arriva entonces aparecera un widget "center"
          ),
    );
  }
}
