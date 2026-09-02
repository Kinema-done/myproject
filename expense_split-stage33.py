# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: ExpenseSplit
class ActionHistory:
    """Records undoable operations and supports rollback."""
    
    def __init__(self):
        self._history = []
        self._undo_stack = []
    
    def record(self, action):
        self._history.append(action)
        self._undo_stack.append(action)
    
    def undo(self):
        if self._undo_stack:
            return self._undo_stack.pop()
        return None
    
    def clear_undo(self):
        self._undo_stack.clear()
    
    def get_history(self):
        return list(self._history)
