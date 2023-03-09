import 'package:flutter/material.dart';
// import 'package:audioplayer/audioplayer.dart';

class MyHomePage extends StatefulWidget {
  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  // MyHomePage();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      bottomNavigationBar: BottomAppBar(
        child: Container(
          height: 60,
          color: Colors.amber,
        ),
      ),
      endDrawer: Drawer(
          backgroundColor: const Color.fromARGB(255, 23, 94, 103),
          child: infinitIma()),
      drawer: Drawer(
          backgroundColor:const Color.fromARGB(255, 121, 45, 45),
          child: ListView(
            children: [
              Card(
                child: Image.network(
                    "https://avatars.githubusercontent.com/u/108163041?s=400&u=6c6af4a3b6c32023cde74120f69198ec3b401a4f&v=4"),
              ),
              Card(
                child: Image.network(
                    "https://avatars.githubusercontent.com/u/108163041?s=400&u=6c6af4a3b6c32023cde74120f69198ec3b401a4f&v=4"),
              ),
              Card(
                child: Image.network(
                    "https://avatars.githubusercontent.com/u/108163041?s=400&u=6c6af4a3b6c32023cde74120f69198ec3b401a4f&v=4"),
              ),
              Card(
                child: Image.asset("assets/ima5.JPG"),
              ),
              Card(
                child: Image.asset("assets/ima1.JPG"),
              ),
            ],
          )),
      floatingActionButton: FloatingActionButton(
        child: const Icon(Icons.accessibility_new),
        onPressed: () {},
      ),
      backgroundColor: const Color.fromARGB(255, 75, 76, 84),
      appBar: AppBar(
        backgroundColor: const Color.fromARGB(255, 17, 148, 113),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(30)),
        title:  const Text("Material App"),
        // actions: <Widget>[
        //   IconButton(onPressed: _add, icon: Icon(Icons.accessible_sharp))
        // ]
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.end,
        children: [
          const Center(
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
          const Icon(size: 100, Icons.favorite),
          IconButton(
              iconSize: 100,
              onPressed: () {
                print("hola");
              },
              icon: const Icon(Icons.favorite_border)),
          GestureDetector(
            onDoubleTap: () {
              Navigator.pushNamed(context, "/second");
              // _showSecondPage(context);
            },
            child: Container(
              color: Colors.pink.shade900,
              height: 100,
              width: 100,
              child: const Text(
                "Pagina 2",
                style: TextStyle(fontSize: 30),
              ),
            ),
          ),
          Row(
            children: <Widget>[
              const Expanded(child: Text("Activar sonido")),
              Switch(value: true, onChanged: (value) {}),
            ],
          ),
          const Divider(),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: <Widget>[
              const Text("Activar camara"),
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
                color:  const Color.fromARGB(255, 24, 148, 167),
                height: 50,
                width: 50,
              ),
              Container(
                color: const Color.fromARGB(100, 115, 41, 172),
                height: 100,
                width: 100,
              ),
              Container(
                color: const Color.fromARGB(100, 84, 12, 31),
                height: 50,
                width: 50,
              ),
              Container(
                color: const Color.fromARGB(255, 225, 225, 29),
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

  final List<String> _names = [
    "PEPE",
    "TOÑO",
    "PEPETOÑO",
    "PATRICIO",
    "JUAN",
    "BOLA",
    "BANANA",
    "DOS"
  ];

  //Este es un wigdet con imagenes de pato tierno infinitas
  Widget infinitIma() {
    return ListView.builder(
      itemCount: _names.length,
      itemBuilder: (context, index) {
        // final name = _names[index];
        return Card(
          child: Image.network(
              "https://avatars.githubusercontent.com/u/108163041?s=400&u=6c6af4a3b6c32023cde74120f69198ec3b401a4f&v=4"),
        );
      },
    );
  }

  // void _showSecondPage(BuildContext context) {
  //   // Esta forma no es la mas adecuada. L mas adecuada es hacer uso de rutas.
  //   final route = MaterialPageRoute(builder: (BuildContext context) {
  //     return SecondPage(key: key, name: "Dereck");
  //   });

  //   Navigator.of(context).push(route);

  //   // Navigator.of(context).pushNamed("/second", arguments: "Dereck");  //Esta forma es mas adecuada
  // }
}
