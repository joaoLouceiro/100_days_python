
import sqlite3

# Ao criar uma conexão, a BD é automaticamente adicionada ao nosso projeto
db = sqlite3.connect("books-collection.db")

# O cursor é responsável pela interação com a BD
cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()