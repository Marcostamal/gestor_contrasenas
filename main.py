from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

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

    if len(website.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0 :
        error = messagebox.showinfo(title="Error", message="Asegurate de llenar todos los campos")
    
    else:

        mensaje = """Quiere ingresar los siguientes datos?
        Email: {}
        Password: {}""".format(email,password)


        is_ok = messagebox.askokcancel(title=website, message=mensaje)    

        with open("data.txt", "a") as data_file:
            data_file.write(f"{website.lower()},{email.lower()},{password.lower()}\n")
            entry_website.delete(0,END)
            entry_email.delete(0,END)
            entry_email.insert(0,"email@example.com")
            entry_password.delete(0,END)
        
    

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

entry_website = Entry(width=50)
entry_website.grid(column=1, row=1, columnspan=2)
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


window.mainloop()