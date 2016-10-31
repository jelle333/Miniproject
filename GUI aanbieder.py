from tkinter import *

root = Tk()

button = Button(master=root,
                text='nog niet aangeboden films',)
button.pack(pady=10)

button = Button(master=root,
                text='overzicht films die ik aanbied',)
button.pack(pady=10)

button = Button(master=root,
                text='overzicht bezoekers bij mij',)
button.pack(pady=10)

button = Button(master=root,
                text='aanmeldcode bezoekers',)
button.pack(pady=10)

root.mainloop()
