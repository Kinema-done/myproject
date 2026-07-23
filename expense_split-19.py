# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: ExpenseSplit
def archive_old_records(records, cutoff_days=365):
    """Archive records older than `cutoff_days` days into a separate list."""
    from datetime import datetime, timedelta
    today = datetime.now()
    cutoff = today - timedelta(days=cutoff_days)
    archived = []
    active = []
    for rec in records:
        created = rec.get("created_at") or rec.get("timestamp")
        if isinstance(created, str):
            created = datetime.fromisoformat(created.replace("Z", "+00:00"))
        elif isinstance(created, datetime):
            pass
        else:
            continue
        if created < cutoff:
            archived.append(rec)
        else:
            active.append(rec)
    return active, archived
