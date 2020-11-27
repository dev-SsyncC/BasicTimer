from tkinter import *

world = 0

def countdown():
    global world
    world = world + int(userInput.get())
    return world

def timer():
    global world
    if world > 0:
        firstlabel.config(text = world)
        world -= 1
        firstlabel.after(1000,timer)
    elif world == 0:
        print("End")
        firstlabel.config(text = "End")        

root = Tk()
root.geometry("200x200")
firstlabel = Label(root,pady = 10,padx = 10)
firstlabel.pack()
time = StringVar()
userInput = Entry(root, textvariable = time)
userInput.pack()
button = Button(root,text = "Set", width = 15, pady = 5,command = countdown)
button.pack()
button2 = Button(root,text = "Start", width = 20, pady = 5,command = timer)
button2.pack()


root.mainloop()