import 'package:app2/models/transaction.dart';
import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

class ListTrans extends StatelessWidget {
  final List<Transaction> list_tra;


  const ListTrans(this.list_tra);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: list_tra.map((tx) {
        // Aqui estamos generando los widgets que vayamos a necesitar. Con un map.
        return Card(
          child: Row(
            children: [
              Container(
                  margin:
                      const EdgeInsets.symmetric(vertical: 10, horizontal: 15),
                  decoration: BoxDecoration(
                      border: Border.all(
                    color: Colors.green,
                    width: 2,
                  )),
                  padding: const EdgeInsets.all(10),
                  // width: 60,
                  // height: 60,
                  // color: Colors.amber,  // no se pueden poner dos colores al mismo tiempo. Cuidado con eso.
                  child: Text(
                    "\$${tx.amount}", //this is string interpolation.  Es cuando usamos ${}  es como usamos el f"{}" en python. Pero para que podamos usar el symbolo de pesos normal tenemos que usar "\"
                    style: const TextStyle(
                        fontWeight: FontWeight.bold,
                        fontSize: 20,
                        color: Colors.purpleAccent),
                  )),
              Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text(
                  tx.id,
                  style:
                      const TextStyle(fontSize: 19, color: Colors.pinkAccent),
                ),
                Text(tx.title),
                Text(
                  DateFormat.yMd().add_jm().format(tx
                      .date), // Este es un paquete que importamos "intl" para modificar el formato de la fecha.
                  style: const TextStyle(color: Colors.grey),
                ),
              ]),
            ],
          ),
        );
      }).toList(),
    );
  }
}
