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
                         
     