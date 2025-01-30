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

function App() {

  return (
    <>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={""} /> 
        <Route path="/transactions" element={<Transactions userId={1} />} /> 
        <Route path="/transaction_form" element={<TransactionForm />} />
        <Route path="/beneficiaire" element={<BeneficiaireForm />} />
        <Route path="/register" element={<Register />} />


      </Routes>
    </BrowserRouter>
    <div className="App">
      <Accounts /> 
      <CreateAccount/>
  
    </div>
  </>
  );
    
}

export default App;

