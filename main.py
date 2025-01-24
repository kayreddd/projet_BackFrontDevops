from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi import HTTPException
#import asyncio


# # from fastapi.staticfiles import StaticFiles pour le css
# from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from createAccount import create_account  # Importez la fonction depuis createAccount.py
from createUser import create_user
from showUser import showUser
from showAccount import showAccount
from addMoney import addMoney
from transaction import create_transaction
from transaction import updateTransaction
from showTransaction import showTransaction
from closeAccount import close_account
from showBeneficiaire import addBeneficiaire
from showBeneficiaire import showBeneficiaire



app = FastAPI()

#app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurer Jinja2 pour les templates
# templates = Jinja2Templates(directory="template")

# Route pour afficher une page HTML
# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     return templates.TemplateResponse("home.html", {"request": request, "title": "Page d'accueil"})

# Définir un modèle Pydantic pour la validation des données d'entrée
class CompteCreate(BaseModel):
    money: int
    id_user: int

class UserCreate(BaseModel):
    mail: str
    password: str

class transactionCreate(BaseModel):
    montant: int
    id_sender: int
    id_receveur: int
    statut: str
    message: str

class BeneficiaireCreate(BaseModel):
    name_beneficiaire: str
    id_beneficiaire: str

# Route pour créer un compte
@app.post("/create_account")
async def create_account_route(compte: CompteCreate):
    try:
        # Appeler la fonction create_account depuis createAccount.py
        result = create_account(compte)  # On passe l'objet CompteCreate

        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])

        return result  # Renvoie le message de succès

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Route pour créer un user
@app.post("/create_user")
async def create_user_route(user: UserCreate):
    try:
        # Appeler la fonction create_account depuis createAccount.py
        result = create_user(user)  # On passe l'objet CompteCreate

        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])

        return result  # Renvoie le message de succès

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/show_accounts")
async def get_accounts(id_user):
    # Connexion à la base de données
    result = showAccount(id_user)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result  # Renvoie le message de succès 

@app.post("/show_user")
async def get_user(id_user):
    # Connexion à la base de données
    result = showUser(id_user)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result  # Renvoie le message de succès 

# Route pour ajouter de l'argent à un compte
@app.post("/add_money")
async def add_money_route(id_compte, montant):
    try:
        # Appeler la fonction create_account depuis createAccount.py
        result = addMoney(id_compte, montant)  # On passe l'objet CompteCreate

        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])

        return result  # Renvoie le message de succès

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/create_transaction")
async def create_transaction_route(transaction: transactionCreate):
    try:
        # Appeler la fonction create_account depuis createAccount.py
        result = create_transaction(transaction)  # On passe l'objet CompteCreate

        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])

        return result  # Renvoie le message de succès

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/update_transaction")
async def update_transaction_route():
    # Connexion à la base de données
    result = updateTransaction()
        
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result  # Renvoie le message de succès


@app.post("/show_transaction")
async def get_transaction(account_id):
    # Connexion à la base de données
    result = showTransaction(account_id)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result  # Renvoie le message de succès

@app.post("/close_account")
async def get_close_account(account_id):
    # Connexion à la base de données
    result = close_account(account_id)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result  # Renvoie le message de succès


@app.post("/add_beneficiaire")
async def add_beneficiaire_route(beneficiaire: BeneficiaireCreate, id_user):
    try:
        result = addBeneficiaire(beneficiaire.name_beneficiaire, beneficiaire.id_beneficiaire, id_user)

        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])

        return result  # Renvoie le message de succès

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/show_beneficiare")
async def get_beneficiaire(id_user):
    # Connexion à la base de données
    result = showBeneficiaire(id_user)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result  # Renvoie le message de succès


#pour que la fonction ne s'execute que toutes les 10 sec auto

# @app.on_event("startup")
# async def start_background_task():
#     asyncio.create_task(run_update_transaction_periodically())


# async def run_update_transaction_periodically():
#     while True:
#         result = await updateTransaction()  # Appelle la fonction
#         if "error" in result:
#             print(f"Erreur : {result['error']}")
#         else:
#             print("Mise à jour réussie.")
#         await asyncio.sleep(10)  # Attends 10 secondes avant de recommencer