from tkinter import *

root = Tk()

label=Label(master=root,
            text='Vul uw gewenste gebruikersnaam in: ',
            width=34,
            anchor=W)
label.grid(row=0,
           column=0,
           pady=10)

label = Label(master=root,
              text='Vul uw gewenste wachtwoord in: ',
              width=34,
              anchor=W)
label.grid(row=1,
           column=0,
           pady=10)

label = Label(master=root,
              text='Vul nogmaals uw gewenste wachtwoord in: ',
              width=34,
              anchor=W)
label.grid(row=2,
           column=0,
           pady=10)

entry = Entry(master=root,
              text='Vul uw gebruikersnaam in',
              width=20)
entry.grid(row=0,
           column=1,
           pady=10)

entry = Entry(master=root,
              width=20)
entry.grid(row=1,
           column=1,
           pady=10)

entry = Entry(master=root,
              text='Vul uw wachtwoord nogmaals in',
              width=20)
entry.grid(row=2,
           column=1,
           pady=10)

root.mainloop()
