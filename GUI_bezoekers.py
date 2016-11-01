from tkinter import *
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
import base64
from urllib.request import urlopen
from io import BytesIO
from API_Opvragen import *


def clickedNaamMail():
    global naamInvul,mailInvul
    naam = naamInvul.get()
    mail = mailInvul.get()
    if '@' not in mail or '.' not in mail:
        bericht = 'Dit is geen geldig emailadres, probeer het nog een keer'
        showinfo(title='popup', message=bericht)
    else:
        plaatjes()
    return

def plaatjes():
    global filmMenu
    root.withdraw()
    filmMenu = Toplevel(master=root,background='white')
    info = coversOpvragen()

    kiesEenFilm = Label(master=filmMenu,
                text='Kies een van de onderstaande films',
                background='white',
                font=('Arial', 18))
    kiesEenFilm.grid(row=0,column=1,columnspan=3, pady=5, sticky='nesw')

    for i in range(0, len(info)):
        if i == 0:
            URL = info[0][0]
            u = urlopen(URL)
            raw_data = u.read()
            u.close()

            im = Image.open(BytesIO(raw_data))
            photo0 = ImageTk.PhotoImage(im)

            button0 = Button(master=filmMenu, image=photo0, command= lambda: movieClick(info,0))
            button0.image = photo0
            button0.grid(row=1, column=0)

            text0 = '{} ({})'.format(info[0][1],info[0][2])

            label0 = Label(master=filmMenu,
                           text=text0,
                           background='white',
                           wraplength=250,
                           font=('Arial', 16))
            label0.grid(row=2, column= 0, pady=5)
        elif i == 1:
            URL = info[1][0]
            u = urlopen(URL)
            raw_data = u.read()
            u.close()

            im = Image.open(BytesIO(raw_data))
            photo1 = ImageTk.PhotoImage(im)

            button1 = Button(master=filmMenu, image=photo1,command= lambda: movieClick(info,1))
            button1.image = photo1
            button1.grid(row=1, column=1)

            text1 = '{} ({})'.format(info[1][1],info[1][2])

            label1 = Label(master=filmMenu,
                           text=text1,
                           background='white',
                           wraplength=250,
                           font=('Arial', 16))
            label1.grid(row=2, column= 1, pady=5)
        elif i == 2:
            URL = info[2][0]
            u = urlopen(URL)
            raw_data = u.read()
            u.close()

            im = Image.open(BytesIO(raw_data))
            photo2 = ImageTk.PhotoImage(im)

            button2 = Button(master=filmMenu, image=photo2,command= lambda: movieClick(info,2))
            button2.image = photo2
            button2.grid(row=1, column=2)

            text2 = '{} ({})'.format(info[2][1],info[2][2])

            label2 = Label(master=filmMenu,
                           text=text2,
                           background='white',
                           wraplength=250,
                           font=('Arial', 16))
            label2.grid(row=2, column= 2, pady=5)
        elif i == 3:
            URL = info[3][0]
            u = urlopen(URL)
            raw_data = u.read()
            u.close()

            im = Image.open(BytesIO(raw_data))
            photo3 = ImageTk.PhotoImage(im)

            button3 = Button(master=filmMenu, image=photo3,command= lambda: movieClick(info,3))
            button3.image = photo3
            button3.grid(row=1, column=3)

            text3 = '{} ({})'.format(info[3][1],info[3][2])

            label3 = Label(master=filmMenu,
                           text=text3,
                           background='white',
                           wraplength=250,
                           font=('Arial', 16))
            label3.grid(row=2, column= 3, pady=5)
        elif i == 4:
            URL = info[4][0]
            u = urlopen(URL)
            raw_data = u.read()
            u.close()

            im = Image.open(BytesIO(raw_data))
            photo4 = ImageTk.PhotoImage(im)

            button4 = Button(master=filmMenu, image=photo4,command= lambda: movieClick(info,4))
            button4.image = photo4
            button4.grid(row=1, column=4)

            text4 = '{} ({})'.format(info[4][1],info[4][2])

            label4 = Label(master=filmMenu,
                           text=text4,
                           background='white',
                           wraplength=250,
                           font=('Arial', 16))
            label4.grid(row=2, column= 4, pady=5)
        elif i == 5:
            URL = info[5][0]
            u = urlopen(URL)
            raw_data = u.read()
            u.close()

            im = Image.open(BytesIO(raw_data))
            photo5 = ImageTk.PhotoImage(im)

            button5 = Button(master=filmMenu, image=photo5,command= lambda: movieClick(info,5))
            button5.image = photo5
            button5.grid(row=3, column=0)

            text5 = '{} ({})'.format(info[5][1],info[5][2])

            label5 = Label(master=filmMenu,
                           text=text5,
                           background='white',
                           wraplength=250,
                           font=('Arial', 16))
            label5.grid(row=4, column= 0, pady=5)
        elif i == 6:
            URL = info[6][0]
            u = urlopen(URL)
            raw_data = u.read()
            u.close()

            im = Image.open(BytesIO(raw_data))
            photo6 = ImageTk.PhotoImage(im)

            button6 = Button(master=filmMenu, image=photo6,command= lambda: movieClick(info,6))
            button6.image = photo6
            button6.grid(row=3, column=1)

            text6 = '{} ({})'.format(info[6][1],info[6][2])

            label6 = Label(master=filmMenu,
                           text=text6,
                           background='white',
                           wraplength=250,
                           font=('Arial', 16))
            label6.grid(row=4, column= 1, pady=5)
        elif i == 7:
            URL = info[7][0]
            u = urlopen(URL)
            raw_data = u.read()
            u.close()

            im = Image.open(BytesIO(raw_data))
            photo7 = ImageTk.PhotoImage(im)

            button7 = Button(master=filmMenu, image=photo7,command= lambda: movieClick(info,7))
            button7.image = photo7
            button7.grid(row=3, column=2)

            text7 = '{} ({})'.format(info[7][1],info[7][2])

            label7 = Label(master=filmMenu,
                           text=text7,
                           background='white',
                           wraplength=250,
                           font=('Arial', 16))
            label7.grid(row=4, column= 2, pady=5)
        elif i == 8:
            URL = info[8][0]
            u = urlopen(URL)
            raw_data = u.read()
            u.close()

            im = Image.open(BytesIO(raw_data))
            photo8 = ImageTk.PhotoImage(im)

            button8 = Button(master=filmMenu, image=photo8,command= lambda: movieClick(info,8))
            button8.image = photo8
            button8.grid(row=3, column=3)

            text8 = '{} ({})'.format(info[8][1],info[8][2])

            label8 = Label(master=filmMenu,
                           text=text8,
                           background='white',
                           wraplength=250,
                           font=('Arial', 16))
            label8.grid(row=4, column= 3, pady=5)
        elif i == 9:
            URL = info[9][0]
            u = urlopen(URL)
            raw_data = u.read()
            u.close()

            im = Image.open(BytesIO(raw_data))
            photo9 = ImageTk.PhotoImage(im)

            button9 = Button(master=filmMenu, image=photo9,command= lambda: movieClick(info,9))
            button9.image = photo9
            button9.grid(row=3, column=4)

            text9 = '{} ({})'.format(info[2][9],info[2][9])

            label9 = Label(master=filmMenu,
                           text=text9,
                           background='white',
                           wraplength=250,
                           font=('Arial', 16))
            label9.grid(row=4, column= 4, pady=5)

def movieClick(info,i):
    filmMenu.withdraw()
    perFilmMenu = Toplevel(master=filmMenu,background='white')
    URL = info[i][0]
    u = urlopen(URL)
    raw_data = u.read()
    u.close()

    im = Image.open(BytesIO(raw_data))
    photo0 = ImageTk.PhotoImage(im)

    button0 = Label(master=perFilmMenu, image=photo0)
    button0.image = photo0
    button0.grid(row=1, column=0)

    text0 = '{} ({})'.format(info[i][1],info[i][2])

    label0 = Label(master=perFilmMenu,
                    text=text0,
                    background='white',
                    wraplength=500,
                    font=('Arial', 16))
    label0.grid(row=2, column= 0, pady=5)

    synopsys = Label(master=perFilmMenu,
                    text=info[i][3],
                    background='white',
                    wraplength=250,
                    font=('Arial', 12))
    synopsys.grid(row=1, column= 1,columnspan= 3, pady=5, sticky='n')




root = Tk()


naamInvul = Entry(master=root)
naamInvul.grid(row=0, column= 1,padx=10, pady=2)

naam = Label(master=root, text='Naam: ', height=2)
naam.grid(row=0, column= 0,padx=10, pady=2)

mailInvul = Entry(master=root)
mailInvul.grid(row=1, column=1,padx=10, pady=2)

email = Label(master=root, text='Email: ', height=2)
email.grid(row=1, column= 0,padx=10, pady=2)

login = Button(master=root, text='Log in', command=clickedNaamMail)
login.grid(row=2, column= 1,padx=10, pady=2)



root.mainloop()
