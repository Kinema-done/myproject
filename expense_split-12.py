# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: ExpenseSplit
def load_from_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("JSON root must be an object")
        return data
    except FileNotFoundError:
        print(f"Файл не найден: {filepath}")
        return None
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return None
