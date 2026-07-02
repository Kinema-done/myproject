# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: ExpenseSplit
def run_cli():
    print("=== ExpenseSplit CLI ===")
    while True:
        cmd = input("\nКоманда (1-4, q=выход): ").strip().lower()
        if cmd == 'q': break
        elif cmd in ('1', '2', '3', '4'):
            print(f"Выполнение команды {cmd}...")
        else:
            print("Неизвестная команда.")
