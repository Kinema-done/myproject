# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: ExpenseSplit
def check_overdue_reminders(self) -> List[Reminder]:
        """Возвращает список просроченных напоминений."""
        overdue = []
        for r in self.reminders:
            if r.done:
                continue
            deadline = datetime.fromisoformat(r.deadline).replace(tzinfo=datetime.now().astimezone().tzinfo)
            if datetime.now() > deadline:
                overdue.append(Reminder(reminder_id=r.id, text=f"[{r.title}] Просрочено на {timedelta(days=(datetime.now()-deadline).days)} дней", done=False))
        return overdue
