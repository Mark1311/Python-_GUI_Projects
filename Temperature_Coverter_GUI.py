from tkinter import *
from tkinter import ttk
import random

def cel_to_far(celsius):
    farenhiet = 32 + celsius*1.8
    return round(farenhiet,3)

def far_to_cel(farenhiet):
    celsius = (farenhiet-32)/1.8
    return round(celsius,3)

def kel_to_cel(kelvin):
    celsius = kelvin - 273
    return round(celsius,3)

def cel_to_kel(celsius):
    kelvin = celsius+273
    return round(kelvin,3)

def convert():
  try:
     celsius = Celsius_input.get(1.0,END)
     farenhiet = Farenhiet_input.get(1.0,END)
     kelvin = Kelvin_input.get(1.0,END)

     if len(celsius)>1 :
        celsius = int(celsius)
        farenhiet = cel_to_far(celsius)
        kelvin = cel_to_kel(celsius)

     elif len(kelvin)>1:
        kelvin = int(kelvin)
        celsius = kel_to_cel(kelvin)
        farenhiet = cel_to_far(celsius)
     
     elif len(farenhiet)>1:
        farenhiet = int(farenhiet)
        celsius = far_to_cel(farenhiet)
        kelvin = cel_to_kel(celsius)

     Celsius_input.delete(1.0,END)
     Celsius_input.insert(END, celsius)
     Farenhiet_input.delete(1.0,END)
     Farenhiet_input.insert(END, farenhiet)
     Kelvin_input.delete(1.0,END)
     Kelvin_input.insert(END, kelvin)

  except:
     print("error")

def clear():
     Celsius_input.delete(1.0,END)
     Farenhiet_input.delete(1.0,END)
     Kelvin_input.delete(1.0,END)



root = Tk()
root.geometry("700x400")
root.resizable(True,True)
root.config(bg = 'gray20')
root.title("Converter")

Font = 'arial', 20, 'bold'

Label(root, text="Celsius", font=Font).place(x=50, y=50)
Label(root, text="farenhiet", font=Font).place(x=50, y=125)
Label(root, text="Kelvin", font=Font).place(x=50, y=200)


Celsius_input = Text(root,font='arial 20', height = 1,width = 50,padx=5,pady=5)
Celsius_input.place(x= 225,y=50)

Farenhiet_input= Text(root,font='arial 20', height = 1, width = 50,  wrap = WORD, padx=5,pady=5)
Farenhiet_input.place(x= 225,y=125)

Kelvin_input = Text(root, font='arial 20', height = 1, width = 50, padx=5,pady=5)
Kelvin_input.place(x= 225,y=200)

clearBtn = Button(root, text = "clear", font = Font, padx=5, pady=5, command=clear)
clearBtn.place(x=750, y=300)

convertBtn = Button(root, text= "convert", font = Font, padx=5, pady=5, command=convert)
convertBtn.place(x=600, y=300)

root.mainloop()