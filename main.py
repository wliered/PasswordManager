import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generatePassword():
    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password_entry.delete(0, tk.END)
    password="".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()

    fields_complete = len(website_text) >0 and len(email_text) >0 and len(password_text) >0

    if fields_complete:
        is_ok =messagebox.askokcancel(title=website_text,message=f"Do you want to save your password?\nEmail/Username: {email_text}\nPassword: {password_text}")
    else:
        messagebox.showerror(title=website_text,message=f"Please fill in all fields")
        return

    if is_ok:
        with open('password.txt', 'a') as file:
            file.write(website_text+"|"+email_text+"|"+password_text+"\n")
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.minsize(450, 400)
window.config(padx=50, pady=50)

logo_canvas = tk.Canvas(width=200, height=200)
logo_png = tk.PhotoImage(file="logo.png")
logo_canvas.create_image(100, 100, image=logo_png)
logo_canvas.grid(row=0, column=1)

website_label = tk.Label(window, text="Website:")
website_label.grid(row=1, column=0)

website_entry = tk.Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = tk.Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "pretendemail@email.com")

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = tk.Entry(width=22)
password_entry.grid(row=3, column=1)

generate_button = tk.Button(text="Generate Password", command=generatePassword)
generate_button.grid(row=3, column=2)

add_password_button = tk.Button(text="Add Password", width=34, command=save_password)
add_password_button.grid(row=4, column=1, columnspan=2)







window.mainloop()