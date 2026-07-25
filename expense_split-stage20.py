# === Stage 20: Добавь восстановление записей из архива ===
# Project: ExpenseSplit
def load_archive(path, *, delimiter=",", encoding="utf-8"):
    """Load expense records from a CSV-like archive file."""
    records = []
    with open(path, "r", encoding=encoding) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            fields = line.split(delimiter)
            if len(fields) != 6:
                print(f"Skipping malformed line: {line!r}")
                continue
            try:
                date_str, payer, category, amount, currency, notes = [s.strip() for s in fields]
                records.append({
                    "date": date_str,
                    "payer": payer,
                    "category": category,
                    "amount": float(amount),
                    "currency": currency or "",
                    "notes": notes or "",
                })
            except ValueError:
                print(f"Skipping invalid line: {line!r}")
    return records
