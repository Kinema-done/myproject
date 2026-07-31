# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: ExpenseSplit
def format_entry(e: ExpenseEntry) -> str:
    parts = [f"[{e.id}] {e.date.strftime('%Y-%m-%d')} | {e.category.name}", f"  amount={e.amount:.2f} rub"]
    if e.paid_by and e.paid_by != e.for_whom:
        paid = e.paid_by.name if isinstance(e.paid_by, Person) else str(e.paid_by)
        for_whom = e.for_whom.name if isinstance(e.for_whom, Person) else str(e.for_whom)
        parts.append(f"  paid by {paid} for {for_whom}")
    if e.is_settled is not None:
        settled_str = "settled" if e.is_settled else "pending"
        parts.append(f"  status={settled_str}")
    return "\n".join(parts)

def print_entries(entries: list[ExpenseEntry], limit: int | None = None) -> str:
    out = []
    for i, e in enumerate(entries):
        if limit and i >= limit:
            break
        out.append(format_entry(e))
    return "\n".join(out)

def main():
    people = [Person("Alice"), Person("Bob")]
    cats = [Category("Food"), Category("Transport")]
    entries = []
    for p in people:
        entries.append(ExpenseEntry(amount=50, date=datetime.date.today(), paid_by=p, for_whom=people[1-p.id], category=cats[p.id % len(cats)]))

    print(print_entries(entries, limit=3))
