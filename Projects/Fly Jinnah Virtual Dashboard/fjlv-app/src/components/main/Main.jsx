import "./Main.css";
import Dashboard from "../dashboard/Dashboard";
import Schedules from "../schedules/Schedules";
import Bookings from "../bookings/Bookings";
import Notams from "../notams/Notams";
import Settings from "../settings/Settings";

const Main = ({activeNavItem}) => {
    return (
        <div className="Main">
            {activeNavItem === 1 && <Dashboard />}
            {activeNavItem === 2 && <Schedules />}
            {activeNavItem === 3 && <Bookings />}
            {activeNavItem === 4 && <Notams />}
            {activeNavItem === 5 && <Settings />}
        </div>
    );
}

export default Main;