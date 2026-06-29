# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: ExpenseSplit
def filter_transactions(status=None, category=None, tags=None):
    filtered = []
    for t in transactions:
        if status and t.get('status') != status: continue
        if category and t.get('category') != category: continue
        if tags and not any(t.get(tag) == tag_value for tag, tag_value in tags.items()): continue
        filtered.append(t)
    return filtered

def get_summary_by_category(transactions):
    summary = {}
    for t in transactions:
        cat = t.get('category')
        amount = float(t.get('amount', 0))
        if cat not in summary: summary[cat] = {'total': 0, 'count': 0}
        summary[cat]['total'] += amount
        summary[cat]['count'] += 1
    return {k: list(v.values())[0] for k, v in sorted(summary.items(), key=lambda x: -x[1]['total'])}
