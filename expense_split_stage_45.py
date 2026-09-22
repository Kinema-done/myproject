# === Stage 45: Добавь восстановление из резервной копии ===
# Project: ExpenseSplit
def restore_backup(source_path, target_path=None):
    """Восстанавливает данные из резервной копии JSON-файла.
    source_path — путь к файлу с бэкапом.
    target_path — путь, куда записать восстановленные данные (по умолчанию в source_path).
    Возвращает True если восстановление прошло успешно, иначе False.
    """
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            backup_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, PermissionError):
        return False

    if target_path is None:
        target_path = source_path

    try:
        with open(target_path, 'w', encoding='utf-8') as f:
            json.dump(backup_data, f, indent=2, ensure_ascii=False)
        return True
    except (PermissionError, OSError):
        return False
