import random
import tkinter as tk

Height = 800
Width = 700

def test_function(entry):
    print("Button clicked!, this is the entry: ", entry)

def donothing():
    filewin = tk.Toplevel(root)
    button = tk.Button(filewin, text="Do nothing button")
    button.pack()

root = tk.Tk()

canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

background_image = tk.PhotoImage(file='North.png')
backgroud_label = tk.Label(root, image=background_image)
backgroud_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg ="grey", bd=10)
frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

entry = tk.Entry(frame, text="What is your question?", bd=5)
entry.place(relx=0, rely=0.1, relheight=0.1, relwidth=0.5)


button = tk.Button(frame, text="Submit", font=40, command=lambda: test_function(entry.get()))
button.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.5 )

mylist=["Yes", "No", "Maybe"]
x = random.choice(mylist)

lower_frame = tk.Frame(root, bg='white', bd=10)
lower_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.55, anchor='n')

label = tk.Label(lower_frame, text=print(x), bg='#3766b2')
label.place(relwidth=1, relheight = 1)

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

root.mainloop()




