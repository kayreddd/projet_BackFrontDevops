import { useState } from 'react'
import TransactionForm from "./TransactionForm";
import Register from "./Register";
import Beneficiaire from "./BeneficiaireForm";
import './App.css'
import { BrowserRouter } from 'react-router-dom';
import { Route,Routes } from 'react-router-dom';
import React from 'react';
import Transactions from "./transaction";
import TestPage from './test';
import BeneficiaireForm from './BeneficiaireForm';
import Accounts from './Accounts';
import CreateAccount from './CreateAccount';
import './Accounts.css'

function App() {

  return (
    <>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={""} /> 
        <Route path="/transactions" element={<Transactions />} /> 
        <Route path="/transaction_form" element={<TransactionForm />} />
        <Route path="/beneficiaire" element={<BeneficiaireForm />} />
        <Route path="/register" element={<Register />} />
        <Route path='/account' element={<Accounts />} />
        <Route path='/create_account' element={<CreateAccount />} />
        

      </Routes>
      {/* <div className="App">
          <Accounts /> 
          <CreateAccount/>
      </div>   */}
    </BrowserRouter>
    
  </>
  );
    
}

export default App;

