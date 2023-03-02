import 'dart:convert';
import 'package:flutter/material.dart';

// import 'package:audioplayers/audioplayers.dart';

import 'package:just_audio/just_audio.dart';

// import 'package:flutter_application_1/Widgets/canciones.dart';

class SecondPage extends StatefulWidget {
  const SecondPage({super.key});
  // final String name;

  @override
  State<SecondPage> createState() => _SecondPageState();
}

class _SecondPageState extends State<SecondPage> {
  // final player = AudioPlayer();
  final AudioPlayer _player = AudioPlayer();

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    final double HeightS = MediaQuery.of(context).size.height;
    final double WidthS = MediaQuery.of(context).size.width;
    return Scaffold(
        bottomNavigationBar: BottomNavigationBar(
            elevation: 0.0,
            iconSize: 50,
            unselectedItemColor: const Color.fromARGB(255, 137, 11, 11),
            selectedItemColor: Colors.green[700],
            currentIndex: 2,
             // Set the current index to 0 to select the first tab by default
    onTap: (index) { // Define a function to handle tab taps
      if (index == 0) { // Check if the first tab was tapped
        Navigator.pushNamed(context, '/third'); // Navigate to the second screen using the named route '/second'
      }
    },
            items: [
              BottomNavigationBarItem(
                icon: Icon(Icons.home_filled),
                label: "Home",
              ),
              BottomNavigationBarItem(
                  icon: Icon(Icons.search), label: "Search"),
              BottomNavigationBarItem(
                  icon: Icon(Icons.library_music), label: "Library"),
              BottomNavigationBarItem(
                  icon: Icon(Icons.person), label: "Library")
            ]),
        backgroundColor: const Color.fromARGB(255, 0, 0, 0),
        appBar: AppBar(
          backgroundColor: Colors.black87,
          elevation: 0.0,
          title: const Text(
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

              return ListView.builder(
                itemCount: songs?.length,
                itemBuilder: (context, index) {
                  var path = songs![index].toString();
                  var title = path.split("/").last.toString();
                  title = title.replaceAll("%20", "");
                  title = title.split(".").first;

                  return Container(
                    height: HeightS / 17,
                    margin: const EdgeInsets.only(
                        top: 0.0, left: 10.0, right: 10.0),
                    padding: const EdgeInsets.only(top: 0.0, bottom: 0.0),
                    decoration: BoxDecoration(
                      color: const Color.fromARGB(186, 12, 99, 64),
                      borderRadius: BorderRadius.circular(4.0),
                      border: Border.all(
                        color: Colors.black,
                        width: 1.0,
                      ),
                    ),
                    child: ListTile(
                      trailing: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          IconButton(
                            icon: const Icon(Icons.download),
                            color: Colors.white,
                            onPressed: () {},
                          ),
                          IconButton(
                            icon: const Icon(Icons.favorite),
                            color: Colors.white,
                            onPressed: () {},
                          ),
                          IconButton(
                            icon: const Icon(Icons.more_horiz),
                            color: Colors.white,
                            onPressed: () {},
                          ),
                        ],
                      ),
                      // trailing: Icon(Icons.more_horiz, color: Colors.white),
                      textColor: const Color.fromARGB(204, 11, 170, 14),
                      title: Text(
                        title,
                        style: const TextStyle(
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
                        "https://avatars.githubusercontent.com/u/108163041?s=400&u=6c6af4a3b6c32023cde74120f69198ec3b401a4f&v=4",
                      ),
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
