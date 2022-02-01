from tkinter import *
from time import strftime

root = Tk()

root.geometry("640x594")

root.config(bg = "lightyellow")

def Show_Text_Bar():
    text_1 = Text(root, height = 5, width = 40)
    text_1.pack(side = TOP)

def Show_Random_text():
    label = Label(root, text = "Now is the winter of our discontent", font = ("new courrier", 13))
    label.pack(side = BOTTOM)


def time():
    string = strftime("%H:%M:%S")
    labl.config(text = string)
    labl.after(1000, time)


labl = Label(root, font = ("new courrier", 13), fg = "purple")
labl.pack(anchor = "center")


btn_1 = Button(root, text = "Start here!", command = Show_Text_Bar)    
btn_1.pack(side = TOP)

btn_2 = Button(root, text = "Get Your text here", command = Show_Random_text)
btn_2.pack(side = TOP)

root.title("TypetesTer")

time()
root.mainloop()
