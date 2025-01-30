from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import logging

app = FastAPI()

# Configurer les logs
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Modèle Pydantic pour valider les données d'entrée
class UserRequest(BaseModel):
    id_user: int

def showAccount(id_user):
    try:
        logger.debug(f"Tentative de connexion à la base de données avec l'id_user: {id_user}")
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        # Exécution de la requête SQL pour récupérer les comptes
        logger.debug("Exécution de la requête SQL pour récupérer les comptes...")
        cursor.execute("SELECT * FROM compte WHERE id_user = ? ORDER BY id DESC", (id_user,))
        rows = cursor.fetchall()
        logger.debug(f"Résultats de la requête: {rows}")
        
        # Fermer la connexion
        conn.close()

        # Si la table est vide
        if not rows:
            return {"message": "La table 'compte' est vide."}

        # Retourner les données sous forme de liste de dictionnaires
        return {"accounts": [{"id": row[0], "money": row[1], "id_user": row[2], "type_de_compte": row[3], "iban": row[4]} for row in rows]}

    except sqlite3.DatabaseError as e:
        logger.error(f"Erreur de base de données: {str(e)}")
        return {"error": f"Erreur de base de données: {str(e)}"}
    except Exception as e:
        logger.error(f"Erreur inconnue: {str(e)}")
        return {"error": f"Erreur inconnue: {str(e)}"}