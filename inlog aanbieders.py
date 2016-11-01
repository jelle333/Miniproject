from tkinter import *
# from tkinter.messagebox import showinfo
import csv

def raise_frame(frame):
    frame.tkraise()

def clickedReg():
    naam = entryGebruikerReg.get()
    # .get() werkt niet!
    wachtwoord1 = entryWw1.get()
    wachtwoord2 = entryWw2.get()
    email = entryEmail.get()
    with open('aanbieders.csv', 'r', newline='') as aanbieders:
        reader = csv.reader(aanbieders, delimiter=';')

        gebruikteNamen = []
        gebruikteWw = []
        gebruikteEmail = []

        for row in reader:
            gebruikteNamen.append(row[0])
            gebruikteWw.append(row[1])
            gebruikteEmail.append(row[2])

        if naam in gebruikteNamen:
            print('Gekozen gebruikersnaam is al bezet! Kies een ander!')


root = Tk()

start = Frame(root)
inlog = Frame(root)
reg = Frame(root)
aanbiederGUI = Frame(root)

for frame in (start, inlog, reg, aanbiederGUI):
    frame.grid(row=0, column=0, sticky='news')

Label(start, text='Startpagina').pack()
Button(start, text='Ga naar inlog pagina', command=lambda:raise_frame(inlog), width=25).pack(side=LEFT, padx=2)
# 'Maakt een knop met als parent f1, wanneer je er op klikt ga je naar de aangeven f, in dit geval f2.'
Button(start, text='Ga naar registratie pagina', command=lambda:raise_frame(reg), width=25).pack(side=RIGHT, padx=2)

Label(inlog, text='Inlog pagina').pack()
Button(inlog, text='Ga naar registratie pagina', command=lambda:raise_frame(reg), width=25).pack(side=RIGHT, padx=2)
Button(inlog, text='Ga naar startpagina', command=lambda:raise_frame(start), width=25).pack(side=LEFT, padx=2)

Label(reg, text='Registratie pagina').pack()
Button(reg, text='Ga naar startpagina', command=lambda:raise_frame(start), width=25).pack(side=RIGHT, padx=2)
Button(reg, text='Ga naar inlog pagina', command=lambda:raise_frame(inlog), width=25).pack(side=LEFT, padx=2)

Label(aanbiederGUI, text='Pagina van de aanbieder').pack()
Button(aanbiederGUI, text='Log uit', command=lambda:raise_frame(inlog), width=25).pack(side=BOTTOM, pady=2, padx=2)

# ---------------------------------------------------------------------------------------------------------------------

labelGebruiker = Label(inlog,
                       text='Vul uw gebruikersnaam in: ',
                       width=25).pack()
entryGebruiker = Entry(inlog,
                       width=25).pack(pady=2)

labelWw = Label(inlog,
                text='Vul uw wachtwoord in: ',
                width=25).pack()
entryWw = Entry(inlog,
                width=25,
                show='*').pack(pady=2)
# wil extra ruimte hier tussen
button = Button(inlog,
                text='Log in',
                command=lambda:raise_frame(aanbiederGUI),
                width=22).pack(pady=4)

# ---------------------------------------------------------------------------------------------------------------------

labelGebruikerReg=Label(reg,
                     text='Vul uw gewenste gebruikersnaam in: ',
                     width=35).pack()
entryGebruikerReg = Entry(reg,
                       width=35).pack(pady=2)

labelWw1 = Label(reg,
                 text='Vul uw gewenste wachtwoord in: ',
                 width=35).pack()
entryWw1 = Entry(reg,
                 width=35,
                 show='*').pack(pady=2)

labelWw2 = Label(reg,
                 text='Vul nogmaals uw gewenste wachtwoord in: ',
                 width=35).pack()
entryWw2 = Entry(reg,
                 width=35,
                 show='*').pack(pady=2)

labelEmail = Label(reg,
                   text='Vul uw emailaddres in: ',
                   width=35).pack()
entryEmail = Entry(reg,
                   width=35).pack(pady=2)

buttonReg = Button(reg,
                text='Registreer',
                width=22,
                command=clickedReg).pack(pady=4)

# ---------------------------------------------------------------------------------------------------------------------

button1 = Button(aanbiederGUI,
                text='nog niet aangeboden films')
button1.pack(pady=10,
             padx=5,
             side = LEFT)

button2 = Button(aanbiederGUI,
                text='overzicht films die ik aanbied',)
button2.pack(pady=10,
             padx=5,
             side = LEFT)

button3 = Button(aanbiederGUI,
                text='overzicht bezoekers bij mij',)
button3.pack(pady=10,
             padx=5,
             side = LEFT)

button4 = Button(aanbiederGUI,
                text='aanmeldcode bezoekers',)
button4.pack(pady=10,
             padx=5,
             side = LEFT)

# ---------------------------------------------------------------------------------------------------------------------

raise_frame(start)
root.mainloop()
