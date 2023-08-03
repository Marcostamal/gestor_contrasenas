from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generated_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    entry_password.delete(0,END)
    entry_password.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    new_data = {
        website:{
            "email": email,
            "password": password,
            }
        }

    if len(website.strip()) == 0 or len(password.strip()) == 0 :
        error = messagebox.showinfo(title="Error", message="Asegurate de llenar todos los campos")
    
    else:
        try:
            with open("data.json", "r") as data_file:
                # Lectura
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Actualizacion
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Guardar
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0,END)
            entry_email.delete(0,END)
            entry_email.insert(0,"email@example.com")
            entry_password.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = entry_website.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No hay datos en el archivo")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="Aun no hay una contraseña para {}".format(website))
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#                                              ----------etiquetas-----------
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

#                                                 ---------Entradas----------

entry_website = Entry(width=32)
entry_website.grid(column=1, row=1)
entry_website.focus()

entry_email = Entry(width=50)
entry_email.insert(0, "email@example.com")
entry_email.grid(column=1, row=2, columnspan=2)


entry_password = Entry(width=50)
entry_password.grid(column=1, row=3, columnspan=2)

#                                                     -------Botones--------

boton_gererate = Button(text="Generate Password",command=generated_password)
boton_gererate.grid(column=2, row=3)

boton_add = Button(text="Add", width=43, command=save)
boton_add.grid(column=1, row=4, columnspan=2,)

search_boton = Button(text="Search", width=10, command=find_password)
search_boton.grid(column=2, row=1)


window.mainloop()