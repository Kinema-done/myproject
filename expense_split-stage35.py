# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: ExpenseSplit
def suggest_next_actions(state: dict) -> list[str]:
    """Generate next-step recommendations based on current project state."""
    actions = []
    if "modules" not in state:
        actions.append("Define core modules: models, services, repository, views")
    elif state.get("modules", {}).get("models") != "done":
        actions.append("Implement ExpenseSplit model with id, participants, categories, balances, history")
    elif state.get("modules", {}).get("services") != "done":
        actions.append("Build calculation engine: split expenses by category, track debts, compute balances")
    elif state.get("modules", {}).get("repository") != "done":
        actions.append("Create SQLite-backed repository: CRUD for expenses, transactions, balances")
    elif state.get("modules", {}).get("views") != "done":
        actions.append("Implement CLI/text-based views: list expenses, show balance, generate reports")
    elif state.get("tests") != "done":
        actions.append("Write unit tests for models, services, and repository")
    elif state.get("docs") != "done":
        actions.append("Add README.md with setup instructions and usage examples")
    elif state.get("deployment") != "done":
        actions.append("Add requirements.txt and packaging config (pyproject.toml)")
    else:
        actions.append("Consider adding web UI (Flask/FastAPI) or mobile integration")
    return actions[:3]
