from tkinter import *


def convertion():
    x = float(input1.get())
    n = x * 1.60934
    label5.config(text=f"{n}")



window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=380, height=150)
window.config(padx=20, pady=20)

button = Button(text="Calculate", command=convertion)
button.grid(column=1, row=2)

input1 = Entry(width=20)
input1.grid(column=1, row=0)
input1.insert(END, string=0)

label1 = Label(text="is equal to: ", font=("Arial", 16))
label1.grid(column=0, row=1)

label2 = Label(text="Miles", font=("Arial", 16))
label2.grid(column=2, row=0)
label2.config(padx=10)

label3 = Label(text="Km", font=("Arial", 16))
label3.grid(column=2, row=1)

label5 = Label(text="0", font=("Arial", 18))
label5.grid(column=1, row=1)

window.mainloop()
