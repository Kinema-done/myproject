# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: ExpenseSplit
def delete_record(record_id, table_name):
    if not record_id:
        raise ValueError("ID записи не может быть пустым")
    if not table_name or table_name not in TABLES:
        raise KeyError(f"Таблица {table_name} не найдена или недоступна для удаления")
    records = get_table(table_name)
    for i, record in enumerate(records):
        if record.get('id') == str(record_id):
            del records[i]
            return True
    return False

def delete_by_category(category_id, table_name='expenses'):
    if not category_id:
        raise ValueError("ID категории не может быть пустым")
    categories = get_table('categories')
    expenses = get_table(table_name)
    valid_ids = [str(c['id']) for c in categories if str(c.get('id')) == str(category_id)]
    filtered_expenses = [e for e in expenses if e.get('categoryId') not in valid_ids]
    return filtered_expenses

def delete_debt(debtor_name, table_name='debts'):
    debts = get_table(table_name)
    updated_debts = [d for d in debts if str(d.get('debtorName')) != debtor_name]
    return updated_debts
