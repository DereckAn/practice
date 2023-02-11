import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';

class repro extends StatefulWidget {
  const repro({super.key});

  @override
  State<repro> createState() => _reproState();
}

class _reproState extends State<repro> {
  final player = AudioPlayer();
  bool isPlaying = false;
  
  @override
  Widget build(BuildContext context) {
    final double HeightS = MediaQuery.of(context).size.height;
    final double WidthS = MediaQuery.of(context).size.width;
    return Stack(
      children: <Widget>[
        Column(
          children: [
            Container(
      height: HeightS/25,
      width: double.infinity,
      color: Color.fromARGB(255, 114, 209, 224),
      child: TextButton(
        onPressed: () {  },
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
                      "Cancion Sonand",
                      style: TextStyle(
                          fontSize: 16,
                          fontFamily: "DancingScript-VariableFont_wght.ttf",
                          color: Colors.white),
                    ),
                    Text(
                      "Cancion Sonand",
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
        // onPressed: () {
        //   if (isPlaying) {
        //     player.stop();
        //   }
        //   player.play(AssetSource(widget.path));
        //   setState(() {
        //     isPlaying = true;
        //   });
        // },
      ),
    ),
            Container(
              height: HeightS/11,
              width: WidthS,
              color: Colors.yellow[800],
              child: Row(
                children: [
                  Container(padding: EdgeInsets.all(10), 
                    color: Color.fromARGB(200, 200, 200, 200),width: WidthS/3, 
                  ),
                   Container(padding: EdgeInsets.all(10),
                    color: Color.fromARGB(199, 197, 69, 69),width: WidthS/3,
                  ),
                   Container(padding: EdgeInsets.all(10),
                    color: Color.fromARGB(199, 56, 155, 173),width: WidthS/3,
                  ),
                ],
              ),
            ),
          ],
        )
      ],
    );
  }
}
