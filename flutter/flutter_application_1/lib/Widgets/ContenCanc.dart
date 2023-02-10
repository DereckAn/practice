import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/material.dart';

class ConCan extends StatefulWidget {
  final String path;
  const ConCan({required this.path});

  @override
  State<ConCan> createState() => _ConCanState();
}

class _ConCanState extends State<ConCan> {
  final player = AudioPlayer();
  bool isPlaying = false;

  @override
  void initState() {
    super.initState();
    player.onPlayerStateChanged.listen((state) {
      if (state == PlayerState.stopped) {
        setState(() {
          isPlaying = false;
        });
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 60,
      width: double.infinity,
      color: Color.fromARGB(255, 19, 73, 81),
      child: TextButton(
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            Row(
              children: <Widget>[
                Container(
                  // margin: EdgeInsetsDirectional.only(start: 10),
                  height: 50,
                  width: 50,
                  child: Image.network(
                      "https://avatars.githubusercontent.com/u/108163041?s=400&u=6c6af4a3b6c32023cde74120f69198ec3b401a4f&v=4"),
                ),
                Container(margin: EdgeInsets.all(7)),
                Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: <Widget>[
                    Text(
                      widget.path.substring(6, widget.path.length - 4),
                      style: TextStyle(
                          fontSize: 16,
                          fontFamily: "DancingScript-VariableFont_wght.ttf",
                          color: Colors.white),
                    ),
                    Text(
                      widget.path.substring(6, widget.path.length - 4),
                      style: TextStyle(
                          fontSize: 14,
                          fontFamily: "DancingScript-VariableFont_wght.ttf",
                          color: Color.fromARGB(255, 134, 134, 134)),
                    ),
                  ],
                ),
              ],
            ),
            Row(
              children: <Widget>[
                IconButton(
                  alignment: Alignment.centerRight,
                  color: Colors.white,
                  icon: Icon(Icons.favorite),
                  onPressed: () {
                    // player.play(AssetSource(widget.path));
                  },
                ),
                IconButton(
                  alignment: Alignment.centerRight,
                  color: Colors.white,
                  icon: Icon(Icons.more_horiz),
                  onPressed: () {
                    player.stop();
                  },
                ),
              ],
            ),
          ],
        ),
        onPressed: () {
          if (isPlaying) {
            player.stop();
          }
          player.play(AssetSource(widget.path));
          setState(() {
            isPlaying = true;
          });
        },
      ),
    );
  }
}
