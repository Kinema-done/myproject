# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: ExpenseSplit
import json, os

def save_to_file(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_from_file(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)
