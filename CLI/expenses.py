from dataclasses import dataclass, field
from datetime import date as Date
import csv
from pathlib import Path

@dataclass 
class Expense:
    amount: float
    category: str
    note: str
    date: Date = field(default_factory=Date.today)

    def to_row(self) -> list:
        return [str(self.date), self.category, self.note, str(self.amount)]
    

    @classmethod
    def from_row(cls, row:list) -> "Expense":
        return cls (
            date = Date.fromisoformat(row[0]),
            category = row[1],
            note = row[2],
            amount = float(row[3])
        )
    
    def __str__(self) -> str:
        return f"{self.date} | {self.category} | {self.note} | {self.amount}"

CSV_PATH = Path("expenses.csv")
HEADERS = ["date", "category", "note", "amount"]

def load_expenses() -> list[Expense]:
    if not CSV_PATH.exists():
        return []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        return [Expense.from_row(row) for row in reader if row]
    
def save_expenses(expenses: list[Expense]) -> None:
    with open(CSV_PATH,"w", newline="", encoding="utf-8") as f:
        writer= csv.writer(f)
        writer.writerow(HEADERS)
        writer.writerows([e.to_row() for e in expenses])
                         
def filter_by_category(expenses: list[Expense], category: str) -> list[Expense]:
    return [e for e in expenses if e.category.lower() == category.lower()]

def filter_by_date(expenses: list[Expense], start: Date, end: Date) -> list[Expense]:
    return [e for e in expenses if start <= e.date <= end]   

def summarize_by_category(expenses : list[Expense]) -> dict[str, float]:
    categories = {e.category.lower() for e in expenses}
    return  {
        cat: round(sum(e.amount for e in expenses if e.category.lower() == cat), 2)
        for cat in categories

    }  

class CSVManager:
    def __init__(self, path: Path, mode: str = "r"):
        self.path = path
        self.mode = mode
        self._file = None

    def __enter__(self):
        self._file = open(self.path, self.mode, newline="", encoding="utf-8")
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._file:
            self._file.close()
        if exc_type is not None:
            print(f"  file error: {exc_val}")
            return True  # suppress the exception
        return False