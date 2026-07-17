# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: ExpenseSplit
def weekly_stats(self, transactions=None):
        """Calculate weekly statistics grouped by ISO week."""
        txs = transactions or self.transactions
        if not txs:
            return {}
        
        weekly_data = {}
        for tx in txs:
            date = tx.get("date")
            if not isinstance(date, datetime):
                continue
            
            iso_week = date.isocalendar()[1]  # ISO week number (year-agnostic)
            
            if iso_week not in weekly_data:
                weekly_data[iso_week] = {
                    "week": iso_week,
                    "total_amount": 0.0,
                    "transaction_count": 0,
                    "participants": set()
                }
            
            weekly_data[iso_week]["total_amount"] += tx.get("amount", 0)
            weekly_data[iso_week]["transaction_count"] += 1
            
            for participant in tx.get("participants", []):
                weekly_data[iso_week]["participants"].add(participant)
        
        return {week: data for week, data in weekly_data.items()}
