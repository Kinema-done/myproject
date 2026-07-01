# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: ExpenseSplit
def sort_transactions(transactions, key='date'):
    if not transactions: return []
    reverse = {'date': True, 'priority': False, 'name': False}.get(key, True)
    def _sort_key(t):
        val = t.get('date', 0) or (t.get('priority') or 0) * -1 or (t.get('name') or '').lower()
        return val if reverse else (-val if isinstance(val, int) else val.lower())
    return sorted(transactions, key=_sort_key)
