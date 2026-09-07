# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: ExpenseSplit
import json

def repair_data(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        return {'status': 'error', 'message': 'Файл не найден'}
    except json.JSONDecodeError:
        return {'status': 'error', 'message': 'Некорректный JSON'}
    errors = []
    if isinstance(data, dict):
        for key in ['participants', 'expenses', 'debts']:
            if key not in data:
                errors.append(f'Отсутствует обязательное поле: {key}')
                continue
            if not isinstance(data[key], list):
                errors.append(f'Поле {key} должно быть списком')
                continue
            if data[key] and not all(isinstance(item, dict) for item in data[key]):
                errors.append(f'Элементы {key} должны быть словарями')
    if errors:
        return {'status': 'error', 'message': '; '.join(errors)}
    return {'status': 'ok', 'message': 'Данные целостны'}

def repair_simple(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return {'status': 'error', 'message': 'Файл не найден'}
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        return {'status': 'error', 'message': 'Некорректный JSON'}
    if 'participants' not in data:
        data['participants'] = []
    if 'expenses' not in data:
        data['expenses'] = []
    if 'debts' not in data:
        data['debts'] = []
    for key in ['participants', 'expenses', 'debts']:
        if data[key] and not isinstance(data[key][0], dict):
            data[key] = [{} for _ in data[key]]
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return {'status': 'ok', 'message': 'Данные отремонтированы'}
