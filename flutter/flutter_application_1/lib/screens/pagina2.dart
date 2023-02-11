import 'dart:convert';
import 'dart:typed_data';
import 'package:flutter/material.dart';
// import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/services.dart';
import 'package:flutter_application_1/Widgets/ContenCanc.dart';
import 'package:just_audio/just_audio.dart';

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
  AudioPlayer _player = AudioPlayer();

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    final double HeightS = MediaQuery.of(context).size.height;
    final double WidthS = MediaQuery.of(context).size.width;
    return Scaffold(
        bottomNavigationBar: BottomAppBar(
          elevation: 0.0,
          color: Color.fromARGB(0, 183, 18, 18),
          child: Container(
            child: repro(),
            height: HeightS / 7.3,
          ),
        ),
        backgroundColor: Color.fromARGB(255, 19, 73, 81),
        appBar: AppBar(
          backgroundColor: Colors.black87,
          elevation: 0.0,
          title: Text(
            "Your Songs",
            style: TextStyle(fontFamily: "DancingScript-VariableFont_wght.ttf"),
          ),
        ),
        body: FutureBuilder<String>(
          future:
              DefaultAssetBundle.of(context).loadString("AssetManifest.json"),
          // future: rootBundle.loadString("AssetManifest.json")
          builder: (context, item) {
            if (item.hasData) {
              Map? jsonMap = json.decode(item.data!);
              // List? songs = jsonMap?.keys.toList();
              List? songs = jsonMap?.keys
                  .where((element) => element.endsWith(".mp3"))
                  .toList();
              print(jsonMap);
              print("\n\n\n");
              print(songs);

              return ListView.builder(
                itemCount: songs?.length,
                itemBuilder: (context, index) {
                  var path = songs![index].toString();
                  var title = path.split("/").last.toString();
                  title = title.replaceAll("%20", "");
                  title = title.split(".").first;

                  return Container(
                    margin: const EdgeInsets.only(
                        top: 10.0, left: 10.0, right: 15.0),
                    padding: const EdgeInsets.only(top: 0.0, bottom: 0.0),
                    decoration: BoxDecoration(
                      color: Color.fromARGB(33, 35, 142, 33),
                      borderRadius: BorderRadius.circular(4.0),
                      border: Border.all(
                        color: Colors.white70,
                        width: 1.0,
                      ),
                    ),
                    child: ListTile(
                      trailing:
                          const Icon(Icons.more_horiz, color: Colors.white),
                      textColor: Colors.white30,
                      title: Text(
                        title,
                        style: TextStyle(
                            fontFamily: "DancingScript-VariableFont_wght.ttf"),
                      ),
                      subtitle: Text(
                          "path: ${path.substring(13, path.length - 4)}",
                          style: const TextStyle(
                              color: Colors.white70,
                              fontSize: 12.0,
                              fontFamily:
                                  "DancingScript-VariableFont_wght.ttf")),
                      leading: Image.network(
                          "https://avatars.githubusercontent.com/u/108163041?s=400&u=6c6af4a3b6c32023cde74120f69198ec3b401a4f&v=4"),
                      onTap: () async {
                        final snackBar = SnackBar(
                          content: Text(title),
                        );
                        ScaffoldMessenger.of(context).showSnackBar(snackBar);
                        // await player.setSourceAsset(path.substring(13));
                        // await player.play(
                        //     AssetSource("${(songs[index]).substring(13)}"));
                        print((songs[index]).substring(13));
                        await _player.setAsset(path);
                        await _player.play();
                      },
                    ),
                  );
                },
              );
            } else {
              return const Center(child: Text("No Songs Found"));
            }
          },
        )

        // body: ListView(
        //   children: <Widget>[
        //     ConCan(path: "Music/Milagrito.mp3"),
        //     ConCan(path: "Music/Dutustmirniemehrweh.mp3"),
        //     ConCan(path: "Music/Clair_de_Lune.mp3"),
        //     ConCan(path: "Music/Bandido.mp3"),
        //     ConCan(path: "Music/Andare.mp3"),
        //     ConCan(path: "Music/Another_Love.mp3"),
        //     ConCan(path: "Music/Somewhere_Only_We_Know.mp3"),
        //     ConCan(path: "Music/Snow.mp3"),
        //     ConCan(path: "Music/Billie_Jean.mp3"),
        //     // repro()
        //   ],
        // ),
        );
  }
}
