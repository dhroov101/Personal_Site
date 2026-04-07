from expenses import load_expenses, save_expenses, Expense
def main():
    expenses = load_expenses()


    expenses.append(Expense(amount=12.50, category="food", note="lunch"))
    expenses.append(Expense(amount=3.20,  category="transport", note="bus"))


    save_expenses(expenses)

    reloaded = load_expenses()
    for e in reloaded:
        print(e)
    
if __name__ == '__main__':
    main()
