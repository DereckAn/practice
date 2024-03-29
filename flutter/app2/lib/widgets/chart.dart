import 'package:app2/models/transaction.dart';
import 'package:app2/widgets/chart_bar.dart';
import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

class Chart extends StatelessWidget {
  final List<Transaction> recentTransactions;

  const Chart(this.recentTransactions, {super.key});

  List<Map<String, Object>> get groundTransactionValues {
    return List.generate(7, (index) {
      final weekDay = DateTime.now().subtract(Duration(days: index));
      double totalSum = 0.0;
      // for (var i = 0; i < recentTransactions.length; i++) {
      //   // hay ptra manera de poner el "for"  for( var tx in recentTransactions )
      //   if (recentTransactions[i].date.day == weekDay.day &&
      //       recentTransactions[i].date.month == weekDay.month &&
      //       recentTransactions[i].date.year == weekDay.year) {
      //     totalSum += recentTransactions[i].amount;
      //   }
      // }
      for (var tx in recentTransactions) {
        if (tx.date.day == weekDay.day &&
            tx.date.month == weekDay.month &&
            tx.date.year == weekDay.year) {
          totalSum += tx.amount;
        }
      }

      // print(DateFormat.E().format(weekDay));
      // print(totalSum);
      return {
        'day': DateFormat.E().format(weekDay).substring(0, 1),
        'amount': totalSum
      };
    }).reversed.toList();
  }

  double get totalSpending {
    return groundTransactionValues.fold(0.0, (sum, item) {
      // investigar la funcion fold
      return sum + (item['amount'] as double);
    });
  }

  @override
  Widget build(BuildContext context) {
    print(groundTransactionValues);
    return Card(
      elevation: 6,
      margin: const EdgeInsets.all(20),
      child: Padding(
        padding: const EdgeInsets.all(10),
        child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: groundTransactionValues.map((data) {
              return Flexible(
                fit: FlexFit.tight,
                child: CharBar(
                    data['day'] as String,
                    data['amount']
                        as double, //  que no se te olbide cast los datos
                    totalSpending == 0.0
                        ? 0.0
                        : (data["amount"] as double) / totalSpending),
              );
            }).toList()),
      ),
    );
  }
}
