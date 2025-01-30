import React, { useState, useEffect } from 'react';
import axios from 'axios';  // Importation d'Axios
import './Accounts.css';  // Importation du CSS

function Accounts() {
  const [accounts, setAccounts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchAccounts = async () => {
      setLoading(true);
      try {
        // Utilisation d'Axios pour faire la requête
        const response = await axios.post("http://127.0.0.1:8000/show_accounts", {
          id_user: 1,  // Remplacer par un ID utilisateur valide
        });

        

        // Vérification et formatage des données
        const formattedAccounts = response.data.accounts.map((account) => ({
          id: account.id,
          type_de_compte: account.type_de_compte,
          money: account.money,
          iban: account.iban, // Assurez-vous que 'iban' existe dans la réponse
        }));

        setAccounts(formattedAccounts);  // Mettre à jour l'état avec les comptes formatés
      } catch (error) {
        setError(error.message || "Erreur lors de la récupération des comptes");
      } finally {
        setLoading(false);
      }
    };

    fetchAccounts();
  }, []);

  // Calcul du total des actifs
  const totalAssets = accounts.reduce((total, account) => total + account.money, 0);

  return (
    <div className="App">
      <header>
        <button className="add-account-btn">Ajouter un compte</button>
        <h1>Mes Comptes</h1>
        <h2 className="total-assets">Total des actifs : {totalAssets} €</h2>
      </header>
      <main>
        {loading ? (
          <p>Chargement des comptes...</p>
        ) : error ? (
          <p className="error">Erreur : {error}</p>
        ) : (
          <div className="account-container">
            {accounts.length === 0 ? (
              <p>Aucun compte trouvé.</p>
            ) : (
              accounts.map((account) => (
                <div key={account.iban} className="account-card">
                  <h2>{account.type_de_compte}</h2>
                  <p><strong>IBAN :</strong> {account.iban}</p>
                  <p><strong>Solde :</strong> {account.money} €</p>
                  <button onClick={() => alert(`Transactions du compte ${account.iban}`)}>
                    Transactions
                  </button>
                </div>
              ))
            )}
          </div>
        )}
      </main>
    </div>
  );
}

export default Accounts;
