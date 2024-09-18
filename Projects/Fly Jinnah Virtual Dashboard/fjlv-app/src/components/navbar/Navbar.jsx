import "./Navbar.css";

const Navbar = () => {
  return (
    <div className="Navbar">
      <div className="navbar-title-con">
        <h1 className="navbar-title great-vibes-regular">Fly Jinnah Virtual</h1>
      </div>
      <div className="navbar-items-con news-cycle-regular">
        <ul className="navbar-items">
            <li className="active-item">Dashboard</li>
            <li className="navbar-item">Schedules</li>
            <li className="navbar-item">Bookings</li>
            <li className="navbar-item">NOTAMs</li>
            <li className="navbar-item">Settings</li>
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