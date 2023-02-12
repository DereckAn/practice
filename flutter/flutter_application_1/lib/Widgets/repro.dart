// import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';

class repro extends StatefulWidget {
  const repro({super.key});

  @override
  State<repro> createState() => _reproState();
}

class _reproState extends State<repro> {
  // final player = AudioPlayer();
  bool isPlaying = false;

  @override
  Widget build(BuildContext context) {
    final double HeightS = MediaQuery.of(context).size.height;
    final double WidthS = MediaQuery.of(context).size.width;
    return Container(
        // width: double.infinity,
        // height: double.infinity,
        child: Column(
      children: [
        Container(
          height: HeightS / 22,
          width: double.infinity,
          decoration: BoxDecoration(
              color: Color.fromARGB(84, 255, 7, 85),
              borderRadius: BorderRadius.all(Radius.circular(7))),
          child: TextButton(
            onPressed: () {},
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: <Widget>[
                Row(
                  children: <Widget>[
                    Container(
                      height: 50,
                      width: 50,
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.all(Radius.circular(7)),
                        image: DecorationImage(
                            image: NetworkImage(
                                "https://avatars.githubusercontent.com/u/108163041?s=400&u=6c6af4a3b6c32023cde74120f69198ec3b401a4f&v=4"),
                            fit: BoxFit.cover),

                        // child: ,fit: BoxFit.cover,
                      ),
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
                      icon: Icon(
                        Icons.play_arrow,
                      ),
                      onPressed: () {
                        // player.stop();
                      },
                      splashRadius: 1,
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
          height: HeightS / 11,
          width: WidthS,
          color: Color.fromARGB(64, 249, 168, 37),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.center,
            // mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              Container(
                // padding: EdgeInsets.all(10),
                color: Color.fromARGB(0, 0, 0, 0),
                width: WidthS / 3,
                height: HeightS / 11,
                child: IconButton(
                    onPressed: () {},
                    icon: Icon(Icons.home_filled),
                    iconSize: 100,
                    color: Colors.white,
                    splashRadius: 1),
              ),
              Container(
                // padding: EdgeInsets.all(10),
                color: Color.fromARGB(0, 0, 0, 0),
                width: WidthS / 3,
                height: HeightS / 11,
                child: IconButton(
                    onPressed: () {},
                    icon: Icon(Icons.search),
                    iconSize: 100,
                    color: Colors.white,
                    splashRadius: 1),
              ),
              Container(
                // padding: EdgeInsets.all(10),
                color: Color.fromARGB(0, 0, 0, 0),
                width: WidthS / 3,
                height: HeightS / 11,
                child: IconButton(
                  onPressed: () {},
                  icon: Icon(Icons.library_music),
                  iconSize: 100,
                  color: Colors.white,
                  splashRadius: 1,
                ),
              ),
            ],
          ),
        ),
      ],
    ));
  }
}
