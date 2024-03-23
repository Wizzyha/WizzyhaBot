import gspread
gc = gspread.service_account()
sh = gc.open_by_key('1S4ksOdt7L49XS09Dm1xTxzDWSDD7UsfnKoTPeNigYPg')
print(sh.sheet1.get('A1:D1'))