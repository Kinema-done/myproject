# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: ExpenseSplit
APP_CONFIG = {
    "app_name": "ExpenseSplit",
    "version": "1.0.0",
    "currency": "USD",
    "max_debt_per_person": 50.0,
    "default_category": "misc",
    "logging": {
        "enabled": True,
        "level": "INFO",
        "file": "expenses.log"
    },
    "validation": {
        "allow_negative_amount": False,
        "allow_empty_participant": False,
        "min_amount": 0.01
    },
    "ui": {
        "decimal_places": 2,
        "separator": ","
    }
}


def get_config(key, default=None):
    if key not in APP_CONFIG:
        raise KeyError(f"Unknown config key: {key}")
    return APP_CONFIG[key]


def update_config(key, value):
    if key not in APP_CONFIG:
        raise KeyError(f"Unknown config key: {key}")
    APP_CONFIG[key] = value


def reset_config():
    APP_CONFIG["logging"]["enabled"] = True
    APP_CONFIG["logging"]["level"] = "INFO"
    APP_CONFIG["validation"]["allow_negative_amount"] = False
    APP_CONFIG["validation"]["allow_empty_participant"] = False
    APP_CONFIG["validation"]["min_amount"] = 0.01
    APP_CONFIG["ui"]["decimal_places"] = 2
    APP_CONFIG["ui"]["separator"] = ","
