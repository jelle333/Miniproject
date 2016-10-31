from tkinter import *

root = Tk()
bg='green'
label=Label(master=root,
            text='Vul uw gebruikersnaam in: ',
            width=25,
            anchor=W,
            bg='yellow')
label.grid(row=0,
           column=0,
           pady=10)

label = Label(master=root,
              text='Vul uw wachtwoord in: ',
              width=25,
              anchor=W)
label.grid(row=1,
           column=0,
           pady=10)

entry = Entry(master=root,
              text='gebruikersnaam',
              width=20)
entry.grid(row=0,
           column=1,
           pady=10)

entry = Entry(master=root,
              text='wachtwoord',
              width=20)
entry.grid(row=1,
           column=1,
           pady=10)

button = Button(master=root,
                text='Log in',
                width=17)
button.grid(row=2,
            column=1)

root.mainloop()
