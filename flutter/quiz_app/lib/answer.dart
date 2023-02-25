import 'package:flutter/material.dart';

class asnwer extends StatelessWidget {
  final VoidCallback selectHandler;
  final String answerText;

  const asnwer(this.selectHandler, this.answerText);

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: double.infinity,
      child: ElevatedButton(
        // style: ButtonStyle(textStyle: Colors.green),
        style: ButtonStyle(backgroundColor: MaterialStateProperty.all(Colors.amber), ),
        onPressed: selectHandler,
        child: Text(answerText, style:  const TextStyle(color: Color.fromARGB(255, 41, 174, 179))),
      ),
    );
  }
}
