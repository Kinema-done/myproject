# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: ExpenseSplit
import unittest


class TestExpenseSplit(unittest.TestCase):
    def test_add_expense(self):
        from expense_split import ExpenseSplit
        app = ExpenseSplit()
        app.add_user("Alice")
        app.add_user("Bob")
        app.add_expense("Dinner", 100, "Alice", "Bob")
        assert app.get_balance("Alice") == -50
        assert app.get_balance("Bob") == 50

    def test_add_expense_with_category(self):
        from expense_split import ExpenseSplit
        app = ExpenseSplit()
        app.add_user("Alice")
        app.add_user("Bob")
        app.add_expense("Dinner", 100, "Alice", "Bob", category="Food")
        assert app.get_balance("Alice") == -50
        assert app.get_balance("Bob") == 50
        assert len(app.get_history()) == 1

    def test_get_balance_with_zero(self):
        from expense_split import ExpenseSplit
        app = ExpenseSplit()
        app.add_user("Alice")
        app.add_user("Bob")
        app.add_expense("Dinner", 100, "Alice", "Bob")
        assert app.get_balance("Alice") == -50
        assert app.get_balance("Bob") == 50
        assert app.get_balance("Alice", zero_balance=True) == 0
        assert app.get_balance("Bob", zero_balance=True) == 0

    def test_get_balance_with_minus(self):
        from expense_split import ExpenseSplit
        app = ExpenseSplit()
        app.add_user("Alice")
        app.add_user("Bob")
        app.add_expense("Dinner", 100, "Alice", "Bob")
        assert app.get_balance("Alice", zero_balance=False) == -50
        assert app.get_balance("Bob", zero_balance=False) == 50

    def test_get_balance_with_nonexistent_user(self):
        from expense_split import ExpenseSplit
        app = ExpenseSplit()
        app.add_user("Alice")
        app.add_user("Bob")
        app.add_expense("Dinner", 100, "Alice", "Bob")
        with self.assertRaises(ValueError):
            app.get_balance("Charlie")

    def test_get_balance_with_nonexistent_category(self):
        from expense_split import ExpenseSplit
        app = ExpenseSplit()
        app.add_user("Alice")
        app.add_user("Bob")
        app.add_expense("Dinner", 100, "Alice", "Bob")
        with self.assertRaises(ValueError):
            app.get_balance_category("Dinner", "Nonexistent")

    def test_get_balance_category_with_nonexistent_category(self):
        from expense_split import ExpenseSplit
        app = ExpenseSplit()
        app.add_user("Alice")
        app.add_user("Bob")
        app.add_expense("Dinner", 100, "Alice", "Bob")
        with self.assertRaises(ValueError):
            app.get_balance_category("Dinner", "Nonexistent")

    def test_get_balance_category_with_nonexistent_user(self):
        from expense_split import ExpenseSplit
        app = ExpenseSplit()
        app.add_user
