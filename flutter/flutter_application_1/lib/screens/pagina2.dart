import 'dart:typed_data';

import 'package:flutter/material.dart';
// import 'package:audioplayer/audioplayer.dart';
import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/services.dart' show rootBundle;
// import 'package:audioplayers/audio_cache.dart';

class SecondPage extends StatefulWidget {
  const SecondPage({super.key});
  // final String name;

  @override
  State<SecondPage> createState() => _SecondPageState();
  // @override
  // _PlayButtonState createState() => _PlayButtonState();
}

class _SecondPageState extends State<SecondPage> {
  final cancion = "Du tust mir nie mehr weh - AnnenMayKantereit.mp3";

//   AudioPlayer _audioPlayer = AudioPlayer();

//   void _play() async {
//   String audioPath = 'assets/Du tust mir nie mehr weh - AnnenMayKantereit.mp3';
//   ByteData data = await rootBundle.load(audioPath);
//   // int result = await _audioPlayer.play(data.buffer.asUint8List(), isLocal: true);
//   if (result == 1) {
//     // success
//   }
// }

  @override
  Widget build(BuildContext context) {
    // SecondPageArguments arguments = ModalRoute.of(context).settings.arguments;
    return Scaffold(
        backgroundColor: Color.fromARGB(255, 21, 21, 21),
        appBar: AppBar(
          title: Text("Sedunga pantalla"),
        ),
        body: ListView(
          children: [
            Container(
                height: 60,
                width: double.infinity,
                color: Colors.transparent,
                child: reproducir(),
                padding: EdgeInsets.all(1)),
            Container(
              height: 50,
              width: double.infinity,
              color: Color.fromARGB(255, 153, 187, 86),
            ),
            Container(
              height: 50,
              width: double.infinity,
              color: Color.fromARGB(255, 195, 96, 96),
            ),
            Container(
              height: 50,
              width: double.infinity,
              color: Color.fromARGB(255, 173, 177, 119),
            ),
            Container(
              height: 50,
              width: double.infinity,
              color: Color.fromARGB(255, 17, 106, 23),
            ),
            Container(
              height: 50,
              width: double.infinity,
              color: Color.fromARGB(255, 106, 88, 17),
            ),
            Container(
              height: 50,
              width: double.infinity,
              color: Color.fromARGB(255, 106, 17, 51),
            ),
          ],
        ));
  }

  Widget reproducir() {
    // bool isFavorited = false;
    // int favoriteCount = 0;

    // void _toggleFavorite() {
    //   setState(
    //     () {
    //       if (isFavorited) {
    //         favoriteCount--;
    //         isFavorited = false;
    //       } else {
    //         favoriteCount++;
    //         isFavorited = true;
    //       }
    //     },
    //   );
    // }

    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      crossAxisAlignment: CrossAxisAlignment.center,
      children: <Widget>[
        Container(
          margin: EdgeInsetsDirectional.only(start: 10),
          color: Colors.amber.shade800,
          height: 50,
          width: 50,
          child: Image.network(
              "https://avatars.githubusercontent.com/u/108163041?s=400&u=6c6af4a3b6c32023cde74120f69198ec3b401a4f&v=4"),
        ),
        TextButton(
          onPressed: () {},
          child: Text(
            "Nombre de la cancion",
            style: TextStyle(
                fontFamily: "DancingScript-VariableFont_wght.ttf",
                color: Colors.white),
          ),
        ),
        // IconButton(
        //   icon: (isFavorited ? Icon(Icons.star) : Icon(Icons.star_border)),
        //   color: (isFavorited ? Color.fromARGB(255, 220, 218, 209) : null),
        //   onPressed: _toggleFavorite,
        // ),
        IconButton(
          color: Colors.white,
          icon: Icon(Icons.play_arrow),
          onPressed: () {
            // _play();
          },
        ),
        IconButton(
          color: Colors.white,
          icon: Icon(Icons.more_vert),
          onPressed: () {},
        ),
      ],
    );
  }
}

// class SecondPageArguments {
//   String name;
//   String lastName;
//   SecondPageArguments({String name, String lastName});
// }
