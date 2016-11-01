from tkinter import *
# from tkinter.messagebox import showinfo
import csv

def raise_frame(frame):
    frame.tkraise()

# def clickedreg():
#     global entryGebruiker
#     with open('aanbieders.csv', 'r', newline='') as aanbieders:
#         reader = csv.reader(aanbieders, delimiter=';')
#
#         bezette_gebruikersnamen = []
#
#         for row in reader:
#             bezette_gebruikersnamen.append(row[0])
#
#         print(bezette_gebruikersnamen)
#
#         if entryGebruiker in bezette_gebruikersnamen:
#             print('Gebruikersnaam is al bezet!')

root = Tk()

start = Frame(root)
inlog = Frame(root)
reg = Frame(root)

class knoppen:
    for frame in (start, inlog, reg):
        frame.grid(row=0, column=0, sticky='news')
    Label(start, text='Startpagina').pack()
    Button(start, text='Ga naar inlog pagina', command=lambda:raise_frame(inlog), width=25).pack(side=LEFT)
    # 'Maakt een knop met als parent f1, wanneer je er op klikt ga je naar de aangeven f, in dit geval f2.'
    Button(start, text='Ga naar registratie pagina', command=lambda:raise_frame(reg), width=25).pack(side=RIGHT)

    Label(inlog, text='Inlog pagina').pack()
    Button(inlog, text='Ga naar registratie pagina', command=lambda:raise_frame(reg), width=25).pack(side=RIGHT)
    Button(inlog, text='Ga naar startpagina', command=lambda:raise_frame(start), width=25).pack(side=LEFT)

    Label(reg, text='Registratie pagina').pack()
    Button(reg, text='Ga naar startpagina', command=lambda:raise_frame(start), width=25).pack(side=RIGHT)
    Button(reg, text='Ga naar inlog pagina', command=lambda:raise_frame(inlog), width=25).pack(side=LEFT)

class login:
    labelGebruiker = Label(inlog,
                           text='Vul uw gebruikersnaam in: ',
                           width=25).pack()
    entryGebruiker = Entry(inlog,
                           width=25).pack()

    labelWw = Label(inlog,
                    text='Vul uw wachtwoord in: ',
                    width=25).pack()
    entryWw = Entry(inlog,
                    width=25,
                    show='*').pack()
    # wil extra ruimte hier tussen
    button = Button(inlog,
                    text='Log in',
                    width=22).pack()

class registratie:
    labelGebruiker=Label(reg,
                         text='Vul uw gewenste gebruikersnaam in: ',
                         width=35).pack()
    entryGebruiker = Entry(reg,
                           width=35).pack()

    labelWw1 = Label(reg,
                     text='Vul uw gewenste wachtwoord in: ',
                     width=35).pack()
    entryWw1 = Entry(reg,
                     width=35,
                     show='*').pack()

    labelWw2 = Label(reg,
                     text='Vul nogmaals uw gewenste wachtwoord in: ',
                     width=35).pack()
    entryWw2 = Entry(reg,
                     width=35,
                     show='*').pack()

    labelEmail = Label(reg,
                       text='Vul uw emailaddres in: ',
                       width=35).pack()
    entryEmail = Entry(reg,
                       width=35).pack()

    button = Button(reg,
                    text='Registreer',
                    width=22,
                    command='clickedreg').pack()

    # with open('aanbieders.csv', 'r', newline='') as aanbieders:
    #     reader = csv.reader(aanbieders, delimiter=';')
    #
    #     lijst_aanbieders = []
    #
    #     for row in reader:
    #         lijst_aanbieders.append(row[0])
    #
    #     if entryGebruiker in lijst_aanbieders:
    #         bericht = 'Gebruikersnaam is al bezet!'
    #         showinfo(title='popup', message=bericht)
    #
    # print(lijst_aanbieders)


raise_frame(start)
root.mainloop()
