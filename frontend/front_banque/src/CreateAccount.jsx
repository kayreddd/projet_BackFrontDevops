import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Import du hook useNavigate
import './Accounts.css';


function CreateAccount() {
  
  const [typeDeCompte, setTypeDeCompte] = useState('Principal');
  const [iban, setIban] = useState('');
  const [error, setError] = useState('');
  const [showForm, setShowForm] = useState(false);
  const navigate = useNavigate(); // Hook pour la navigation

  const handleCreateAccount = async (e) => {
    e.preventDefault();

    try {
      // Log avant d'envoyer la requête pour déboguer
      console.log({
        type_de_compte: typeDeCompte,
        id_user: 1,
      });

      const response = await fetch('http://localhost:8000/create_account', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          id_user: 1,
          type_de_compte: typeDeCompte,
        }),
      });

      const data = await response.json();
      console.log(data); // Log de la réponse du serveur

      if (response.ok) {
        alert(`Compte créé avec succès! IBAN: ${data.iban}`);
        setIban(data.iban);
      } else {
        setError(data.error || 'Une erreur est survenue.');
      }
    } catch (error) {
      setError('Erreur lors de la création du compte');
    }
  };

  return (
    <div>
      <button onClick={() => navigate('/beneficiaire', { state: { id: 1 } })}>
        Ajouter un bénéficiaire
      </button>
      <button className="add-account-btn" onClick={() => setShowForm(!showForm)}>
        Ajouter un compte
      </button>

      {showForm && (
        <div className="overlay">
          <div className="create-account-form">
            <h2>Créer un compte</h2>
            <form onSubmit={handleCreateAccount}>
              <br />
              <label>Type de compte :</label>
              <select
                value={typeDeCompte}
                onChange={(e) => setTypeDeCompte(e.target.value)}
                required
              >
                <option value="Principal">Courant</option>
                <option value="Secondaire">Epargne</option>
              </select>
              <br />
              <button type="submit">Créer le compte</button>
            </form>
            {iban && <p>IBAN : {iban}</p>}
            {error && <p className="error">{error}</p>}
            <button className="close-btn" onClick={() => setShowForm(false)}>Fermer</button>
          </div>
          <div></div>
        </div>
      )}
    </div>
  );
}

export default CreateAccount;
