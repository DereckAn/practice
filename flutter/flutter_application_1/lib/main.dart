import 'package:flutter/material.dart';
// import 'package:parse_server_sdk_flutter/parse_server_sdk_dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  MyHomePage();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      endDrawer: Drawer(),
      drawer: Drawer(),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.accessibility_new),
        onPressed: () {},
      ),
      backgroundColor: Color.fromARGB(255, 69, 44, 126),
      appBar: AppBar(title: Text("Material App")),
      body: Column(
        children: [
          Center(
            child: Text(
              "Hola",
              style: TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                  color: Color.fromARGB(255, 243, 233, 33),
                  backgroundColor: Colors.black),
            ),
          ),
          Image.network(
            "http://t3.gstatic.com/licensed-image?q=tbn:ANd9GcRlex2yeMomsbkm0qzpHjtPf8j9QLCDPLZ_brREwaQIrpsnwot3sOfn8Qr3ujA92cho",
            height: 200,
          ),
          Icon(size: 100, Icons.favorite),
          IconButton(
              iconSize: 100,
              onPressed: () {
                print("hola");
              },
              icon: Icon(Icons.favorite_border)),
        ],
      ),
    );
  }
}
