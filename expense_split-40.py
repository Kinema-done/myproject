# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: ExpenseSplit
import argparse

def main():
    parser = argparse.ArgumentParser(description="ExpenseSplit CLI")
    subparsers = parser.add_subparsers(dest="command")

    # balance
    bp = subparsers.add_parser("balance", help="Show current balances")
    bp.add_argument("--reset", action="store_true", help="Reset all balances")

    # settle
    sp = subparsers.add_parser("settle", help="Settle a debt")
    sp.add_argument("from_user", help="Debtor username")
    sp.add_argument("to_user", help="Creditor username")
    sp.add_argument("amount", type=float, help="Amount to settle")

    # export
    ep = subparsers.add_parser("export", help="Export to CSV")
    ep.add_argument("filename", help="Output CSV path")

    args = parser.parse_args()
    if args.command == "balance":
        if args.reset:
            for user in all_users:
                user.balance = 0.0
        print_balances()
    elif args.command == "settle":
        from_user = get_user(args.from_user)
        to_user = get_user(args.to_user)
        settle_debt(from_user, to_user, args.amount)
    elif args.command == "export":
        export_to_csv(args.filename)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
