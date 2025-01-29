import sqlite3

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
        cursor.execute("SELECT * FROM transaction2 WHERE id_sender = ? OR id_receveur = ?  ",( account_id, account_id))
        rows = cursor.fetchall()
        liste = []
        liste.append(rows)
        cursor.execute("SELECT * FROM historic WHERE id_user = ?  ",(account_id))
        rows = cursor.fetchall()
        liste.append(rows)
        # Fermer la connexion
        conn.close()

        # Si la table est vide
        if not rows:
            return {"message": "Aucune transaction trouvée pour cet utilisateur."}

        # Retourner les données sous forme de liste de dictionnaires
        return liste

    except Exception as e:
        return {"error": str(e)}