# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: ExpenseSplit
import json, random, uuid
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Optional

@dataclass
class Participant:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    balance: float = 0.0

@dataclass
class Expense:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    category: str = "Продукты"
    amount: float = 0.0
    date: date = None
    participants: list[str] = field(default_factory=list)

def generate_demo_data() -> dict:
    now = date.today()
    p1, p2, p3 = Participant("p1", "Алексей"), Participant("p2", "Мария"), Participant("p3", "Дмитрий")
    expenses = [
        Expense(category="Супермаркет", amount=500.0, date=now - timedelta(days=1), participants=["p1", "p2"]),
        Expense(category="Ресторан", amount=1200.0, date=now - timedelta(days=3), participants=["p1", "p2", "p3"]),
    ]
    return {"participants": [p1, p2, p3], "expenses": expenses}

if __name__ == "__main__":
    demo = generate_demo_data()
    print(json.dumps(demo, indent=2, default=str))
