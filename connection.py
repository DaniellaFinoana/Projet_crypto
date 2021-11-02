import  mysql.connector


def connection():
     try:
         conn = mysql.connector.connect(host="localhost",
                                        user="root",
                                        password="",
                                        database="projet")
         print("connection Milay mifandray Okay")

         return conn

     except:
         print("tsy milay  fa tsy mifandray")




def ajout(personne):
    conn = connection()
    cursor=conn.cursor()
    #nom,prenom,service,poste,photo

    valeurs = {"nom": personne.nom, "prenom": personne.prenom,"contact":personne.contact,"adresse":personne.adresse,"photo":personne.photo, "poste": personne.poste, "service": personne.service}
    cursor.execute("""INSERT INTO personne (nom,prenom,adresse,contact,photo,poste,service) VALUES(%(nom)s, %(prenom)s,%(adresse)s,%(contact)s,%(photo)s,%(poste)s,%(service)s)""", valeurs)
    conn.commit()
    conn.close()

def parcourirM():
    conn = connection()
    cursor = conn.cursor()

    cursor.execute(""" SELECT idpers,nom,prenom,poste,service FROM personne WHERE adresse='0' """)
    rows = cursor.fetchall()
    return rows

    conn.close()
def parcourirP():
    conn = connection()
    cursor = conn.cursor()

    cursor.execute(""" SELECT idpers,nom,prenom,adresse,contact,service FROM personne  where poste='0' order by idpers desc""")
    rows = cursor.fetchall()
    return rows

    conn.close()
def delete(a):
    conn = connection()
    cursor=conn.cursor()
    cursor.execute("""delete from personne where idpers={}""".format(a))
    conn.commit()
def voir(a):
    conn = connection()
    cursor=conn.cursor()
    cursor.execute("""SELECT photo from personne where idpers={}""".format(a))
    rows = cursor.fetchall()
    conn.commit()
    return rows
