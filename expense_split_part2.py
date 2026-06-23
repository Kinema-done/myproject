# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: ExpenseSplit
class ExpenseSplit:
    def __init__(self):
        self.participants = {}
        self.expenses = []
        self.debts = []
        self.history = []

    def add_participant(self, name: str) -> None:
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Имя участника должно быть непустой строкой.")
        self.participants[name] = {"balance": 0.0}

    def add_expense(self, amount: float, payer: str, category: str, participants: list[str]) -> None:
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сумма должна быть положительным числом.")
        if payer not in self.participants:
            raise ValueError(f"Оплата от участника '{payer}' не найдена.")
        for p in participants:
            if p not in self.participants:
                raise ValueError(f"Участник '{p}' не найден в списке.")
        share = amount / len(participants)
        payer_balance_change = -amount + share
        others_share = (len(participants) - 1) * share
        for i, p in enumerate(participants):
            if p != payer:
                self.participants[p]["balance"] += share
            else:
                self.participants[p]["balance"] -= amount
        self.expenses.append({
            "amount": round(amount, 2),
            "payer": payer,
            "category": category,
            "participants": participants,
            "share": round(share, 2)
        })
        self.history.append(f"Расход {round(amount, 2)} руб. ({category}) от {payer} на: {', '.join(participants)}.")

    def add_debt(self, creditor: str, debtor: str, amount: float) -> None:
        if not isinstance(creditor, str) or not isinstance(debtor, str):
            raise ValueError("Имена кредитора и должника должны быть строками.")
        if creditor == debtor:
            raise ValueError("Кредитор и должник не могут совпадать.")
        if creditor not in self.participants or debtor not in self.participants:
            raise ValueError("Участники не найдены.")
        if amount <= 0:
            raise ValueError("Сумма долга должна быть положительной.")
        self.debts.append({
            "creditor": creditor,
            "debtor": debtor,
            "amount": round(amount, 2)
        })
        self.participants[creditor]["balance"] += amount
        self.participants[debtor]["balance"] -= amount

    def validate_input(self, data: dict) -> list[str]:
        errors = []
        if not isinstance(data.get("amount"), (int, float)) or data["amount"] <= 0:
            errors.append("Некорректная сумма.")
        if not isinstance(data.get("payer"), str) or len(data["payer"].strip()) == 0:
            errors.append("Некорректное имя плательщика.")
        return errors
