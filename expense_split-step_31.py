# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: ExpenseSplit
# --- ExpenseSplit - Этап 31: Переключение активного профиля ---

class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"User({self.name}, balance={self.balance})"

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


class ExpenseSplit:
    # ... (existing code) ...

    def __init__(self):
        self.users = {}
        self.active_user = None
        self.history = []

    def add_user(self, name, balance=0):
        user = User(name, balance)
        self.users[name] = user
        return user

    def switch_user(self, name):
        if self.active_user and self.active_user.name == name:
            return
        if name not in self.users:
            self.add_user(name)
        self.active_user = self.users[name]
        return self.active_user

    def add_expense(self, amount, category, description=""):
        if not self.active_user:
            raise ValueError("Нет активного пользователя")
        self.history.append({
            "amount": amount,
            "category": category,
            "description": description,
            "user": self.active_user.name,
            "balance": self.active_user.balance
        })
        self.active_user.balance -= amount
        return self.history[-1]
