import "./Navbar.css";

const Navbar = ({activeNavItem, setActiveNavItem}) => {
  return (
    <div className="Navbar">
      <div className="navbar-title-con">
        <h1 className="navbar-title great-vibes-regular">Fly Jinnah Virtual</h1>
      </div>
      <div className="navbar-items-con news-cycle-regular">
        <ul className="navbar-items">
            <li className={activeNavItem === 1 ? "active-item" : "navbar-item"} onClick={() => setActiveNavItem(1)}>Dashboard</li>
            <li className={activeNavItem === 2 ? "active-item" : "navbar-item"} onClick={() => setActiveNavItem(2)}>Schedules</li>
            <li className={activeNavItem === 3 ? "active-item" : "navbar-item"} onClick={() => setActiveNavItem(3)}>Bookings</li>
            <li className={activeNavItem === 4 ? "active-item" : "navbar-item"} onClick={() => setActiveNavItem(4)}>NOTAMs</li>
            <li className={activeNavItem === 5 ? "active-item" : "navbar-item"} onClick={() => setActiveNavItem(5)}>Settings</li>
        </ul>
      </div>
      <div className="navbar-controls-con news-cycle-regular">
        <p className="navbar-controls-message">Welcome, Rahameen K.</p>
        <button className="navbar-controls-button">Logout</button>
      </div>
    </div>
  );
};

export default Navbar;