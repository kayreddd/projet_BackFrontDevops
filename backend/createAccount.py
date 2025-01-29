from pydantic import BaseModel

import sqlite3

# Définir un modèle Pydantic pour la validation des données d'entrée
class CompteCreate(BaseModel):
    money: int
    id_user: int

# Fonction pour créer un compte
def create_account(compte: CompteCreate):
    try:
        # Connexion à la base de données SQLite
        conn  = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        # Commande SQL pour insérer un nouvel utilisateur
        cursor.execute("""
        INSERT INTO compte (money, id_user, statut_compte, iban) 
        VALUES (?, ?, ?, ?)
        """, (0, compte.id_user, "Secondaire", compte.id_user))  # Utilisation des données du modèle

        # Sauvegarder les changements et fermer la connexion
        conn.commit()

        return {"message": f"Compte avec {compte.money} et id_user {compte.id_user} créé avec succès!"}

    except Exception as e:
        return {"error": str(e)}
