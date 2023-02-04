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
      backgroundColor: Color.fromARGB(255, 44, 126, 60),
      appBar: AppBar(
          shape:
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(30)),
          title: Text("Material App"),
          elevation: 0,
          actions: <Widget>[
            IconButton(onPressed: _add, icon: Icon(Icons.accessible_sharp))
          ]),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.end,
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
          Container(
            color: Colors.pink.shade900,
            height: 100,
            width: 100,
          ),
          Row(
            children: <Widget>[
              Expanded(child: Text("Activar sonido")),
              Switch(value: true, onChanged: (value) {}),
            ],
          ),
          Divider(),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: <Widget>[
              Text("Activar camara"),
              Switch(value: true, onChanged: (value) {}),
            ],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: <Widget>[
              Container(
                color: Colors.amber.shade800,
                height: 50,
                width: 50,
              ),
              Container(
                color: Color.fromARGB(255, 24, 148, 167),
                height: 50,
                width: 50,
              ),
              Container(
                color: Color.fromARGB(100, 115, 41, 172),
                height: 100,
                width: 100,
              ),
              Container(
                color: Color.fromARGB(100, 84, 12, 31),
                height: 50,
                width: 50,
              ),
              Container(
                color: Color.fromARGB(255, 225, 225, 29),
                height: 50,
                width: 50,
              )
            ],
          )
        ],
      ),
    );
  }

  void _add() {
    print("Hola Popo");
  }
}
