import gspread
from datetime import date

def add_expense_to_sheet(googlesheet_id, category, price, comment):
    gc = gspread.service_account()
    today = date.today().strftime("%d.%m.%Y")
    sh = gc.open_by_key(googlesheet_id)
    sh.sheet1.append_row([today, category, price, comment])