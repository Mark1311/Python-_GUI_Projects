from tkinter import *
root = Tk()
root.title("Simple CalCulator :- Mark VaranVal")
root.geometry("570x585")
root.resizable(True, True)
root.configure(bg = "#17161b")


equation = ""

def show(value):
    global equation
    equation+=value
    result.config(text=equation)

def clear():
    global equation
    equation = ""
    result.config(text=equation)
    

def Answer():
    global equation
    resultant = ""
    if equation != "":
          try:
               resultant = eval(equation)
          except:
               resultant = "error"
               equation = ""
    result.config(text = resultant)



result = Label(root, text = "", width=24,relief=SUNKEN, height=2,bg="gray", font=("arial", 30))
result.place(x = 0, y = 0)

Button(root, text="C", width=5,relief=SUNKEN, height=1, font=("arial", 30, "bold"),  bd = 1, fg="black", bg="#3697f5", command=lambda:clear()).place(x = 10, y =100)
Button(root,text="/", width=5,relief=SUNKEN, height=1, font=("arial", 30, "bold"), bd = 1, fg="#fff", bg="#3697f5",command=lambda:show("/")).place(x = 150, y =100)
Button(root, text="%", width=5,relief=SUNKEN, height=1, font=("arial", 30, "bold"), bd = 1, fg="#fff", bg="#3697f5",command=lambda:show("%")).place(x =290, y =100)
Button(root,text="*", width=5,relief=SUNKEN, height=1, font=("arial", 30, "bold"), bd = 1, fg="#fff", bg="#3697f5",command=lambda:show("*")).place(x = 430, y =100)


Button(root, text="7", width=5,relief=SUNKEN, height=1, font=("arial", 30, "bold"), bd = 1, fg="#fff", bg="#3697f5",command=lambda:show("7")).place(x = 10, y =200)
Button(root,text="8", width=5,relief=SUNKEN, height=1, font=("arial", 30, "bold"), bd = 1, fg="#fff", bg="#3697f5",command=lambda:show("8")).place(x = 150, y =200)
Button(root, text="9", width=5,relief=SUNKEN, height=1, font=("arial", 30, "bold"), bd = 1, fg="#fff", bg="#3697f5",command=lambda:show("9")).place(x =290, y =200)
Button(root,text="-", width=5,relief=SUNKEN, height=1, font=("arial", 30, "bold"), bd = 1, fg="#fff", bg="#3697f5",command=lambda:show("-")).place(x = 430, y =200)

Button(root, text="4", width=5,relief=SUNKEN, height=1, font=("arial", 30, "bold"), bd = 1, fg="#fff", bg="#3697f5",command=lambda:show("4")).place(x = 10, y =300)
Button(root,text="5", width=5,relief=SUNKEN, height=1, font=("arial", 30, "bold"), bd = 1, fg="#fff", bg="#3697f5",command=lambda:show("5")).place(x = 150, y =300)
Button(root, text="6", width=5,relief=SUNKEN, height=1, font=("arial", 30, "bold"), bd = 1, fg="#fff", bg="#3697f5",command=lambda:show("6")).place(x =290, y =300)
Button(root,text="+", width=5,relief=SUNKEN, height=1, font=("arial", 30, "bold"), bd = 1, fg="#fff", bg="#3697f5",command=lambda:show("+")).place(x = 430, y =300)

Button(root, text="1", width=5,relief=SUNKEN, height=1, font=("arial", 30, "bold"), bd = 1, fg="#fff", bg="#3697f5",command=lambda:show("1")).place(x = 10, y =400)
Button(root,text="2", width=5,relief=SUNKEN, height=1, font=("arial", 30, "bold"), bd = 1, fg="#fff", bg="#3697f5",command=lambda:show("2")).place(x = 150, y =400)
Button(root, text="3", width=5,relief=SUNKEN, height=1, font=("arial", 30, "bold"), bd = 1, fg="#fff", bg="#3697f5",command=lambda:show("3")).place(x =290, y =400)
Button(root,text="0", width=11,relief=SUNKEN, height=1, font=("arial", 30, "bold"), bd = 1, fg="#fff", bg="#3697f5",command=lambda:show("0")).place(x = 10, y =500)

Button(root, text=".", width=5,relief=SUNKEN, height=1, font=("arial", 30, "bold"), bd = 1, fg="#fff", bg="#3697f5",command=lambda:show(".")).place(x =290, y =500)
Button(root,text="=", width=5,relief=SUNKEN, height=3, font=("arial", 30, "bold"), bd = 1, fg="black", bg="#fe9037",command=lambda:Answer()).place(x =430, y =400)


root.mainloop()