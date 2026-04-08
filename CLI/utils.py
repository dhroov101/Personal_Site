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

