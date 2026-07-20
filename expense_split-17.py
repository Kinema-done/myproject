# === Stage 17: Добавь группировку записей по категориям ===
# Project: ExpenseSplit
def __repr__(self):
        return (f"Transaction({self.amount}, {self.category}, "
                f"{self.date}, {self.description})")


def group_by_category(transactions: list) -> dict:
    result = {}
    for t in transactions:
        cat = t.category
        if cat not in result:
            result[cat] = []
        result[cat].append(t)
    return result
