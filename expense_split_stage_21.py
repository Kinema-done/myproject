# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: ExpenseSplit
class Reminder:
    def __init__(self, text, due_date):
        self.text = text
        self.due_date = due_date
    
    @property
    def is_overdue(self):
        return datetime.now() > self.due_date


def add_reminder(text, due_date_str):
    reminder = Reminder(text, due_date_str)
    reminders.append(reminder)
    print(f"Напоминание добавлено: '{text}' до {due_date_str}")


def show_reminders():
    if not reminders:
        print("Нет назначенных напоминаний.")
        return
    
    for r in sorted(reminders, key=lambda x: x.due_date):
        status = "⚠️ ПРОСРОЧЕНО" if r.is_overdue else f"📅 До {r.due_date}"
        print(f"- {status}: {r.text}")
