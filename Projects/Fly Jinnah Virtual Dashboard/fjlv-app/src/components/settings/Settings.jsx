import "./Settings.css";
import Footer from "../footer/Footer";

const Settings = () => {
    return (
        <>
            <div className="Settings news-cycle-bold">
                <div className="settings-title">
                    <h1>Administrator Settings</h1>
                </div>
                <div className="flex-con-row">
                    <div className="flex-col">
                        <h2>Account</h2>
                        <ul className="settings-list">
                            <li className="settings-item-con">Update name
                                {/* <label className="switch">
                                    <input type="checkbox" />
                                    <span className="slider"></span>
                                </label> */}
                                <input className="update-text-input" type="text" />
                            </li>
                            <li className="settings-item-con">Update password
                                {/* <label className="switch">
                                    <input type="checkbox" />
                                    <span className="slider"></span>
                                </label> */}
                                <input className="update-text-input" type="password" />
                            </li>
                            <li className="settings-item-con">Do not disturb
                                <label className="switch">
                                    <input type="checkbox" checked/>
                                    <span className="slider"></span>
                                </label>
                            </li>
                            <li className="settings-item-con">Update email
                                <input className="update-text-input" type="email"/>
                            </li>
                        </ul>
                    </div>
                    <div className="flex-col">
                        <h2>UI/UX</h2>
                        <ul className="settings-list">
                            <li className="settings-item-con">Dark mode
                                <label className="switch">
                                    <input type="checkbox" checked />
                                    <span className="slider"></span>
                                </label>
                            </li>
                            <li className="settings-item-con">Imperial units
                                <label className="switch">
                                    <input type="checkbox" />
                                    <span className="slider"></span>
                                </label>
                            </li>
                            <li className="settings-item-con">24HR time format
                                <label className="switch">
                                    <input type="checkbox" />
                                    <span className="slider"></span>
                                </label>
                            </li>
                        </ul>
                    </div>
                    <div className="flex-col">
                        <h2>Airline Operations</h2>
                        <ul className="settings-list">
                            <li className="settings-item-con">Deactivate all pilots
                                <label className="switch">
                                    <input type="checkbox" />
                                    <span className="slider"></span>
                                </label>
                            </li>
                            <li className="settings-item-con">Deactivate all schedules
                                <label className="switch">
                                    <input type="checkbox" />
                                    <span className="slider"></span>
                                </label>
                            </li>
                            <li className="settings-item-con">24HR time format
                                <label className="switch">
                                    <input type="checkbox" />
                                    <span className="slider"></span>
                                </label>
                            </li>
                        </ul>
                    </div>
                    <div className="flex-col">
                        <h2>Stats</h2>
                        <ul className="settings-list">
                            <li className="settings-item-con">Item 1
                                <label className="switch">
                                    <input type="checkbox" />
                                    <span className="slider"></span>
                                </label>
                            </li>
                            <li className="settings-item-con">Item 1
                                <label className="switch">
                                    <input type="checkbox" />
                                    <span className="slider"></span>
                                </label>
                            </li>
                            <li className="settings-item-con">Item 1
                                <label className="switch">
                                    <input type="checkbox" />
                                    <span className="slider"></span>
                                </label>
                            </li>
                        </ul>
                    </div>
                </div>
                <div className="carousel-wrapper">
                    <div className="carousel-item-con">36 active flights</div>
                    <div className="carousel-item-con">152 total pilots</div>
                    <div className="carousel-item-con">74 schedules</div>
                    <div className="carousel-item-con">5 bookings</div>
                    <div className="carousel-item-con">19 filed PIREPs</div>
                    <div className="carousel-item-con">55 aircrafts in fleet</div>
                    <div className="carousel-item-con">3 awaiting messages</div>
                    <div className="carousel-item-con">2 aircrafts in maintenance</div>
                    <div className="carousel-item-con">1 LOA requests</div>
                    <div className="carousel-item-con">41 active aircrafts</div>
                </div>
            </div>
            <Footer />
        </>
    );
}

export default Settings;