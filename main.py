from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    pass_input.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols =[random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0,password)

    # copies password to user clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    email = user_input.get()
    website = web_input.get()
    password = pass_input.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }
    }



    if len(website) == 0 or len(password) == 0:
            messagebox.showerror(title="Oops", message= "Please don't leave any fields empty!")
    else:
         try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
         except FileNotFoundError:
             with open("data.json","w") as data_file:
                 json.dump(new_data, data_file, indent=4)
         else:
                # Updating old data with new data
             data.update(new_data)

             with open("data.json","w") as data_file:
                    # Saving updated data
                    json.dump(data,data_file,indent = 4)


         user_input.delete(0,END)
         web_input.delete(0,END)
         pass_input.delete(0,END)

def find_password():
    email = user_input.get()
    website = web_input.get()

    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
            messagebox.showerror(title = "File not found",message= "This file does not exist!")

    else:
        if website in data:
            mail = data[website][("email")]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {mail}\nPassword: {password}")
        else:
            messagebox.showerror(title= "Error", message= f"No records exist for {website}")

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.config(padx = 50, pady =50)
window.title("Password Manager")

# Logo image
photo = PhotoImage(file = "logo.png")
canvas = Canvas(width = 200, height = 200)
canvas.create_image(100,100,image = photo)

canvas.grid(column = 1, row = 0)

# Labels
web_label = Label(text = "Website:")
web_label.grid(column = 0, row = 1)

user_label = Label(text="Email/Username:")
user_label.grid(column = 0, row = 2)

pass_label = Label(text = "Password:")
pass_label.grid(column = 0, row = 3)

# Entries
web_input = Entry(width = 35)
web_input.focus()
web_input.grid(column = 1, row = 1)


user_input = Entry(width = 35)
user_input.grid(column = 1, row = 2)


pass_input  = Entry(width = 35)
pass_input.grid(column = 1, row = 3)


# Buttons
pass_button = Button(text = "Generate Password",command= generate_password)
pass_button.grid(column = 2, row = 3)

add_button = Button(text="Add", width= 36, command = save)
add_button.grid(column = 1, row = 4,columnspan = 2)

search_button = Button(text = "Search", command = find_password, width = 14)
search_button.grid(column = 2, row = 1, columnspan =2)

















window.mainloop()
