from tkinter import *
import random
import string

def generate():
    small_Alpha = string.ascii_lowercase
    capital_Alpha = string.ascii_uppercase
    numbers = string.digits
    specil_char = string.punctuation

    MyPassword = small_Alpha+capital_Alpha+numbers+specil_char
    password_length = int(lengthBox.get())

    if choice.get() ==1:
          passwordEntry.insert(0, random.sample(small_Alpha+capital_Alpha, password_length))
    if choice.get() ==2:
          passwordEntry.insert(0, random.sample(small_Alpha+capital_Alpha+numbers, password_length))
    if choice.get() ==3:
         passwordEntry.insert(0, random.sample(MyPassword, password_length))
                               
                    

def all_clear():
     passwordEntry.delete(0, END)


root = Tk()
root.config(bg='gray20')
choice = IntVar()
Font = 'arial', 20, 'bold'

root.title("Random Passw0rd Generator")

password = Label(root, text="Random Password Generator", font = ('times new roman', 50, 'bold'), bg= 'gray20', fg = 'white')
password.pack(pady = 20)

weakbutton = Radiobutton(root, text='Weak Password', padx=15, value = 1, variable = choice, font = Font)
weakbutton.pack(pady=10)

Meadiumbutton = Radiobutton(root, text='Medium Password',padx=15, value = 2, variable = choice, font = Font)
Meadiumbutton.pack(pady = 10)

strongbutton = Radiobutton(root, text='Strong Password',padx=15, value = 3, variable = choice, font = Font)
strongbutton.pack(pady = 10)


password = Label(root, text="Choice Your Password Length", font = ('times new roman', 25, 'bold'), bg= 'gray20', fg = 'white')
password.pack(pady=5)

lengthBox = Spinbox(root, from_= 5, to_=15 , width = 5, font = Font )
lengthBox.pack(pady=5)

generatebutton= Button(root, text = 'Generator Password', pady=0, font = ('times new roman', 20, 'bold'), command=generate, bg = "Green")
generatebutton.pack(pady=10)

passwordEntry = Entry(root, width=25, bd = 2, font = ('times new roman', 20, 'bold'))
passwordEntry.pack()

clearbutton = Button(root, text = 'Reset', font =Font, command=all_clear, bg = "red")
clearbutton.pack(pady=10)



































root.mainloop()