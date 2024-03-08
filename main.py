from tkinter import *
from tkinter import messagebox
import os
import base64
def main():
    global screen
    global Text_1
    global code
    
    screen=Tk()
    screen.geometry("400x400")
    
    img_icon=PhotoImage(file="icon.png")
    screen.iconphoto(False,img_icon)
    screen.title("App")
    
    def reset():
        code.set("")
        Text_1.delete(1.0,END)
    
    Label(text="Enter text:",fg="black",font=("calbri",15)).place(x=10,y=10)
    Text_1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    Text_1.place(x=10,y=50,width=350,height=100)
    
    Label(text="Enter secret key:",fg="black",font=("calbri",12)).place(x=10,y=170)
    
    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)
    
    Button(text="ENCRYPT",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200,y=250)
    Button(text="RESET",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)

    screen.mainloop()

main()