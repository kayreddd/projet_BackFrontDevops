import { useState } from 'react'
import './App.css'

import Transactions from "./transaction";

function App() {
  return (
    <div>
      <Transactions userId={2} /> {/* Remplace 1 par l'ID de ton utilisateur */}
    </div>
  );
}

export default App;

