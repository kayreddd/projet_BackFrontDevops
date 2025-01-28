from pydantic import BaseModel

import sqlite3

# Définir un modèle Pydantic pour la validation des données d'entrée
class TransactionCreate(BaseModel):
    montant: int
    id_sender: int
    id_receveur: int
    statut: str
    message: str

# Fonction pour créer un compte
def create_transaction(transaction: TransactionCreate):
    try:
        if (transaction.montant  < 0):
            return {"message":"transaction impossible, montant négatif"}
        
        elif (transaction.id_receveur  == transaction.id_sender):
            return {"message":"transaction impossible, receveur et envoyeur sont la même personne"}
        # Connexion à la base de données SQLite
        conn  = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        # Commande SQL pour insérer un nouvel utilisateur
        cursor.execute("""
        INSERT INTO transaction2 (valeur_transaction, id_sender, id_receveur, type_transaction, message) 
        VALUES (?, ?, ?, ?, ?)
        """, (transaction.montant, transaction.id_sender, transaction.id_receveur, "pending", transaction.message))  # Utilisation des données du modèle

        # Sauvegarder les changements et fermer la connexion
        conn.commit()
        conn.close()

        return {"message": f"transaction de {transaction.id_sender} vers {transaction.id_receveur} d'un montant de {transaction.montant} a été créé avec succès!"}

    except Exception as e:
        return {"error": str(e)}
    
def updateTransaction():
    try:
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        
        # Récupérer uniquement la première ligne correspondante
        cursor.execute("SELECT * FROM transaction2 WHERE type_transaction = 'pending'")
        transactions = cursor.fetchall()
        for transaction in transactions:
            cursor.execute("SELECT money FROM compte WHERE id = ?",(str(transaction[1])))
            money_left = cursor.fetchone()
            if (money_left[0] > transaction[4]):

                left = money_left[0] - transaction[4] # soustraction du montant d'argent qui va être donné
                
                cursor.execute("UPDATE compte SET money = ? WHERE id = ?", (left, str(transaction[1])))
                cursor.execute("SELECT money FROM compte WHERE id = ?",(str(transaction[2]))) # récupération de l'argent du receveur
                money_done = cursor.fetchone()
                done = money_done[0] + transaction[4]
                cursor.execute("UPDATE compte SET money = ? WHERE id = ?", (done, str(transaction[2])))
                cursor.execute("""
                INSERT INTO historic (id_user, type_transaction, valeur_transaction) 
                VALUES (?, ?, ?)
                """, (str(transaction[1]), "envoie de l'argent vers", str(transaction[4])))
                cursor.execute("""
                INSERT INTO historic (id_user, type_transaction, valeur_transaction) 
                VALUES (?, ?, ?)
                """, (str(transaction[2]), "reçoit de l'argent de", str(transaction[4])))

                cursor.execute("UPDATE transaction2 SET type_transaction = ? WHERE id = ?", ("done", str(transaction[0])))
                
            else:
                cursor.execute("UPDATE transaction2 SET type_transaction = ? WHERE id = ?", ("no money", str(transaction[0])))
        conn.commit()
        return ("terminé sans accroc")
        
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.close()

def cancelTransaction(id_transaction):

    conn  = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT type_transaction FROM transaction2 WHERE id = '?'", (id_transaction))
    transaction = cursor.fetchone()
    if transaction and transaction[0] == "pending":
        cursor.execute("UPDATE transaction2 SET type_transaction = ? WHERE id = ?", ("cancel", id_transaction))
    conn.commit()
    conn.close()

    return ("transaction annulé")

