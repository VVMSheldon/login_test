import tkinter as tk
from tkinter import *
from tkinter import messagebox
import datumwaarde
    
def check_login():
    username = username_entry.get()
    password = password_entry.get()
    
    valid_username = "Sheldon Daal"
    valid_password = "1234"
    
    if username == valid_username and password == valid_password:
        messagebox.showinfo("Login Succesvol", "Welkom, " + username + "!")
        login_window.destroy()
        datumwaarde.init()
        #exec(open('datumwaarde.py').read())
    else: 
        messagebox.showerror("Login Mislukt!", "Ongeldige naam of password")

login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("500x320")


#username_label = tk.Label(window, text="Naam:")
#username_label.pack()

username_default_text = "Naam"
username_entry = tk.Entry(login_window, width=30, justify="center")
username_entry.insert(0,username_default_text)
username_entry.pack(pady=5)

#password_label = tk.Label(window, text="Password:")
#password_label.pack()

password_default_text = "Password"
password_entry = tk.Entry(login_window, width=30, justify="center",show='*')
password_entry.insert(0,password_default_text)
password_entry.pack(pady=5)

login_button = tk.Button(login_window, text="*")
password_entry.pack(pady=5)

login_button = tk.Button(login_window, text="Login", command=check_login)
login_button.pack(pady=10)

login_window.mainloop()        
