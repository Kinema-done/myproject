# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: ExpenseSplit
TEMPLATES = {
    "dinner": {
        "label": "Обед",
        "category": "Обеды",
        "amount": 500,
        "participants": "all",
        "description": "Обед на всех"
    },
    "coffee": {
        "label": "Кофе",
        "category": "Кофе",
        "amount": 300,
        "participants": "all",
        "description": "Кофе"
    },
    "taxi": {
        "label": "Такси",
        "category": "Такси",
        "amount": 1200,
        "participants": "all",
        "description": "Такси"
    },
    "groceries": {
        "label": "Продукты",
        "category": "Продукты",
        "amount": 2000,
        "participants": "all",
        "description": "Покупки продуктов"
    },
    "rent": {
        "label": "Аренда",
        "category": "Аренда",
        "amount": 50000,
        "participants": "all",
        "description": "Аренда жилья"
    }
}

def apply_template(template_name, **overrides):
    """Apply a template to create a new record with optional overrides."""
    tpl = TEMPLATES.get(template_name)
    if not tpl:
        raise ValueError(f"Unknown template: {template_name}. Available: {list(TEMPLATES)}")
    record = {
        "label": tpl["label"],
        "category": tpl["category"],
        "amount": tpl["amount"],
        "participants": tpl["participants"],
        "description": tpl["description"],
        "template": template_name
    }
    record.update(overrides)
    return record
