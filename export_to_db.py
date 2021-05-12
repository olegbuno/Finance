import csv, sqlite3

con = sqlite3.connect("finance.db")
cur = con.cursor()
cur.execute("CREATE TABLE ZM (Date, Open, High, Low, Close, AdjClose, Volume);") # use your column names here

with open('ZM.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['Date'], i['Open'], i['High'], i['Low'], i['Close'], i['AdjClose'], i['Volume'],) for i in dr]

cur.executemany("INSERT INTO ZM (Date, Open, High, Low, Close, AdjClose, Volume) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()