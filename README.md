import csv
import random 
import string

def llegir_dades_csv(nom_arxiu):
    estudiants = []
    with open(nom_arxiu, mode='r', encoding='utf-8') as fitxer:
        lector = csv.DictReader(fitxer)
        for fila in lector:
            estudiants.append(fila)
    return estudiants
    
def generar_mail(nom, cognoms):
    email = f"{nom}.{cognoms}@insgabrielamistral.cat".lower().replace(" ", "")
    return email

def generar_contrasenya():
    caracters = string.ascii_letters + string.digits + string.punctuation
    contrasenya = "".join(random.choice(caracters) for _ in range(10))  
    return contrasenya

# Funció per escriure les dades a un nou CSV
def escriure_csv(estudiants, nom_arxiu):
    with open(nom_arxiu, mode='w', encoding='utf-8') as fitxer:
        escritor = csv.DictWriter(fitxer, fieldnames=estudiants[0].keys())
        escritor.writeheader()
        escritor.writerows(estudiants)

# EXEMPLE D'US DEL PROGRAMA 
nom_arxiu_entrada = "estudiants_nous.csv"
nom_arxiu_sortida = "estudiants_actualitzats.csv"

estudiants = llegir_dades_csv(nom_arxiu_entrada)
for estudiant in estudiants:
    estudiant["email"] = generar_mail(estudiant["nom"], estudiant["cognoms"])
    estudiant["contrasenya"] = generar_contrasenya()

# Escriure les dades actualitzades a un nou fitxer CSV
escriure_csv(estudiants, nom_arxiu_sortida)

print(f"Dades actualitzades guardades a {nom_arxiu_sortida}.")
