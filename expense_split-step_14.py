# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: ExpenseSplit
def print_summary(data):
    if not data:
        return None
    total_expenses = sum(
        r["amount"] for r in data.get("expenses", [])
    )
    settled_amounts = [
        p["settled"] for p in data.get("participants", [])
    ]
    settlement_total = sum(settled_amounts)
    pending_settlements = []
    for i, p1 in enumerate(data.get("participants", [])):
        for j, p2 in enumerate(data.get("participants", [])):
            if i >= j:
                continue
            diff = round(p1["settled"] - p2["settled"], 2)
            if abs(diff) > 0.01:
                pending_settlements.append({
                    "from": p1["name"],
                    "to": p2["name"],
                    "amount": diff,
                })
    categories = {}
    for r in data.get("expenses", []):
        cat = r.get("category", "Other")
        categories[cat] = categories.get(cat, 0) + r["amount"]
    result = {
        "total_expenses": round(total_expenses, 2),
        "settled_by_participants": set(
            [round(p["settled"], 2) for p in data.get("participants", [])]
        ),
        "categories": categories,
        "pending_settlements": pending_settlements,
    }
    return result
