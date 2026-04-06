import tkinter as tk # use foe GUI 
import random        # use for random choice
import pyperclip     # copy the things in the clipboard
from tkinter import messagebox      # show the message

window=tk.Tk()
window.title(" Advanced Password Generator")
window.geometry("400x700")
window.config(bg="#0F172A")
result_var=tk.StringVar()# data show in GUI

frame = tk.Frame(window, bg="#1E293B", padx=60, pady=80)
frame.pack(pady=30)

tk.Label(frame, text="🔐 Password Generator",bg="#1E293B", fg="#38BDF8",font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(frame,text="Enter the length",font=("Arial",14,"bold"),bg="#1E293B",fg="white").pack(pady=8)
length_entry=tk.Entry(frame,width=25)
length_entry.pack(pady=6)

var_uppercase=tk.IntVar()
tk.Checkbutton(frame, text="Include Uppercase",variable=var_uppercase,bg="#1E293B", fg="white",selectcolor="#334155",activebackground="#1E293B").pack(anchor="w",padx=20) 
var_lowercase=tk.IntVar()
tk.Checkbutton(frame,text="Include Lowercase",variable=var_lowercase, bg="#1E293B", fg="white",selectcolor="#334155",activebackground="#1E293B").pack(anchor="w",padx=20)
var_digits=tk.IntVar()
tk.Checkbutton(frame,text="Include Digits",variable=var_digits ,bg="#1E293B", fg="white",selectcolor="#334155",activebackground="#1E293B").pack(anchor="w",padx=20)
var_symbols=tk.IntVar()
tk.Checkbutton(frame,text="Include Symbols",variable=var_symbols, bg="#1E293B", fg="white",selectcolor="#334155",activebackground="#1E293B").pack(anchor="w",padx=20)

def generate_password():
    length_text=length_entry.get() # get take the value
    if not length_text.isdigit():
        messagebox.showerror("Error","Enter valid Number:")
        return
    length=int(length_text)

    chars=""
    if var_uppercase.get()==1:
        chars +="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if var_lowercase.get()==1:
        chars +="abcdefghijklmnopqrstuvwxyz"
    if var_digits.get()==1:
        chars +="0123456789"
    if var_symbols.get()==1:
        chars +="!@#$%^&*()"
    if chars == "":
        messagebox.showerror("Error","Select atleast one option")
        return
    
    password_list=[]
    if var_uppercase.get():
        password_list.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if var_lowercase.get():
        password_list.append(random.choice("abcdefghijklmnopqrstuvwxyz"))
    if var_digits.get():
        password_list.append(random.choice("0123456789"))
    if var_symbols.get():
        password_list.append(random.choice("!@#$%^&*()"))
    if length<len(password_list):
        messagebox.showerror("Error","Length too short for select options")
        return

    remaining= length - len(password_list)
    for i in range(remaining):
        password_list.append(random.choice(chars))

    random.shuffle(password_list) # shuffle the passward to make it random
    password="".join(password_list) # convert the list into string

    result_var.set(password)     # show the value
    length_entry.delete(0,tk.END)
   
def copy_password():
    password=result_var.get()
    if password=="":
        messagebox.showerror("Error","No password copied")
        return
    
    pyperclip.copy(password)
    messagebox.showinfo("Copied","password copied")
    result_var.set("")
    var_uppercase.set(0) # 0 means the box is unchecked
    var_lowercase.set(0)
    var_digits.set(0)
    var_symbols.set(0)
  
tk.Button(frame,text="Generate Password", command=generate_password,bg="#22C55E",fg="white",font=("Arial",12,"bold"),relief="flat",padx=10,pady=5).pack(pady=12)

tk.Label(frame,text="YOUR PASSWORD IS HERE",fg="#38BDF8",bg="#1E293B", font=("Arial",15,"bold")).pack(pady=10)
result_entry=tk.Entry(frame,textvariable=result_var,justify="center",width=25,font=("Arial",11,"bold")) # show the result in the entry 
result_entry.pack(pady=6) 

tk.Button(frame,text="Copy Passward", command=copy_password,bg="#22C55E",fg="white",font=("Arial",12,"bold"),relief="flat",padx=10,pady=5).pack(pady=12)

tk.mainloop()
