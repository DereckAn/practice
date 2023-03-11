import 'package:flutter/material.dart';

class Mobetas extends StatelessWidget {
  const Mobetas({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      endDrawer: Drawer(
          child: Container(
        decoration: const BoxDecoration(
            image: DecorationImage(image: AssetImage("assets/ima4.jpg"))),
      )),
      appBar: AppBar(
        title: const Text(
          "Reward details",
          style: TextStyle(
              color: Color.fromARGB(150, 0, 0, 0),
              fontSize: 18,
              fontWeight: FontWeight.bold),
        ),
        backgroundColor: Colors.white,
        iconTheme: const IconThemeData(color: Color.fromARGB(172, 0, 0, 0)),
        centerTitle: true,
        // leading: const Icon(Icons.arrow_back_ios_new),
        leading: Builder(
            builder: (context) => IconButton(
                onPressed: () {
                  Navigator.pushNamed(context, '/second');
                },
                icon: const Icon(Icons.arrow_back_ios_new))),
      ),
      body: ListView(
        children: <Widget>[
          Container(
              color: Colors.pink,
              width: double.infinity,
              height: 190,
              child: Image.asset(
                "assets/ima3.jpg",
                fit: BoxFit.fill,
              )),
          Padding(
            padding: const EdgeInsets.all(25.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Container(
                  margin: const EdgeInsets.only(
                      left: 0, right: 0.0, top: 0.0, bottom: 50.0),
                  padding: const EdgeInsets.all(5),
                  color: Colors.pink[100],
                  child: const Text(
                    "EXPIRES MAR 30",
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      color: Color.fromARGB(143, 0, 0, 0),
                    ),
                  ),
                ),
                const Text(
                  "A Free mini plate",
                  style: TextStyle(
                      fontSize: 30,
                      fontWeight: FontWeight.bold,
                      color: Color.fromARGB(179, 0, 0, 0)),
                ),
                const Text(
                  "Includes: Mini plate- 2 choice, founder's favorite or mini chili palte)",
                  style: TextStyle(fontSize: 22, color: Colors.grey),
                ),
                const Text(
                  "This reward expired at 03/30/2023. View terms and conditions",
                  style: TextStyle(fontSize: 15, color: Colors.grey),
                ),
                Container(
                    width: double.infinity,
                    height: 20,
                    alignment: Alignment.center,
                    child: const Text("Need help with anything?",
                        style: TextStyle(
                          fontSize: 15,
                          color: Colors.grey,
                        ))),
              ],
            ),
          )
        ],
      ),
    );
  }
}
