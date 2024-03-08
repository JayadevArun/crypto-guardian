from tkinter import *
from tkinter import messagebox
import os
import base64

def encrypt():
    passwd=code.get()
    
    if passwd=="12345":
        screen1=Toplevel(screen)
        img_icon=PhotoImage(file="icon.png")
        screen1.iconphoto(False,img_icon)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")
        
        message=Text_1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")
        
        Label(screen1,text="ENCRYPT",fg="white",bg="#ed3833",font="arial").place(x=10,y=0)
        Text_2=Text(screen1,font="Robote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        Text_2.place(x=10,y=40,width=350,height=150)
        
        Text_2.insert(END,encrypt)
        
    elif passwd=="":
        messagebox.showerror("Encryption","Enter password")
        
    elif passwd!="12345":
        messagebox.showerror("Encryption","Invalid password")

def decrypt():
    passwd=code.get()
    
    if passwd=="12345":
        screen2=Toplevel(screen)
        img_icon=PhotoImage(file="icon.png")
        screen2.iconphoto(False,img_icon)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")
        
        message=Text_1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")
        
        Label(screen2,text="DECRYPT",fg="white",bg="#00bd56",font="arial").place(x=10,y=0)
        Text_2=Text(screen2,font="Robote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        Text_2.place(x=10,y=40,width=350,height=150)
        
        Text_2.insert(END,decrypt)
        
    elif passwd=="":
        messagebox.showerror("Decryption","Enter password")
        
    elif passwd!="12345":
        messagebox.showerror("Decryption","Invalid password")

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