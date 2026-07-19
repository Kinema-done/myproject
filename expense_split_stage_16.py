# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: ExpenseSplit
def monthly_stats(self, since=None, until=None):
    """Расчёт месячной статистики: суммы расходов по месяцам."""
    if since is None or until is None:
        months = {}
        for entry in self.transactions:
            dt = entry.get('date', datetime.now())
            month_key = dt.strftime('%Y-%m')
            months[month_key] = months.get(month_key, 0) + entry.get('amount', 0)
    else:
        since_dt = datetime.strptime(since, '%Y-%m')
        until_dt = datetime.strptime(until, '%Y-%m')
        months = {}
        for entry in self.transactions:
            dt = entry.get('date', datetime.now())
            month_key = dt.strftime('%Y-%m')
            if since_dt <= dt.replace(day=1) < until_dt or (dt.replace(day=1) == since_dt and dt.replace(day=1) == until_dt):
                months[month_key] = months.get(month_key, 0) + entry.get('amount', 0)
    return dict(sorted(months.items()))

print("Monthly stats:", monthly_stats(self))
