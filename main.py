from tkinter import *
from tkinter import messagebox
import random

# --------------------------------- SAVE INPUTS ---------------------------------


def save_input():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == '' or username == '' or password == "":
        messagebox.showerror(title="Oops!",
                             message="Please don't leave any fields empty.")
    else:

        is_ok = messagebox.askokcancel(
            title=website, message=f"Details entered:\nUsername: {username}\nPassword: {password}\nAre you sure you want to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(
                    f"WEBSITE: {website} | USERNAME/EMAIL: {username} | PASSWORD: {password}\n")
            website_entry.delete(0, "end")
            username_entry.delete(0, "end")
            password_entry.delete(0, "end")
            website_entry.focus()


# --------------------------------- GENERATE PASSWORD ---------------------------------

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters)
                     for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols)
                      for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers)
                      for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, "end")
    password_entry.insert(0, password)


# --------------------------------- UI SETUP ---------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
app_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=app_logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
username_label = Label(text="Username:")
password_label = Label(text="Password:")

website_entry = Entry(width=35)
username_entry = Entry(width=35)
password_entry = Entry(width=21)

generate_pass_btn = Button(text="Generate", width=10, command=generate_pass)
save_pass_btn = Button(text="Save password", width=33, command=save_input)

website_label.grid(column=0, row=1)
website_entry.grid(column=1, columnspan=2, row=1)
website_entry.focus()
username_label.grid(column=0, row=2)
username_entry.grid(column=1, columnspan=2, row=2)
password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3)
generate_pass_btn.grid(column=2, row=3)
save_pass_btn.grid(column=1, columnspan=2, row=4)

window.mainloop()
