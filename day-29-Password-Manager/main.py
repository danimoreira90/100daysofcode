from tkinter import *
from tkinter import messagebox
FONT = ("Helvetica", 11, "bold")
from random import *
import pyperclip
import json
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():

    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Password Manager", message=f"{website}\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for item in range(randint(8, 10))]
    password_numbers = [choice(numbers) for item in range(randint(2, 4))]
    password_symbols = [choice(symbols) for item in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {
        website : {
             "email": email,
            "password": password,
        }

    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white", font=FONT)
website_label.grid(column=0, row=1)
website_label.config(padx=5, pady=5)

email_username_label = Label(text="Email/Username:", bg="white", font=FONT)
email_username_label.grid(column=0, row=2)
email_username_label.config(padx=5, pady=5)

password_label = Label(text="Password:", bg="white", font=FONT)
password_label.grid(column=0, row=3)
password_label.config(padx=5, pady=5)

#Entries

website_input = Entry(width=36)
website_input.grid(column=1, row=1)
website_input.focus()

email_username_input = Entry(width=55)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "danielcm90@gmail.com")

password_input = Entry(width=36)
password_input.grid(column=1, row=3)


#Buttons

add_button = Button(text="Add", highlightthickness=0, width=47, command=save)
add_button.grid(column=1, row=4, columnspan=2)

generate_passsword_button = Button(text="Generate Password", width=15, command=password_generator)
generate_passsword_button.grid(column=2, row=3)

search_button = Button(text="Search", highlightthickness=0, width=15, command=find_password)
search_button.grid(column=2, row=1)









window.mainloop()