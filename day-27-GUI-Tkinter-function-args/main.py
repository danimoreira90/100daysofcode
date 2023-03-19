from tkinter import *


def button_click():
    my_label.config(text=input.get())
    print("I got clicked.")

#Window

window = Tk()
window.title("My first GUI Program")
window.minsize(width=300, height=100)
window.config(padx=10, pady=10)


#Label
my_label = Label(text="I am a Label", font=("Arial", 18, "italic"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)



#button

button = Button(text="Click me",command=button_click)
button.grid(column=1, row=1)

#entry

input = Entry(width=15)
input.grid(column=3, row=3)
# input.get()

#New button

new_button = Button(text="Click Me", command=button_click)
new_button.grid(column=2, row=0)

window.mainloop()