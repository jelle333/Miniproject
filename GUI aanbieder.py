from tkinter import *

def toonVenster():
    def close():
        subwindow.withdraw()
    subwindow = Toplevel(master=root)
    button2 = Button(master=subwindow,
                     text='Sluit mij',
                     command=close)
    button2.pack(padx=10, pady=10)

root = Tk()

button1 = Button(master=root,
                text='nog niet aangeboden films',
                 command=toonVenster)
button1.pack(pady=10)

button2 = Button(master=root,
                text='overzicht films die ik aanbied',)
button2.pack(pady=10)

button3 = Button(master=root,
                text='overzicht bezoekers bij mij',)
button3.pack(pady=10)

button4 = Button(master=root,
                text='aanmeldcode bezoekers',)
button4.pack(pady=10)

root.mainloop()
