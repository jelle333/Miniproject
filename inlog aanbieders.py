from tkinter import *

def raise_frame(frame):
    frame.tkraise()

root = Tk()

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)

for frame in (f1, f2, f3):
    frame.grid(row=0, column=0, sticky='news')
class knoppen:
    Label(f1, text='Startpagina').pack()
    Button(f1, text='Ga naar inlog pagina', command=lambda:raise_frame(f2), width=30).pack(side=LEFT)
    # 'Maakt een knop met als parent f1, wanneer je er op klikt ga je naar de aangeven f, in dit geval f2.'
    Button(f1, text='Ga naar registratie pagina', command=lambda:raise_frame(f3), width=30).pack(side=RIGHT)

    Label(f2, text='Inlog pagina').pack()
    Button(f2, text='Ga naar registratie pagina', command=lambda:raise_frame(f3), width=30).pack(side=RIGHT)
    Button(f2, text='Ga naar startpagina', command=lambda:raise_frame(f1), width=30).pack(side=LEFT)

    Label(f3, text='Registratie pagina').pack()
    Button(f3, text='Ga naar startpagina', command=lambda:raise_frame(f1), width=30).pack(side=RIGHT)
    Button(f3, text='Ga naar inlog pagina', command=lambda:raise_frame(f2), width=30).pack(side=LEFT)


labelGebruiker = Label(f2,
                       text='Vul uw gebruikersnaam in: ',
                       width=25).pack()
entryGebruiker = Entry(f2,
                       text='gebruikersnaam',
                       width=20).pack()

labelWw = Label(f2,
                text='Vul uw wachtwoord in: ',
                width=25).pack()
entryWw = Entry(f2,
              text='wachtwoord',
              width=20).pack()
# wil extra ruimte hier tussen
button = Button(f2,
                text='Log in',
                width=17).pack()

raise_frame(f1)
root.mainloop()
