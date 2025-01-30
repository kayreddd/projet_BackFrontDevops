import React from 'react';
import './App.css';
import Accounts from "./Accounts";
import CreateAccount from './CreateAccount';

  // Import du composant Accounts

function App() {
  return (
    <div className="App">
      <Accounts /> 
      <CreateAccount/>
  
    </div>
  );
}

export default App;
