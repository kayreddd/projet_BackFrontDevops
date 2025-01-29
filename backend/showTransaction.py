import sqlite3
import json

def showTransaction(transaction_id, user_id):
    try:
         
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        # Récupérer toutes les lignes de la table 'compte'
        cursor.execute("SELECT * FROM transaction2 WHERE id = ? AND (id_sender = ? OR id_receveur = ?)  ",(transaction_id, user_id, user_id))
        rows = cursor.fetchone()
        # Fermer la connexion
        conn.commit()
        conn.close()

        # Si la table est vide
        if not rows:
            return {"message": "Aucune transaction trouvée pour cet utilisateur."}

        # Retourner les données sous forme de liste de dictionnaires
        return {"id":rows[0], "id_sender": rows[1], "id_receveur": rows[2], "type_transaction": rows[3], "valeur_transaction": rows[4], "message": rows[5],"date": rows[6]}
    
    except Exception as e:
        return {"error": str(e)}
    
def showAllTransaction(account_id):
    try:
            
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        # Récupérer toutes les lignes de la table 'compte'
        cursor.execute("SELECT * FROM historic WHERE id_user = ?  ",(account_id))
        rows = cursor.fetchall()
        # Fermer la connexion
        conn.close()
        keys = ["id", "id_user", "type", "value", "date_transaction", "iban", "message"]
        transactions = [dict(zip(keys, row)) for row in rows]
        # Si la table est vide
        if not transactions:
            return {"message": "Aucune transaction trouvée pour cet utilisateur."}

        # Retourner les données sous forme de liste de dictionnaires
        return transactions

    except Exception as e:
        return {"error": str(e)}