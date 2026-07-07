# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: ExpenseSplit
def export_to_json(self):
    """Экспортирует текущее состояние ExpenseSplit в JSON-строку."""
    import json as _json
    data = {
        "participants": self._participants,
        "categories": self._categories,
        "transactions": [
            {"id": t.id, "amount": t.amount, "payer_id": t.payer_id} for t in self._transactions
        ],
        "debts": self._debts,
        "balances": {uid: b.balance for uid, b in self._balances.items()},
    }
    return _json.dumps(data, indent=2)
