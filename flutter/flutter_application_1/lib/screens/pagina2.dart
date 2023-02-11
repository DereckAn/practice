import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:audioplayers/audioplayers.dart';
import 'package:flutter_application_1/Widgets/ContenCanc.dart';

import '../Widgets/repro.dart';
// import 'package:flutter_application_1/Widgets/canciones.dart';

class SecondPage extends StatefulWidget {
  const SecondPage({super.key});
  // final String name;

  @override
  State<SecondPage> createState() => _SecondPageState();
}

class _SecondPageState extends State<SecondPage> {
  // final player = AudioPlayer();

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Color.fromARGB(255, 19, 73, 81),
        appBar: AppBar(
          backgroundColor: Colors.black87,
          elevation: 0.0,
          title: Text(
            "Your Songs",
            style: TextStyle(fontFamily: "DancingScript-VariableFont_wght.ttf"),
          ),
        ),
        body: ListView(
          children: <Widget>[
            ConCan(path: "Music/Milagrito.mp3"),
            ConCan(path: "Music/Dutustmirniemehrweh.mp3"),
            ConCan(path: "Music/Clair_de_Lune.mp3"),
            ConCan(path: "Music/Bandido.mp3"),
            ConCan(path: "Music/Andare.mp3"),
            ConCan(path: "Music/Another_Love.mp3"),
            ConCan(path: "Music/Somewhere_Only_We_Know.mp3"),
            ConCan(path: "Music/Snow.mp3"),
            ConCan(path: "Music/Billie_Jean.mp3",),
            repro()
          ],
        )
      );
  }
}
