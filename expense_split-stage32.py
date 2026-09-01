# === Stage 32: Добавь журнал действий пользователя ===
# Project: ExpenseSplit
class ActionLog:
    def __init__(self):
        self.actions = []

    def log(self, action_type: str, details: str, actor: str = "unknown"):
        self.actions.append({"action_type": action_type, "details": details, "actor": actor})

    def get_last(self, limit: int = 10) -> list:
        return self.actions[-limit:]
