import sqlite3

def connect():
    conn=sqlite3.connect("Books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def viewall():
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store WHERE title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET title=?,author=?,year=?,isbn=? WHERE id=?", (title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
#insert("The moon","pramodh",1989,9997882)
#delete(3)
#update(4,"the ocean","harsha",2000,8464637)
#print(viewall())
