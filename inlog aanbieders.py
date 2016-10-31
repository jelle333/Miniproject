from tkinter import *

root = Tk()

button = Button(master=root,
                text='Login',
                width=10)
button.pack(pady=10)

button = Button(master=root,
                text='Registreren',
                width=10)
button.pack(pady=10)

root.mainloop()
