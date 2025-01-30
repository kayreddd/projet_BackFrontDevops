from pydantic import BaseModel
import sqlite3

class BeneficiaireCreate(BaseModel):
    name_beneficiaire: str
    id_beneficiaire: int
    id_user: int

def showBeneficiaire(id_user):
    try:

        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        # Récupérer toutes les lignes de la table 'compte'
        cursor.execute("SELECT * FROM beneficiaire WHERE id_beneficiant = ?", (id_user,))
        rows = cursor.fetchall()
        print(rows)
        # Fermer la connexion
        conn.close()

        # Si la table est vide
        if not rows:
            return {"message": "La table 'beneficiaire' est vide."}

        # Retourner les données sous forme de liste de dictionnaires
        return {"accounts": [{"id": row[0], "name_beneficiare": row[1], "id_beneficiaire": row[2],"id_beneficiant": row[3], "date_transaction": row[4]} for row in rows]}

    except Exception as e:
        return {"error": str(e)}

def addBeneficiaire(beneficiaire: BeneficiaireCreate):
    try:
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM compte WHERE id = ?", (beneficiaire.id_beneficiaire,))
        row = cursor.fetchone()
        #vérifier si le compte que l'on veut bénéficiaire existe bien
        if not row:
            return {"message": f"Le compte du bénéficiaire que vous chercher à créer n'existe pas"}
        # Vérifier si le bénéficiaire existe déjà
        cursor.execute("SELECT id FROM beneficiaire WHERE name_beneficiaire = ? AND id_beneficiant = ?", (beneficiaire.name_beneficiaire,beneficiaire.id_user))
        if cursor.fetchone():
            return {"message": f"Le bénéficiaire '{beneficiaire.name_beneficiaire}' est déjà enregistré."}

        # Ajouter le bénéficiaire
        cursor.execute("""
            INSERT INTO beneficiaire (name_beneficiaire, id_beneficiaire, id_beneficiant) 
            VALUES (?,?, ?)
        """, (beneficiaire.name_beneficiaire, beneficiaire.id_beneficiaire, beneficiaire.id_user))

        conn.commit()
        conn.close()

        return {"message": f"Bénéficiaire '{beneficiaire.name_beneficiaire}' ajouté avec succès."}

    except Exception as e:
        return {"error": str(e)}
