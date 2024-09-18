import { useState } from 'react';
import './App.css';
import Navbar from './components/navbar/Navbar';

function App() {
  const [activeNavItem, setActiveNavItem] = useState(1);

  const handleSetActiveNavItem = (itemNum) => {
    setActiveNavItem(itemNum);
  }

  return (<Navbar activeNavItem={activeNavItem} setActiveNavItem={setActiveNavItem} />)
}

export default App;
