from tkinter import *

# --------------------------------- UI SETUP---------------------------------

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

generate_pass_btn = Button(text="Generate", width=10)
save_pass_btn = Button(text="Save password", width=33)

website_label.grid(column=0, row=1)
website_entry.grid(column=1, columnspan=2, row=1)
username_label.grid(column=0, row=2)
username_entry.grid(column=1, columnspan=2, row=2)
password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3)
generate_pass_btn.grid(column=2, row=3)
save_pass_btn.grid(column=1, columnspan=2, row=4)

window.mainloop()
