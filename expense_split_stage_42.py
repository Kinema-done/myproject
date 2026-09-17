# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: ExpenseSplit
import sys

def colored(text, color=None):
    """Return ANSI-colored text, or plain if colors are disabled."""
    if colors_disabled:
        return text
    return f"\033[1;{30 + (color % 8) if color is not None else 39}m{text}\033[0m"

def set_color_state(enabled):
    global colors_disabled
    colors_disabled = not enabled

def main():
    print(colored("ExpenseSplit v0.42", color="green"))
    print(colored("Colors: enabled" if not colors_disabled else "Colors: disabled", color="yellow"))
    print("Type 'set_color_state(False)' to disable colors.")
    print("Type 'set_color_state(True)' to re-enable them.")
    print()
    print(colored("Participants:", color="cyan"))
    for p in participants:
        print(f"  - {colored(p, color='white')}")
    print()
    print(colored("Expenses:", color="magenta"))
    for e in expenses:
        print(f"  {colored(e['name'], color='white')}: {colored(str(e['amount']), color='green')}")
    print()
    print(colored("Settlements:", color="yellow"))
    for s in settlements:
        print(f"  {colored(s['name'], color='white')}: {colored(str(s['amount']), color='green')}")
    print()
    print(colored("Balance:", color="bold red"))
    print(f"  {colored(balance, color='white')}")

if __name__ == "__main__":
    main()
