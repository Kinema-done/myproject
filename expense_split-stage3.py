# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: ExpenseSplit
class ExpenseSplit:
    def __init__(self):
        self.participants = {}
        self.transactions = []
    
    def add_participant(self, name, balance=0):
        if not self.participants.get(name):
            self.participants[name] = {'balance': float(balance)}
    
    def record_transaction(self, payer_name, receiver_names, amount, category='general'):
        for receiver in receiver_names:
            if receiver not in self.participants:
                self.add_participant(receiver)
            if payer_name not in self.participants:
                self.add_participant(payer_name)
            
            transaction = {
                'id': len(self.transactions) + 1,
                'payer': payer_name,
                'receivers': receiver_names.copy(),
                'amount': float(amount),
                'category': category,
                'timestamp': __import__('datetime').datetime.now().isoformat()
            }
            
            self.participants[receiver]['balance'] += float(amount) / len(receiver_names)
            if payer_name != receiver:
                self.participants[payer_name]['balance'] -= float(amount) / len(receiver_names)
            
            self.transactions.append(transaction)
