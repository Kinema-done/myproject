# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: ExpenseSplit
import json, sys
from io import StringIO

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки."""
    try:
        data = json.loads(json_string)
        
        # Валидация обязательных полей
        required_fields = ['participants', 'expenses']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Отсутствует обязательное поле: {field}")
            
            # Проверка структуры участников
            for i, p in enumerate(data['participants']):
                if not isinstance(p, dict) or 'name' not in p:
                    raise ValueError(f"Неверная структура участника #{i+1}")
                
            # Проверка структуры расходов
            for i, e in enumerate(data['expenses']):
                required_expense_fields = ['amount', 'category', 'participants']
                if not all(field in e for field in required_expense_fields):
                    raise ValueError(f"Неверная структура расхода #{i+1}")
                
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Инициализация вспомогательных структур, если они отсутствуют в данных
    if 'categories' not in data:
        data['categories'] = {}
        
    return data

# Пример использования (раскомментируйте для тестирования):
if __name__ == "__main__":
    sample_json = """{
        "participants": [
            {"id": 1, "name": "Алексей", "balance": 0},
            {"id": 2, "name": "Мария", "balance": 0}
        ],
        "expenses": [
            {
                "amount": 500,
                "category": "Еда",
                "participants": [1, 2]
            }
        ]
    }"""
    
    loaded_data = load_initial_data(sample_json)
    print(f"Загружено участников: {len(loaded_data['participants'])}")
    print(f"Загружено расходов: {len(loaded_data['expenses'])}")
