from tkinter import *
from tkinter.messagebox import *
import math as m



#Some Default Variables
font = ("Verdana", 22, 'bold')

#<<---------------Working Functions------------------->>

def all_clear():
     textField.delete(0, END)


def clear():
     ex = textField.get()
     ex = ex[0:len(ex)-1]
     textField.delete(0, END)
     textField.insert(0,ex)







# This Function for 1 to 9 buttons (By Loops)

def click_btn_fun(event):
     b = event.widget
     text = b["text"]

     #--------- This code for, when any button are not working 
     # if text == "x":
     #      textField.insert(END, *)
     #      return
     
     if text =="=":
          try:
              ex = textField.get()
              anser = eval(ex)
              textField.delete(0, END)
              textField.insert(0,anser)
          except Exception as e:
               print("Error..", e)
               showerror("Error", e)
          return
     
     textField.insert(END, text)


#Basic Structure of Tkinter Project

window = Tk()
window.title("Scintific Calculator - Mark VaranVal")
window.geometry("480x550")

#Picture Portion

pic = PhotoImage(file="file.png")
headerimg = Label(window, image=pic)
headerimg.pack(side=TOP, pady=15)

#Heading Portion

heading = Label(window, text = "My Calculater", font=font)
heading.pack(side=TOP)

#Text-Able Area Hera

textField = Entry(window, font=font, justify=CENTER)
textField.pack(side=TOP, pady=5, fill=X, padx=10)

#Buttons Frame

buttonFrame = Frame(window)
buttonFrame.pack(side=TOP)

#Adding Buttons Using For Loops

temp = 1

for i in range(0,3):
    for j in range(0,3):
          btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief="ridge", activebackground="black", activeforeground="white")
          btn.grid(row=i, column=j, padx=3, pady=3)
          temp = temp + 1
          btn.bind('<Button-1>', click_btn_fun)


#Zero Button Adding

zerobtn = Button(buttonFrame, text="0", font=font, width=5, relief="ridge")
zerobtn.grid(row=3, column=0, padx=3, pady=3)

#DoT Button Adding

dotbtn = Button(buttonFrame, text=".", font=font, width=5, relief="ridge")
dotbtn.grid(row=3, column=1, padx=3, pady=3)

# Equal Button

eqalbtn = Button(buttonFrame, text="=", font=font, width=5, relief="ridge")
eqalbtn.grid(row=3, column=2, padx=3, pady=3)

#Adding + Button

plusbtn = Button(buttonFrame, text="+", font=font, width=5, relief="ridge")
plusbtn.grid(row=0, column=3, padx=3, pady=3)

#Adding - Button

minbtn = Button(buttonFrame, text="-", font=font, width=5, relief="ridge")
minbtn.grid(row=1, column=3, padx=3, pady=3)

#Adding * Button

multbtn = Button(buttonFrame, text="*", font=font, width=5, relief="ridge")
multbtn.grid(row=2, column=3, padx=3, pady=3)

#Adding / Button

divibtn = Button(buttonFrame, text="/", font=font, width=5, relief="ridge")
divibtn.grid(row=3, column=3, padx=3, pady=3)

#Clear Button 

clearbtn = Button(buttonFrame, text="<--", font=font, width=11, relief="ridge", command=clear)
clearbtn.grid(row=4, column=0, columnspan=2, padx=3, pady=3)

#All Claer Button

allclearbtn = Button(buttonFrame, text="AC", font=font, width=11, relief="ridge", command=all_clear)
allclearbtn.grid(row=4, column=2, columnspan=2, padx=3, pady=3)


#Binds All Other Buttons

plusbtn.bind('<Button-1>', click_btn_fun)
minbtn.bind('<Button-1>', click_btn_fun)
multbtn.bind('<Button-1>', click_btn_fun)
divibtn.bind('<Button-1>', click_btn_fun)

zerobtn.bind('<Button-1>', click_btn_fun)
dotbtn.bind('<Button-1>', click_btn_fun)
eqalbtn.bind('<Button-1>', click_btn_fun)




#----------------------Scintifice Calculator Code--------------------#

#Add more Others Buttons

scFrame = Frame(window)

sqrtbtn = Button(scFrame, text="√", font=font, width=5, relief="ridge", )
sqrtbtn.grid(row=0, column=0)

powbtn = Button(scFrame, text="^", font=font, width=5, relief="ridge", )
powbtn.grid(row=0, column=1)

factbtn = Button(scFrame, text="x!", font=font, width=5, relief="ridge", )
factbtn.grid(row=0, column=2)

radbtn = Button(scFrame, text="toRad", font=font, width=5, relief="ridge", )
radbtn.grid(row=0, column=3)


degbtn = Button(scFrame, text="toDeg", font=font, width=5, relief="ridge", )
degbtn.grid(row=1, column=0)



sinbtn = Button(scFrame, text="sinθ", font=font, width=5, relief="ridge", )
sinbtn.grid(row=1, column=1)


cosbtn = Button(scFrame, text="cosθ", font=font, width=5, relief="ridge", )
cosbtn.grid(row=1, column=2)


tanbtn = Button(scFrame, text="tanθ", font=font, width=5, relief="ridge", )
tanbtn.grid(row=1, column=3)


#Add Cube root button----------

cbrtbtn = Button(scFrame, text="cbrt", font=font, width=5, relief="ridge")
cbrtbtn.grid(row=0, column=4,  padx=3, pady=3)

floorbtn = Button(scFrame, text="floor", font=font, width=5, relief="ridge")
floorbtn.grid(row=1, column=4,  padx=3, pady=3)

ceilbtn = Button(scFrame, text="ceil", font=font, width=5, height=3, relief="ridge")
ceilbtn.grid(row=0, column=5, rowspan=2 , padx=3, pady=3)



#Scintifice Calculator Functions

normalcalc = True


def calculat_sc(event):
     answer =""
     btn = event.widget
     ex = textField.get()
     text = btn["text"]
     if text == "toDeg":
          answer = str(m.degrees(float(ex)))

     elif text== "toRad":
          answer = str(m.radians(float(ex)))

     elif text== "x!":
          answer = str(m.factorial(float(ex)))
     elif text== "sinθ":
          answer = str(m.sin(float(ex)))
     elif text== "cosθ":
          answer = str(m.cos(float(ex)))
     elif text== "tanθ":
          answer = m.tan(float(ex))
     elif text== "^":
          base,pow = ex.split(",")      #Manually type -------- base(2), pow(2 => 4 (answer))
          answer = m.pow(int(base), int(pow))
     elif text== "√":
          answer = m.sqrt(int(ex))
     elif text== "cbrt":
          answer = str(m.cbrt(float(ex)))
     elif text== "floor":
          answer = str(m.floor(float(ex)))
     elif text== "ceil":
          answer = str(m.floor(float(ex)))
     

     textField.delete(0,END)
     textField.insert(0,answer)

def sci_click():
     global normalcalc
     if normalcalc:
          buttonFrame.pack_forget()
          scFrame.pack(side=TOP, pady=20)
          buttonFrame.pack(side=TOP)
          window.geometry("790x730")
          normalcalc = False
     else:
          scFrame.pack_forget()
          window.geometry("480x550")
          normalcalc = True


#Create A MenuBar 

menubar = Menu(window)
mod = Menu(menubar,tearoff=0)

mod.add_checkbutton(label="Scintifice_Calculator", command=sci_click)
menubar.add_cascade(label="Mode", menu=mod)
window.config(menu=menubar)

#Buttons Binding Process

sqrtbtn.bind("<Button-1>", calculat_sc)
powbtn.bind("<Button-1>", calculat_sc)
factbtn.bind("<Button-1>", calculat_sc)
radbtn.bind("<Button-1>", calculat_sc)
degbtn.bind("<Button-1>", calculat_sc)
sinbtn.bind("<Button-1>", calculat_sc)
cosbtn.bind("<Button-1>", calculat_sc)
tanbtn.bind("<Button-1>", calculat_sc)
cbrtbtn.bind("<Button-1>", calculat_sc)
floorbtn.bind("<Button-1>", calculat_sc)
ceilbtn.bind("<Button-1>", calculat_sc)

def enterClick(event):
     e = Event()
     e.widget = eqalbtn
     click_btn_fun(e)

textField.bind("<Return>", enterClick)

#Main Loop Function

window.mainloop()
