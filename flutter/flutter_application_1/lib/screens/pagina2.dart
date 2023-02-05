import 'package:flutter/material.dart';

class SecondPage extends StatelessWidget {
  const SecondPage({Key? key, required this.name}) : super(key: key);
  final String name;

  @override
  Widget build(BuildContext context) {
    // SecondPageArguments arguments = ModalRoute.of(context).settings.arguments;
    return Scaffold(
      appBar: AppBar(
        title: Text("Sedunga pantalla"),
      ),
      body: Center(
        child: Text(name),

      ),
    );
  }
}

// class SecondPageArguments {
//   String name;
//   String lastName;
//   SecondPageArguments({String name, String lastName});
// }
