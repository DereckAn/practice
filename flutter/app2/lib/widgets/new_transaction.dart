import 'package:flutter/material.dart';

class NewTransaction extends StatelessWidget {
  final titleController =TextEditingController(); // Este es otro metodo de capturar el input y almacenarlo en una variable.
  final amountController = TextEditingController();
  final Function addTx;
 NewTransaction(this.addTx);

  @override
  Widget build(BuildContext context) {
    return Card(
        child: Container(
      padding: const EdgeInsets.all(10),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.end,
        children: <Widget>[
          TextField(
            decoration: const InputDecoration(labelText: "Title"),
            controller:titleController, // Esto es otra manera de guardar el input.
            // onChanged: (value) => titleInput =// Esto es para guardar nuestro input en una variable. Este solo es un metodo para hacerlo
            //     value
          ),
          TextField(
            decoration: const InputDecoration(labelText: "Amount"),
            controller: amountController,
            // onChanged: (value) => amounInput = // Esto es para guardar nuestro input en una variable. Este es solo un metodo para hacerlo
            //     value
          ),
          ElevatedButton(
            onPressed: () {
              // print(titleInput);
              // print(amounInput);
              print(titleController.text);
              print(amountController.text);
              addTx(titleController.text, double.parse(amountController.text));
            },
            child: const Text(
              "Add Transaction",
              style: TextStyle(color: Color.fromARGB(255, 66, 21, 74)),
            ),
          ) // TextFiel es responsable de recibir texto del usuario. como si fuera un input en python.
        ],
      ),
    ));
  }
}
