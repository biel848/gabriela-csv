import csv
import random
import string


def llegir_dades_csv(nom_arxiu):
    estudiants = []
    with open(nom_arxiu, mode="r", encoding="utf-8") as fitxer:
        lector = csv.DictReader(fitxer)
        for fila in lector:
            estudiants.append(fila)
    return estudiants
def llegir_dades_csv(nom_arxiu):
    print("llegir dades csv")

def generar_mail(nom, cognoms):
    email =f"{nom}.{cognoms}@insgabrielamistral.cat".lower().replace(" ","")                         

def generar_contraseña():    
    print("generar contrasenya")

def escriure_csv(estudiants, nom_arxiu):
    print("escriure csv")

def generar_contraseña():
    caracters = string.ascii_letters + string.digits
    contrasenya = "".join(random.choice(caracters) for _ in range(10))

# Exemple D'us Del Programa
nom_arxiu_estudiants = "estudiants_nous.csv"
estudiants = llegir_dades_csv("nom_arxiu_entradas")
for estudiant in estudiants:
    estudiants["email"] = generar_mail(estudiant["nom"], estudiant["cognoms"])
    estudiants["contrasenya"] = generar_contraseña()

print(estudiants)
