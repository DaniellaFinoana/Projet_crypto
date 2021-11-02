from asyncio.windows_events import NULL
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from tkinter import ttk
from connection import *

import status as status
from decryptage import *
from cryptage import *
import connection as connect

from PIL import Image, ImageTk

window = Tk()
window.title('Centre hospitalier')
window.geometry("1200x1000")
window.iconbitmap("ico.ico")


# menu_bar= Menu(window)

class Person():
    def __init__(self, nom, prenom, adresse, contact, service, poste, photo):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.contact = contact
        self.service = service
        self.poste = poste
        self.photo = photo

    def __eq__(self, other):
        return (
                    self.nom == other.nom and self.prenom == other.prenom and self.adresse == adresse and self.contact == other.contact and self.service == other.service and self.poste == other.poste and self.photo == other.photo)




def choisir():
    global imageName
    imn = askopenfilename(initialdir="/", title="selection photo",
                          filetypes=(("png files", "*.png"), ("jpeg files", "*.jpg")))

    if imn:
        imageName = imn
    if imageName:
        texte = imageName.split("/")
        photo.configure(text=".../" + texte[-1])


def valider():
    global imageName
    photo = imageName
    nom = crypt(nomEntry1.get())
    prenom = crypt(prenomEntry1.get())
    service = crypt(serviceEntry1.get())
    poste = crypt(posteEntry1.get())
    adresse = NULL
    contact = NULL
    data = Person(nom, prenom, adresse, contact,service,poste, photo)
    connect.ajout(data)
    showinfo(title="Validation", message="enregistrement reussi")
    annuler1()


def valider2():
    nom = crypt(nomEntry.get())
    prenom = crypt(prenomEntry.get())
    service = crypt(serviceEntry.get())
    adresse =crypt(adresseEntry.get())
    poste=NULL
    photo=NULL
    data = Person(nom, prenom,adresse, contactEntry.get(),service,poste,photo)
    connect.ajout(data)
    showinfo(title="Validation", message="enregistrement réussi")
    annuler2()


def Lmed():
    hide_all_frames()
    frame1.pack(fill="both", expand=1)
    resultat = parcourirM()
    if len(resultat):
        for enreg in resultat:
            table1.insert('', 'end', iid=enreg[0], values=(enreg[0],SuperDecrypt(enreg[1]), SuperDecrypt(enreg[2]), SuperDecrypt(enreg[3]), SuperDecrypt(enreg[4])))


def Lpat():
    hide_all_frames()
    frame2.pack(fill="both", expand=1)
    resultat = parcourirP()
    if len(resultat):
        for enreg in resultat:
            table.insert('', 'end', iid=enreg[0], values=(enreg[0],SuperDecrypt(enreg[1]), SuperDecrypt(enreg[2]), SuperDecrypt(enreg[3]), enreg[4], SuperDecrypt(enreg[5])))




def Apat():
    hide_all_frames()
    frame3.pack(fill="both", expand=1)


def Amed():
    hide_all_frames()
    frame4.pack(fill="both", expand=1)

def hide_all_frames():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()


def annuler1():
    nomEntry1.delete(0, END)
    prenomEntry1.delete(0, END)
    serviceEntry1.delete(0, END)
    posteEntry1.delete(0, END)
    imageName = ''
    photo.configure(text="aucune image choisie")
def annuler2():
    nomEntry.delete(0,END)
    prenomEntry.delete(0,END)
    adresseEntry.delete(0,END)
    contactEntry.delete(0,END)
    serviceEntry.delete(0,END)

def supp():
    idselect=table1.item(table1.selection())['values'][0]
    delete(idselect)
    table1.delete(table1.selection())
def supp2():
    idselect=table.item(table.selection())['values'][0]
    delete(idselect)
    table.delete(table.selection())
def view():
    idselect=table1.item(table1.selection())['values'][0]
    img=voir(idselect)
    load = Image.open(img)
    load.thumbnail((200, 200))
    photo = ImageTk.PhotoImage(load)
    label_image2 = Label(Vframe, image=photo)
    label_image2.place(x=250, y=250)

    Vframe.place(x=200,y=100)

imageName = ''

window2 = Frame(window, bg="#48c1e6")
window2.pack(fill="both", expand="0")

#menu

liste = Button(window2, text='Liste des medecins', command=Lmed, fg="#292b2c", bg="#48c1e6"
               , width="30"
               , height="5"
               , border=0
               , font=("Courrier", 11)
               )
liste.grid(row=0, column=0)
liste1 = Button(window2, text='Liste patients', command=Lpat, fg="#292b2c", bg="#48c1e6"
                , width="30"
                , height="5"
                , border=0
                , font=("Courrier", 11)
                )
liste1.grid(row=0, column=1)
ajout = Button(window2, text='Ajout patient', command=Apat, fg="#292b2c", bg="#48c1e6"
               , width="30"
               , height="5"
               , border=0
               , font=("Courrier", 11)
               )
ajout.grid(row=0, column=2)
ajout2 = Button(window2, text='Ajout medecin', command=Amed, fg="#292b2c", bg="#48c1e6"
                , width="30"
                , height="5"
                , border=0
                , font=("Courrier", 11)
                )
ajout2.grid(row=0, column=3)
frame1 = Frame(window, bg="white")
frame2 = Frame(window, bg="white")
frame3 = Frame(window, bg="white")
frame4 = Frame(window, bg="white")

#ajout personnel

cadre1 = Frame(frame4, bg="white")
cadre1.pack(padx="200", pady="40")
cadre2 = Frame(frame4, bg="white")
cadre2.pack()
nom = Label(cadre1, text="Nom:", font=("Courrier", 12), bg="white", fg="#292b2c")
nom.grid(row=1, column=0, sticky=E, padx=5, pady=5)
prenom = Label(cadre1, text="Prenom:", font=("Courrier", 12), bg="white", fg="#292b2c")
prenom.grid(row=2, column=0, sticky=E, padx=5, pady=5)
poste = Label(cadre1, text="Poste:", font=("Courrier", 12), bg="white", fg="#292b2c")
poste.grid(row=4, column=0, sticky=E, padx=5, pady=5)
service = Label(cadre1, text="Service:", font=("Courrier", 12), bg="white", fg="#292b2c")
service.grid(row=3, column=0, sticky=E, padx=5, pady=5)
photo = Label(cadre1, text="aucune image choisie", bg="white", fg="#292b2c",
              width="25")
photo.grid(row=5, column=1, sticky=E, padx=5, pady=5)

nomEntry1 = Entry(cadre1, bg="white", fg="#292b2c",
                 width="25"
                 # ,height="2"
                 )
nomEntry1.grid(row=1, column=1, sticky=E, padx=5, pady=5)
prenomEntry1 = Entry(cadre1, bg="white", fg="#292b2c",
                    width="25")
prenomEntry1.grid(row=2, column=1, sticky=E, padx=5, pady=5)
posteEntry1 = Entry(cadre1, bg="white", fg="#292b2c",
                   width="25")
posteEntry1.grid(row=4, column=1, sticky=E, padx=5, pady=5)
serviceEntry1 = Entry(cadre1, bg="white", fg="#292b2c",
                     width="25")
serviceEntry1.grid(row=3, column=1, sticky=E, padx=5, pady=5)
photoEntry = Button(cadre1, text="Choisir la photo", command=choisir, bg="white", fg="#48c1e6"
                    , border="0"
                    )
photoEntry.grid(row=5, column=0, sticky=E, padx=5, pady=5)

enregistrer = Button(cadre2, text="Enregistrer", command=valider, fg="#292b2c", bg="#48c1e6"
                     , width="10"
                     , height="2"
                     , border=0
                     )
enregistrer.grid(row=1, column="0")
annuler = Button(cadre2, text="Annuler", command=annuler1, fg="#292b2c", bg="#48c1e6"
                 , width="10"
                 , height="2"
                 , border=0
                 )
annuler.grid(row=1, column="1")

# ajout patient
cadre11 = Frame(frame3, bg="white")
cadre11.pack(padx="200", pady="50")
cadre22 = Frame(frame3, bg="white")
cadre22.pack()
nom = Label(cadre11, text="Nom:", font=("Courrier", 12), bg="white", fg="#292b2c")
nom.grid(row=1, column=0, sticky=E, padx=5, pady=5)
prenom = Label(cadre11, text="Prenom:", font=("Courrier", 12), bg="white", fg="#292b2c")
prenom.grid(row=2, column=0, sticky=E, padx=5, pady=5)
adresse = Label(cadre11, text="Adresse:", font=("Courrier", 12), bg="white", fg="#292b2c")
adresse.grid(row=3, column=0, sticky=E, padx=5, pady=5)
contact = Label(cadre11, text="Contact:", font=("Courrier", 12), bg="white", fg="#292b2c")
contact.grid(row=4, column=0, sticky=E, padx=5, pady=5)
service = Label(cadre11, text="Service:", font=("Courrier", 12), bg="white", fg="#292b2c")
service.grid(row=5, column=0, sticky=E, padx=5, pady=5)

nomEntry = Entry(cadre11, bg="white", fg="#292b2c",
                 width="25")
nomEntry.grid(row=1, column=1, sticky=E, padx=5, pady=5)
prenomEntry = Entry(cadre11, bg="white", fg="#292b2c",
                    width="25")
prenomEntry.grid(row=2, column=1, sticky=E, padx=5, pady=5)
adresseEntry = Entry(cadre11, bg="white", fg="#292b2c",
                     width="25")
adresseEntry.grid(row=3, column=1, sticky=E, padx=5, pady=5)
contactEntry = Entry(cadre11, bg="white", fg="#292b2c",
                     width="25")
contactEntry.grid(row=4, column=1, sticky=E, padx=5, pady=5)
serviceEntry = Entry(cadre11, bg="white", fg="#292b2c",
                     width="25")
serviceEntry.grid(row=5, column=1, sticky=E, padx=5, pady=5)

Senregistrer = Button(cadre22, text="Enregistrer", command=valider2, fg="#292b2c", bg="#48c1e6"
                     , width="10"
                     , height="2"
                     , border=0
                     )
Senregistrer.grid(row=0, column=0)
Sannuler = Button(cadre22, text="annuler", command=annuler, fg="#292b2c", bg="#48c1e6"
                 , width="10"
                 , height="2"
                 , border=0
                 )
Sannuler.grid(row=0, column=1)


#list medecin
table1 = ttk.Treeview(frame1,column=("column1","column2","column3","column4","column5"),show='headings')
table1.heading("#1",text="ID")
table1.heading("#2",text="Nom")
table1.heading("#3",text="Prénom")
table1.heading("#4",text="Poste")
table1.heading("#5",text="Service")

table1['show']='headings'
table1.pack()

load= Image.open("C:/Users/ASUS/Downloads/fichier/sary/hospital.png")
load.thumbnail((200,200))
photo= ImageTk.PhotoImage(load)
label_image=Label(frame1,image=photo)
label_image.place(x=0,y=250)
supp= Button(frame1,text="Suppression",bg="red",command=supp)
supp.place(x=1000,y=250)
Vframe =Frame(frame1,bg="white")


#liste patient
table = ttk.Treeview(frame2,column=("column1","column2","column3","column4","column5","column6"),show='headings')
table.heading("#1",text="Id")
table.heading("#2",text="Nom")
table.heading("#3",text="Prénom")
table.heading("#4",text="Adresse")
table.heading("#5",text="Contact")
table.heading("#6",text="Service")

table['show']='headings'
supp= Button(frame2,text="Suppression",bg="red",command=supp2)
supp.place(x=0,y=200)

table.pack()




window.mainloop()
