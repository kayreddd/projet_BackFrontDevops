import sqlite3
import json
from fastapi import APIRouter

router = APIRouter()


@router.get("/transactions/{transaction_id}/{user_id}")
def showTransaction(transaction_id, user_id):
    try:
         
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        # on récupère toutes les lignes de la table 'transaction2'
        cursor.execute("SELECT * FROM transaction2 WHERE id = ? AND (id_sender = ? OR id_receveur = ?)  ",(transaction_id, user_id, user_id))
        rows = cursor.fetchone()
        # Fermer la connexion
        conn.commit()
        conn.close()

        # Si la table est vide
        if not rows:
            return {"message": "Aucune transaction trouvée pour cet utilisateur."}

        # on retourne les données sous forme de liste de dictionnaires
        return {"id":rows[0], "id_sender": rows[1], "id_receveur": rows[2], "type_transaction": rows[3], "valeur_transaction": rows[4], "message": rows[5],"date": rows[6]}
    
    except Exception as e:
        return {"error": str(e)}


@router.get("/transactions/{account_id}")
def showAllTransaction(account_id: int):
    try:
            
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        # On récupère toutes les lignes de la table 'historic'
        cursor.execute("SELECT * FROM historic WHERE id_user = ?  ",(account_id,))
        rows = cursor.fetchall()
        # Fermer la connexion
        conn.close()
        keys = ["id", "id_user", "type", "value", "date_transaction", "iban", "message","id_transaction", "etat"]
        transactions = [dict(zip(keys, row)) for row in rows]
        # Si la table est vide
        if not transactions:
            return {"message": "Aucune transaction trouvée pour cet utilisateur."}

        # On retourne les données sous forme de liste de dictionnaires
        return transactions

    except Exception as e:
        return {"error": str(e)}