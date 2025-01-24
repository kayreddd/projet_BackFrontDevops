import sqlite3

def showBeneficiaire(id_user):
    try:

        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        # Récupérer toutes les lignes de la table 'compte'
        cursor.execute("SELECT * FROM beneficiaire WHERE id_beneficiant = ?", (id_user))
        rows = cursor.fetchall()
        print(rows)
        # Fermer la connexion
        conn.close()

        # Si la table est vide
        if not rows:
            return {"message": "La table 'beneficiaire' est vide."}

        # Retourner les données sous forme de liste de dictionnaires
        return {"accounts": [{"id": row[0], "name_beneficiare": row[1], "id_beneficiaire": row[2], "date_transaction": row[3]} for row in rows]}

    except Exception as e:
        return {"error": str(e)}


def addBeneficiaire(name_beneficiaire, id_beneficiaire, id_user):
    try:
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        # Vérifier si le bénéficiaire existe déjà
        cursor.execute("SELECT id FROM beneficiaire WHERE name_beneficiaire = ?", (name_beneficiaire,))
        if cursor.fetchone():
            return {"message": f"Le bénéficiaire '{name_beneficiaire}' est déjà enregistré."}

        # Ajouter le bénéficiaire
        cursor.execute("""
            INSERT INTO beneficiaire (name_beneficiaire, id_beneficiaire, id_beneficiant) 
            VALUES (?,?, ?)
        """, (name_beneficiaire, id_beneficiaire, id_user))

        conn.commit()
        conn.close()

        return {"message": f"Bénéficiaire '{name_beneficiaire}' ajouté avec succès."}

    except Exception as e:
        return {"error": str(e)}
