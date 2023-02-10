import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:audioplayers/audioplayers.dart';
import 'package:flutter_application_1/Widgets/ContenCanc.dart';
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
          ],
        ));
  }

  // Widget reproducir() {
  //   String path = "Milagrito.mp3";
  //   return Row(
  //     mainAxisAlignment: MainAxisAlignment.spaceBetween,
  //     crossAxisAlignment: CrossAxisAlignment.center,
  //     children: <Widget>[
  //       Container(
  //         margin: EdgeInsetsDirectional.only(start: 10),
  //         color: Colors.amber.shade800,
  //         height: 50,
  //         width: 50,
  //         child: Image.network(
  //             "https://avatars.githubusercontent.com/u/108163041?s=400&u=6c6af4a3b6c32023cde74120f69198ec3b401a4f&v=4"),
  //       ),
  //       TextButton(
  //         onPressed: () {},
  //         child: Text(
  //           path,
  //           style: TextStyle(
  //               fontFamily: "DancingScript-VariableFont_wght.ttf",
  //               color: Colors.white),
  //         ),
  //       ),
  //       IconButton(
  //         color: Colors.white,
  //         icon: Icon(Icons.play_arrow),
  //         onPressed: () {
  //           // AudioPlayer.play();
  //           player.play(AssetSource(path));
  //         },
  //       ),
  //       IconButton(
  //         color: Colors.white,
  //         icon: Icon(Icons.stop),
  //         onPressed: () {
  //           player.stop();
  //         },
  //       ),
  //       IconButton(
  //         color: Colors.white,
  //         icon: Icon(Icons.more_horiz),
  //         onPressed: () {
  //           player.pause();
  //         },
  //       ),
  //       IconButton(
  //         color: Colors.white,
  //         icon: Icon(Icons.favorite),
  //         onPressed: () {
  //           player.resume();
  //         },
  //       ),

  //     ],
  //   );
  // }

  //  Widget reproducir2() {
  //   String path = "Dutustmirniemehrweh.mp3";
  //   return Row(
  //     mainAxisAlignment: MainAxisAlignment.spaceBetween,
  //     crossAxisAlignment: CrossAxisAlignment.center,
  //     children: <Widget>[
  //       Container(
  //         margin: EdgeInsetsDirectional.only(start: 10),
  //         color: Colors.amber.shade800,
  //         height: 50,
  //         width: 50,
  //         child: Image.network(
  //             "https://avatars.githubusercontent.com/u/108163041?s=400&u=6c6af4a3b6c32023cde74120f69198ec3b401a4f&v=4"),
  //       ),
  //       TextButton(
  //         onPressed: () {},
  //         child: Text(
  //           path,
  //           style: TextStyle(
  //               fontFamily: "DancingScript-VariableFont_wght.ttf",
  //               color: Colors.white),
  //         ),
  //       ),
  //       IconButton(
  //         color: Colors.white,
  //         icon: Icon(Icons.play_arrow),
  //         onPressed: () {
  //           // AudioPlayer.play();
  //           player.play(AssetSource(path));
  //         },
  //       ),
  //       IconButton(
  //         color: Colors.white,
  //         icon: Icon(Icons.stop),
  //         onPressed: () {
  //           player.stop();
  //         },
  //       ),
  //       IconButton(
  //         color: Colors.white,
  //         icon: Icon(Icons.more_horiz),
  //         onPressed: () {
  //           player.pause();
  //         },
  //       ),
  //       IconButton(
  //         color: Colors.white,
  //         icon: Icon(Icons.favorite),
  //         onPressed: () {
  //           player.resume();
  //         },
  //       )
  //     ],
  //   );
  // }

  //  Widget reproducir3() {
  //   String path = "Clair_de_Lune.mp3";
  //   return Row(
  //     mainAxisAlignment: MainAxisAlignment.spaceBetween,
  //     crossAxisAlignment: CrossAxisAlignment.center,
  //     children: <Widget>[
  //       Container(
  //         margin: EdgeInsetsDirectional.only(start: 10),
  //         color: Colors.amber.shade800,
  //         height: 50,
  //         width: 50,
  //         child: Image.network(
  //             "https://avatars.githubusercontent.com/u/108163041?s=400&u=6c6af4a3b6c32023cde74120f69198ec3b401a4f&v=4"),
  //       ),
  //       TextButton(
  //         onPressed: () {},
  //         child: Text(
  //           path,
  //           style: TextStyle(
  //               fontFamily: "DancingScript-VariableFont_wght.ttf",
  //               color: Colors.white),
  //         ),
  //       ),
  //       IconButton(
  //         color: Colors.white,
  //         icon: Icon(Icons.play_arrow),
  //         onPressed: () {
  //           // AudioPlayer.play();
  //           player.play(AssetSource(path));
  //         },
  //       ),
  //       IconButton(
  //         color: Colors.white,
  //         icon: Icon(Icons.stop),
  //         onPressed: () {
  //           player.stop();
  //         },
  //       ),
  //       IconButton(
  //         color: Colors.white,
  //         icon: Icon(Icons.more_horiz),
  //         onPressed: () {
  //           player.pause();
  //         },
  //       ),
  //       IconButton(
  //         color: Colors.white,
  //         icon: Icon(Icons.favorite),
  //         onPressed: () {
  //           player.resume();
  //         },
  //       )
  //     ],
  //   );
  // }

  // Widget reproducir4() {
  //   String path = "Music/Bandido.mp3";
  //   return Row(
  //     mainAxisAlignment: MainAxisAlignment.spaceBetween,
  //     crossAxisAlignment: CrossAxisAlignment.center,
  //     children: <Widget>[
  //       Container(
  //         margin: EdgeInsetsDirectional.only(start: 10),
  //         color: Colors.amber.shade800,
  //         height: 50,
  //         width: 50,
  //         child: Image.network(
  //             "https://avatars.githubusercontent.com/u/108163041?s=400&u=6c6af4a3b6c32023cde74120f69198ec3b401a4f&v=4"),
  //       ),
  //       TextButton(
  //         onPressed: () {},
  //         child: Text(
  //           path.substring(6,path.length - 4),
  //           style: TextStyle(
  //               fontFamily: "DancingScript-VariableFont_wght.ttf",
  //               color: Colors.white),
  //         ),
  //       ),
  //       IconButton(
  //         color: Colors.white,
  //         icon: Icon(Icons.play_arrow),
  //         onPressed: () {
  //           // AudioPlayer.play();
  //           player.play(AssetSource(path));
  //         },
  //       ),
  //       IconButton(
  //         color: Colors.white,
  //         icon: Icon(Icons.stop),
  //         onPressed: () {
  //           player.stop();
  //         },
  //       ),
  //       IconButton(
  //         color: Colors.white,
  //         icon: Icon(Icons.more_horiz),
  //         onPressed: () {
  //           player.pause();
  //         },
  //       ),
  //       IconButton(
  //         color: Colors.white,
  //         icon: Icon(Icons.favorite),
  //         onPressed: () {
  //           player.resume();
  //         },
  //       )
  //     ],
  //   );
  // }
}
