# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: ExpenseSplit
import json, os

DEMO_DIR = "data/demo"

def run_demo():
    if not os.path.isdir(DEMO_DIR):
        print("No demo data found.")
        return
    for f in sorted(os.listdir(DEMO_DIR)):
        with open(os.path.join(DEMO_DIR, f), encoding="utf-8") as fh:
            data = json.load(fh)
        print(f"--- {f} ---")
        if isinstance(data, list):
            for item in data:
                print(json.dumps(item, ensure_ascii=False))
        else:
            print(json.dumps(data, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    run_demo()
