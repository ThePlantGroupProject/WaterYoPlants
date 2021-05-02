from tkinter import *

root = Tk()
root.title("Example Title")
root.geometry("500x500")

# # creating a label widget
# mylabel = Label(root, text="ExampleText")
# mylabel1 = Label(root, text="ExampleText1")
# # location of the label
# # mylabel.grid(row=0, column=0)
# # mylabel1.grid(row=1, column=0)
# mylabel.pack()
# mylabel1.pack()

# # creating the checkboxes
# def show():
#     # .get() is to get whatever information it is given
#     label_for_c = Label(root, text=var.get()).pack()
# 
# var = StringVar()
# c = Checkbutton(root, text="example check box", variable=var, onvalue="on", offvalue="off")
# c.deselect()
# c.pack()
# 
# 
# button_for_c = Button(root, text="example selection", command=show).pack()


# creating an entry box
e = Entry(root, width=25, bg="green", borderwidth=5)
e.insert(0, "example text in box")
e.pack()
# .get() is to get whatever information it is given
e.get()

def myclick():
    typed_in = e.get()
    label_for_e = Label(root, text=typed_in)
    label_for_e.pack()
    
mybutton_for_e = Button(root, text="Example Button", command=myclick, bg="green")
mybutton_for_e.pack()

# # giving the button a command when it gets pressed
# def myclick():
#     mylabel2 = Label(root, text="Example that button is pushed")
#     mylabel2.pack()
# 
# # creating a button
# mybutton = Button(root, text="Example Button", command=myclick, bg="green")
# mybutton.pack()

root.mainloop()