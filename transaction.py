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
        rows = cursor.fetchall()
        for row in rows:
            if row[1] == 1:
                return row[1],
            test = row[1],
            return test # Retourner toute la ligne (tuple)
        else:  # Si aucune ligne ne correspond
            return {"message": "Aucune ligne trouvée avec 'pending'"}
        
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.close()