# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: ExpenseSplit
import shutil, os, json, datetime

def backup_data_file(data_file_path, backup_dir=None):
    if backup_dir is None:
        backup_dir = os.path.join(os.path.dirname(data_file_path), "backups")
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, os.path.basename(data_file_path) + f".{timestamp}")
    shutil.copy2(data_file_path, backup_path)
    return backup_path
