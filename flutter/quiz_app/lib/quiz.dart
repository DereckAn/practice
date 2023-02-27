import 'package:flutter/material.dart';

import './questions.dart';
import './answer.dart';

class Quiz extends StatelessWidget {
  final List<Map<String, Object>> questions;
  final int questionIndex;
  final Function answerQuestions;  // Mucho cuidado aqui. No pongas VoidCallBack porque te dara muchos errores. 

  const Quiz(
      {required this.questions,
      required this.questionIndex,
      required this.answerQuestions});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        Question(questions[questionIndex]['Question'] as String),
        ...(questions[questionIndex]['Answers'] as List<Map<String, Object>>) // Este codigo es para las respuestas. Se generara un boton para cada posible respuesta localizada en el map
            .map((answer) {
          return Answer(()=>answerQuestions(answer['score']), answer['text'] as String);
        }),
      ],
    );
  }
}
