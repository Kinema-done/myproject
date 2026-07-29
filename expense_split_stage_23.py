# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: ExpenseSplit
def print_report(entries, participants):
    """Выводит отчёт в виде таблицы: кто, что оплатил, чей долг."""
    print(f"\n{'Участник':<20} {'Категория':<15} {'Сумма':>12} {'Кто платит':<20}")
    print("-" * 67)
    for e in entries:
        payer = "Я" if e.payee == "Я" else (e.payee if e.payee != "" else "?")
        print(f"{participants[e.payee]:<20} {e.category:<15} {f'{e.amount:.2f}':>12} {payer:<20}")

    total = sum(e.amount for e in entries)
    print("-" * 67)
    print(f"{'Всего:':<40} {total:>12.2f}")
