import { useState } from 'react';
import './App.css';
import Navbar from './components/navbar/Navbar';
import Main from './components/main/Main';

function App() {
  const [activeNavItem, setActiveNavItem] = useState(1);

  const handleSetActiveNavItem = (itemNum) => {
    setActiveNavItem(itemNum);
  }

  return (
    <>
      <Navbar activeNavItem={activeNavItem} setActiveNavItem={handleSetActiveNavItem} />
      <Main activeNavItem={activeNavItem} />
    </>
  )
}

export default App;
