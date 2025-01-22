from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi import HTTPException

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
async def get_accounts():
    # Connexion à la base de données
    result = showAccount()
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result  # Renvoie le message de succès 

@app.post("/show_user")
async def get_accounts():
    # Connexion à la base de données
    result = showUser()
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

account_id = 1
@app.post("/show_transaction")
async def get_transaction():
    # Connexion à la base de données
    result = showTransaction(account_id)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result  # Renvoie le message de succès