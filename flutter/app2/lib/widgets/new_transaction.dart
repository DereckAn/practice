import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

class NewTransaction extends StatefulWidget {
  final Function addTx;
  const NewTransaction(this.addTx, {super.key});

  @override
  State<NewTransaction> createState() => _NewTransactionState();
}

class _NewTransactionState extends State<NewTransaction> {
  final titleController = TextEditingController();
  // Este es otro metodo de capturar el input y almacenarlo en una variable.
  final amountController = TextEditingController();
  DateTime _selectedDate = DateTime.now();

  void _submitData() {
    if (amountController.text.isEmpty) {
      return;
    }
    final enteredTitle = titleController.text;
    final enteredAmount = double.parse(amountController.text);

    if (enteredTitle.isEmpty || enteredAmount <= 0 || _selectedDate == null) {
      // Esto es para que no agrege nuevos objetos si esta vacio o si tiene un valor negativo
      return;
    }

    widget.addTx(enteredTitle, enteredAmount, _selectedDate);

    Navigator.of(context)
        .pop(); // Esto es para cerrar al finalizar de añadir un nuevo objeto a la lista
  }

  void _presentDate() {
    showDatePicker(
            context: context,
            firstDate: DateTime(2019),
            initialDate: DateTime.now(),
            lastDate: DateTime.now())
        .then((pickedDate) {
      if (pickedDate == null) {
        return;
      }
      setState(() {
        _selectedDate = pickedDate;
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: Card(
          child: Container(
        padding: EdgeInsets.only(
            top: 10,
            left: 10,
            right: 10,
            bottom: MediaQuery.of(context).viewInsets.bottom + 10),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.end,
          children: <Widget>[
            TextField(
              decoration: const InputDecoration(labelText: "Title"),
              controller:
                  titleController, // Esto es otra manera de guardar el input.
              // onChanged: (value) => titleInput =// Esto es para guardar nuestro input en una variable. Este solo es un metodo para hacerlo
              //     value
            ),
            TextField(
              decoration: const InputDecoration(labelText: "Amount"),
              keyboardType: const TextInputType.numberWithOptions(
                  decimal: true), // Esto es para cambiar el tipo teclado
              controller: amountController,
              onSubmitted: (_) =>
                  _submitData(), // Aprende esto. Es para que el teclado agrege la cantidad y el titulo cuando apachurras el simbolode " listo" en el teclado
              // onChanged: (value) => amounInput = // Esto es para guardar nuestro input en una variable. Este es solo un metodo para hacerlo
              //     value
            ),
    
            SizedBox(
              height: 70,
              child: Row(
                children: <Widget>[
                  Expanded(
                      child: Text(_selectedDate == null
                          ? "No date Chosen!!"
                          : 'Day Selected: ${DateFormat.yMd().format(_selectedDate)}')),
                  TextButton(
                    onPressed: _presentDate,
                    child: const Text(
                      "Choose Date",
                      style: TextStyle(fontWeight: FontWeight.bold),
                    ),
                  )
                ],
              ),
            ),
            ElevatedButton(
              onPressed: () {
                // print(titleInput);
                // print(amounInput);
                // print(titleController.text);
                // print(amountController.text);
                // addTx(titleController.text, double.parse(amountController.text));
                _submitData();
              },
              child: const Text(
                "Add Transaction",
                style: TextStyle(
                    color: Color.fromARGB(255, 66, 21, 74),
                    fontWeight: FontWeight.bold),
              ),
            ) // TextFiel es responsable de recibir texto del usuario. como si fuera un input en python.
          ],
        ),
      )),
    );
  }
}
