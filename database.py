import sqlite3

db = sqlite3.connect(":memory:")
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS Работник (
   id INT PRIMARY KEY,
   name TEXT,
   surname TEXT,
   gender TEXT,
   age INT);
""")

db.commit()

sql.execute("""CREATE TABLE IF NOT EXISTS Зарплата (
   id INT PRIMARY KEY,
   reward INT,
   currency TEXT);
""")

db.commit()

sql.execute("""CREATE TABLE IF NOT EXISTS Должность (
   id INT PRIMARY KEY,
   position TEXT,
   exp TEXT);
""")

db.commit()

worker = [('1', 'James', 'Bond', 'Male', '50'), ('2', 'Peter', 'Parker', 'Male', '20')]
sql.executemany("INSERT INTO Работник VALUES (?, ?, ?, ?, ?);", worker)
db.commit()
salary = [('1', '50000', 'EUR'), ('2', '1500', 'USD')]
sql.executemany("INSERT INTO Зарплата VALUES (?, ?, ?);", salary)
db.commit()
position = [('1', 'Killer', '25 years'), ('2', 'Hero', '2 years')]
sql.executemany("INSERT INTO Должность VALUES (?, ?, ?);", position)
db.commit()
sql.execute("SELECT * FROM Работник;")
results = sql.fetchall()
print(results)
sql.execute("SELECT * FROM Зарплата;")
results = sql.fetchall()
print(results)
sql.execute("SELECT * FROM Должность;")
results = sql.fetchall()
print(results)