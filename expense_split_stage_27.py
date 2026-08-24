# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: ExpenseSplit
def reset_demo_data():
    """Сбросить демо-данные, очистив участников, категории, долги и историю."""
    global participants, categories, debts, history
    participants = []
    categories = []
    debts = []
    history = []
    print("Демо-данные сброшены.")


def clear_state():
    """Полная очистка состояния приложения."""
    reset_demo_data()
    print("Состояние полностью очищено.")
