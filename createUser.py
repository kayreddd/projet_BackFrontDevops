from pydantic import BaseModel
import sqlite3
from bcrypt import hashpw, gensalt

# Définir un modèle Pydantic pour la validation des données d'entrée
class UserCreate(BaseModel):
    mail: str
    password: str

# Fonction pour créer un compte
def create_user(user: UserCreate):
    try:
         # Hasher le mot de passe
        hashed_password = hashpw(user.password.encode('utf-8'), gensalt()).decode('utf-8')
        # Connexion à la base de données SQLite
        conn  = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        # Commande SQL pour insérer un nouvel utilisateur avec le mot de passe hashé
        cursor.execute("""
        INSERT INTO user (mail, password) 
        VALUES (?, ?)
        """, (user.mail, hashed_password))  # Utilisation des données du modèle

        # Sauvegarder les changements et fermer la connexion
        conn.commit()
        conn.close()

        return {"message": f"Compte avec {user.mail} et id_user {user.password} créé avec succès!"}

    except Exception as e:
        return {"error": str(e)}
    

