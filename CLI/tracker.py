import argparse
from expenses import load_expenses, save_expenses, Expense, filter_by_category, filter_by_date, summarize_by_category
from utils import log_action, validate_expense

@log_action
@validate_expense
def cmd_add(args):
    expenses= load_expenses()
    new = Expense(
        amount=float(args.amount),
        category=args.category,
        note= args.note,
    )
    expenses.append(new)
    save_expenses(expenses)
    print(f"Added {new}")

@log_action
def cmd_list(args):
    expenses=load_expenses()
    if not expenses:
        print("No expenses yet")
        return 
    for e in expenses:
        print(e)

@log_action
def cmd_filter(args):
    expenses=load_expenses()
    results = filter_by_category(expenses, args.category)
    if not results:
        print( f"No expenses in this category { args.category}")
        return 
    for e in results:
        print(e)

@log_action
def cmd_summary(args):
    expenses= load_expenses()
    if not expenses:
        print("No expesnes yet")
        return
    summary = summarize_by_category(expenses)
    print(f"\n{'Category':<15} {'Total':>8}")
    print("-" * 25)
    for cat, total in sorted(summary.items()):
        print(f"{cat:<15} €{total:>7.2f}")
    print("-" * 25)
    print(f"{'Total':<15} €{sum(summary.values()):>7.2f}")


def main():

    parser = argparse.ArgumentParser(description="Expense Tracker")
    sub = parser.add_subparsers(dest='command')

    add_p = sub.add_parser("add", help="Add new expense")
    add_p.add_argument("amount")
    add_p.add_argument("category")
    add_p.add_argument("note")
    sub.add_parser("summary", help="Summarise by category")

    
    filter_p = sub.add_parser("filter", help="Filter by category")
    filter_p.add_argument("category")

    sub.add_parser("list", help='List all expenses')

    args= parser.parse_args()

    if args.command =="add":
        cmd_add(args)
    elif args.command =="list":
        cmd_list(args)
    elif args.command == "filter":
        cmd_filter(args)
    elif args.command == "summary":
        cmd_summary(args)
    
    else:
        parser.print_help()
        
    expenses = load_expenses()




    
if __name__ == '__main__':
    main()
