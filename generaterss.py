from tkinter import *
import os

def generatetext(a,b,c):
    s=""
    s="<lastBuildDate>"
    s=s+str(c)
    s=s+" GMT</lastBuildDate>"
    s=s+"</item>"
    s=s+"<item>"
    s=s+"<title>"+str(a)+"</title>"
    s=s+"<description>"+str(b)+"</description> "
    s=s+"<pubDate>"+str(c)+" GMT</pubDate>"
    s=s+"</item>"
    print(s)
    
def show_entry_fields():
   import datetime
   now = datetime.datetime.now() 
   from datetime import datetime
   time=datetime.utcnow()
   #print(time)
   generatetext(e1.get(),e2.get(),time)
   #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = Tk()
Label(master, text="Title").grid(row=0)
Label(master, text="Description").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
