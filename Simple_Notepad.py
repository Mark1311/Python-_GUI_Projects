from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

#Basic Structure of Tkinter

root = Tk()
root.title("Mark VaranVal - Notepad")
root.geometry("744x788")

#--------------- All Functions Start-------------------#

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
          file = None
    else:
          root.title(os.path.basename(file) + " - Notepad" )
          TextArea.delete(1.0, END)
          f = open(file, "r")
          TextArea.insert(1.0, f.read())
          f.close()
          
          
def saveFile():
    global file
    if file == None:
          file = askopenfilename(initialfile= "Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

          if file == "":
               file = None
          else:
               #Save as A New File
               f = open(file, "w")
               f.write(TextArea.get(1.0, END))
               f.close()

               root.title(os.basename(file) + " - Notepad")
               # print("File Save Sucessfully")# Used only Debugging process.
    else:
          #Save the File
          f = open(file, "w")
          f.write(TextArea.get(1.0, END))
          f.close()
         
     

def quitGUI():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Mark VaranVal - Notepad", "Notepad by Mark VaranVal")





#--------------- All Functions End-------------------#

#Writting Area Here

TextArea = Text(root, font="lucida 13")
file = None                                  #This is Show(Humne koi File nhi open ki)
TextArea.pack( expand = TRUE, fill=BOTH)

#Horizontal MenuBar Scale Heae

MenuBar = Menu(root)

#----------------File Menu Start-------------------#
FileMenu = Menu(MenuBar, tearoff=0)

#Open New File Command

FileMenu.add_command(label="New File", command=newFile)

#Open Alredy Existing File Command

FileMenu.add_command(label="Open File", command=openFile)

#Current File Save Command

FileMenu.add_command(label="Save", command=saveFile)
FileMenu.add_separator()

#Exit Command from the GUI(NotePad)

FileMenu.add_command(label="Exit", command=quitGUI)

MenuBar.add_cascade(label="File", menu=FileMenu)

#----------------File Menu End-------------------#

#----------------Edit Menu Start-------------------#

EditMenu = Menu(MenuBar, tearoff=0)

EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy)
EditMenu.add_command(label="Paste", command=paste)

MenuBar.add_cascade(label="Edit", menu=EditMenu)

#----------------Edit Menu End-------------------#


#------------Start Format---------------#

FormateMenu = Menu(MenuBar, tearoff = 0)

FormateMenu.add_checkbutton(label="Word Wrap")
FormateMenu.add_command(label="Font")

MenuBar.add_cascade(label="Format", menu=FormateMenu)

#------------Start Format---------------#

#---------------View MenuBar Strat-------------#

ViewMenu = Menu(MenuBar, tearoff = 0)

ViewMenu.add_command(label="Zoom")
ViewMenu.add_checkbutton(label="Status Bar")

MenuBar.add_cascade(label="View", menu=ViewMenu)

#---------------View MenuBar Strat-------------#
#----------------Help Menu Start-------------------#

HelpMenu = Menu(MenuBar, tearoff=0)

HelpMenu.add_command(label="About Us", command=about)
MenuBar.add_cascade(label="Help", menu=HelpMenu)


#----------------Help Menu End-------------------#


# Configeation the menubar
root.config(menu=MenuBar)


#------------Add Scrollbar  Strat---------------#

Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)


#------------Add Scrollbar End---------------#










root.mainloop()