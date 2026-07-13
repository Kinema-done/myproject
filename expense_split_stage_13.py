# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: ExpenseSplit
def search(self, query: str) -> list[Record]:
        """Поиск записей по нескольким полям без учёта регистра."""
        results = []
        q_lower = query.lower()
        for rec in self._records:
            if (q_lower in rec["name"].lower() or
                q_lower in rec["category"].lower() or
                q_lower in rec["description"].lower()):
                results.append(rec)
        return results
