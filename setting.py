from tkinter import *
import pandas as pd


root = Tk()

data = pd.read_csv('data.csv', sep=',')


def click():
    juso = txt.get()
    gr = txt2.get()
    
    global data
    data.site[0] = juso
    data.local[0] = gr

    data.to_csv("data.csv")
 
lbl = Label(root, text="주소")
lbl.grid(row=0, column=0)
txt = Entry(root)
txt.grid(row=0, column=1)

lbl2 = Label(root, text="경로")
lbl2.grid(row=1, column=0)
txt2 = Entry(root)
txt2.grid(row=1, column=1)
 
btn = Button(root, text="OK", command = click)
btn.grid(row=2, column=1)
 
root.mainloop()

