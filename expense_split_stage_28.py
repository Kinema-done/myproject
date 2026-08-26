# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: ExpenseSplit
def report_metrics(splits, categories, debts):
    if not splits:
        return {"total_spent": 0, "participants": set(), "categories_used": set(), "avg_per_person": 0, "unresolved_debts": 0}
    total = sum(s["amount"] for s in splits)
    participants = set(s["payer"] for s in splits) | set(s["receiver"] for s in splits)
    cats = set(s["category"] for s in splits)
    avg = total / len(participants) if participants else 0
    return {
        "total_spent": total,
        "participants": sorted(participants),
        "categories_used": sorted(cats),
        "avg_per_person": round(avg, 2),
        "unresolved_debts": sum(1 for d in debts if d["status"] != "cleared"),
    }
