# BOOK-STORE
An application using python 

//code
//frontend

from tkinter import *
import Backend

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])


def viewall_command():
    list1.delete(0,END)
    for row in Backend.viewall():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in Backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    list1.delete(0,END)
    Backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    Backend.delete(selected_tuple[0])



def update_command():
    Backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

window = Tk()
window.wm_title("BookStore")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)
l1=Label(window,text="Author")
l1.grid(row=0,column=2)
l1=Label(window,text="Year")
l1.grid(row=1,column=0)
l1=Label(window,text="ISBN")
l1.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,width=12,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,width=12,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,width=12,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,width=12,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=Listbox(window,height=12,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

list1.bind('<<ListboxSelect>>',get_selected_row)

scroll=Scrollbar(window)
scroll.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=scroll.set)
scroll.configure(command=list1.yview)

b1=Button(window,text="View all",width=12,command=viewall_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add",width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
  
  
//backend
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

    
    ![Untitled](https://user-images.githubusercontent.com/87749012/133541701-39d075fb-677f-40c2-8e91-ae1568ce728d.png)
