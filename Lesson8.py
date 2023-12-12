import sqlite3
 
conn = sqlite3.connect("phonebook.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
 
# Создание таблицы
cursor.execute("""CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, 
               name TEXT, 
               surname TEXT,
               number INTEGER)
               """)
conn.commit()

# Вставляем множество данных в таблицу используя безопасный метод "?"
users = [('1', 'Maria', 'Sucheva', '89230568741', ),
          ('2', 'Pavel', 'Malyk', '89645507777', ),
          ('3', 'Mihail', 'Kristoforov', '89547502358', ),
          ('4', 'Andrey', 'Karpushenkov', '89065584587', )]
 
cursor.executemany("INSERT INTO users VALUES (?,?,?,?)", users)
conn.commit()