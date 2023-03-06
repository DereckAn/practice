import 'package:flutter/material.dart';

class Answer extends StatelessWidget {
  final VoidCallback selectHandler;
  final String answerText;

  const Answer(this.selectHandler, this.answerText);

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: double.infinity,
      child: ElevatedButton(
        // style: ButtonStyle(textStyle: Colors.green),
        style: ButtonStyle(backgroundColor: MaterialStateProperty.all(const Color.fromARGB(255, 40, 170, 110)), ),
        onPressed: selectHandler,
        child: Text(answerText, style:  const TextStyle(color: Color.fromARGB(255, 179, 41, 75))),
      ),
    );
  }
}
