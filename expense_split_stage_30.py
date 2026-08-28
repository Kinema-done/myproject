# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: ExpenseSplit
class Profile:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def add_money(self, amount):
        self.balance += amount
        return self

    def subtract_money(self, amount):
        self.balance -= amount
        return self

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, balance={self.balance:.2f})"


class Profiles:
    def __init__(self):
        self._profiles = {}

    def get_profile(self, name):
        return self._profiles.get(name)

    def create_profile(self, name, balance=0.0):
        if name in self._profiles:
            raise ValueError(f"Профиль с именем {name!r} уже существует")
        self._profiles[name] = Profile(name, balance)
        return self._profiles[name]

    def remove_profile(self, name):
        if name not in self._profiles:
            raise KeyError(f"Профиль {name!r} не существует")
        del self._profiles[name]
        return True

    def list_profiles(self):
        return [p for p in self._profiles.values()]

    def set_initial_balance(self, name, amount):
        p = self.get_profile(name)
        if p is None:
            raise KeyError(f"Профиль {name!r} не существует")
        p.balance += amount
        return p
