import functools
from datetime import datetime
from pathlib import Path

LOG_PATH = Path("Activity Log")

def log_action(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M;%S")
        result = func(*args, **kwargs)
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(f"{timestamp} ={func.__name__} called\n")
        return result
    return wrapper

def validate_expense(func):
    @functools.wraps(func)
    def wrapper(args):
        errors =[]

        try:
            amount = float(args.amount)
            if  amount<=0:
                errors.append("Amount  must be greater than zero")
        except ValueError:
            errors.append(f"{args.amount}' is not a valid number")

        if not args.category.strip():
            errors.append("Category cannot be empty")

        if not  args.note.strip():
            errors.append("note cannot be empty")

        if errors:
            for e in errors:
                print(f" error: {e}")
            return
        
        return func(args)
    
    return wrapper 
