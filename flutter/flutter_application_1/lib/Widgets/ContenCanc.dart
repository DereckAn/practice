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
    final double HeightS = MediaQuery.of(context).size.height;
    final double WidthS = MediaQuery.of(context).size.width;
    return Container(
      height: HeightS/19,
      width: WidthS,
      color: const Color.fromARGB(255, 19, 73, 81),
      child: TextButton(
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            Row(
              children: <Widget>[
                Container(
                  // margin: EdgeInsetsDirectional.only(start: 10),
                  height: WidthS/10,
                  width:  WidthS/10,
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
                      style: const TextStyle(
                          fontSize: 16,
                          fontFamily: "DancingScript-VariableFont_wght.ttf",
                          color: Colors.white),
                    ),
                    Text(
                      widget.path.substring(6, widget.path.length - 4),
                      style: const TextStyle(
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
                  icon: const Icon(Icons.favorite),
                  onPressed: () {
                    // player.play(AssetSource(widget.path));
                  },
                ),
                IconButton(
                  alignment: Alignment.centerRight,
                  color: Colors.white,
                  icon: const Icon(Icons.more_horiz),
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
