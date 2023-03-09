// Esta clase no tiene widgets solo es para que guarde unos datos. 
class Transaction {
  //Attributes or Properties
  final String id;
  final String title;
  final double amount;
  final DateTime date;

  Transaction({required this.id, required this.title, required this.amount, required this.date});
}
