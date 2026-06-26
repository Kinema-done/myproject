# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: ExpenseSplit
def edit_transaction(txn_id: int, **kwargs) -> dict | None:
    if not kwargs:
        raise ValueError("Нужны хотя бы одно поле для обновления")
    txn = next((t for t in transactions if t['id'] == txn_id), None)
    if not txn:
        return None
    updated_fields = {k: v for k, v in kwargs.items() if k in ['amount', 'category', 'paid_by', 'status']}
    if updated_fields:
        txn.update(updated_fields)
    history.append({'action': 'edit', 'id': txn_id, 'timestamp': datetime.now(), 'fields': updated_fields})
    return txn
