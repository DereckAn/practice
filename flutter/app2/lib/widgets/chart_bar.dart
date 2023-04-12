import 'package:flutter/material.dart';

class CharBar extends StatelessWidget {
  final String label;
  final double spendingAmount;
  final double spendingPctOfTotal;

  const CharBar(this.label, this.spendingAmount, this.spendingPctOfTotal,
      {super.key});

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (ctx, constraint){
      return Column(
        children: <Widget>[
          SizedBox(
            height: constraint.maxHeight * 0.15,
            child: FittedBox( // este widget forza a su hijo adentro del espacio disponible
                child: Text(
                    "\$${spendingAmount.toStringAsFixed(1)}")),
          ), // esta parte es para redondear
          SizedBox(height: constraint.maxHeight * 0.05),
          SizedBox(
            height: constraint.maxHeight * 0.6,
            width: 10,
            child: Stack(
              children: <Widget>[
                Container(
                  decoration: BoxDecoration(
                    border: Border.all(color: Colors.grey, width: 1.0),
                    color: const Color.fromARGB(124, 135, 127, 127),
                    borderRadius: BorderRadius.circular(10),
                  ),
                ),
                FractionallySizedBox(
                  heightFactor: spendingPctOfTotal,
                  child: Container(
                    decoration: BoxDecoration(
                      color: Theme.of(context).primaryColor,
                      borderRadius: BorderRadius.circular(10),
                    ),
                  ),
                ),
              ],
            ),
          ),
          SizedBox(height: constraint.maxHeight * 0.05),
          SizedBox(height: constraint.maxHeight * 0.15,
            child: FittedBox(child: Text(label))),
        ],
      );
    },);
  }
}
