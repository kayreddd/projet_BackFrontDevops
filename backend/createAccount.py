from pydantic import BaseModel
import random

import sqlite3

#Fonction pour générer un IBAN aléatoire
def generate_iban():
    country_code = "FR"
    bank_code = "30003"
    branch_code = "01234"
    accountnumber = "".join(str(random.randint(0, 9)) for _ in range(11))
    rib_key = str(random.randint(10, 99))
    return f"{country_code}{bank_code}{branch_code}{accountnumber}{rib_key}"

#Définir un modèle Pydantic pour la validation des données d'entrée
class CompteCreate(BaseModel):
    id_user: int
    type_de_compte: str

# Fonction pour créer un compte
def create_account(compte: CompteCreate):
    try:
        # Connexion à la base de données SQLite
        iban = generate_iban()  # Générer un IBAN
        conn  = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        # Commande SQL pour insérer un nouvel utilisateur
        cursor.execute("""
        INSERT INTO compte (money, id_user, statut_compte, iban) 
        VALUES (?, ?, ?, ?)
        """, (0, compte.id_user, compte.type_de_compte, iban))  # Utilisation des données du modèle

        # Sauvegarder les changements et fermer la connexion
        conn.commit()
        conn.close()

        return {"message": f"Compte créé avec succès! IBAN: {iban}", "iban": iban}

    except Exception as e:
        return {"error": str(e)}
