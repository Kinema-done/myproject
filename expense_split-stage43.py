# === Stage 43: Добавь пагинацию длинных списков ===
# Project: ExpenseSplit
def paginate(items, page_size=20):
    """Yield chunks of items for pagination."""
    for start in range(0, len(items), page_size):
        yield items[start:start + page_size]
