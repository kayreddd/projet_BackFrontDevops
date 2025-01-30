import { useState } from 'react'
import TransactionForm from "./TransactionForm";
import Register from "./Register";
import Beneficiaire from "./BeneficiaireForm";
import './App.css'

import Transactions from "./transaction";

function App() {

  return (
    <>
      <div>
        <h1>Envoyer une Transaction</h1>
        <TransactionForm/>
      </div>
      <div>
        <h1>créer un user</h1>
        <Register/>
      </div>
      <div>
        <h1>créer un beneficiaire</h1>
        <Beneficiaire/>
      </div>
      <div>
        <Transactions userId={1} /> {/* Remplace 1 par l'ID de ton utilisateur */}
      </div>
    </>
  )
}

export default App;

