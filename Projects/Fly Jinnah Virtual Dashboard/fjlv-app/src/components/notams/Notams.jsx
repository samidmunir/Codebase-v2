import "./Notams.css";
import Footer from "../footer/Footer";
import notams_data from "../../data/notams/notams_data";

const Notams = () => {
    const notams = notams_data;
    return (
        <>
            <div className="Notams news-cycle-bold">
                <div className="notams-title-con">
                    <h1 className="notams-title">NOTAMs</h1>
                </div>
                <div className="notams-flex-con">
                    {/* <div className="notams-info-con">
                        <h2>Quick Overview</h2>
                        <h3>{new Date().toLocaleTimeString()}</h3>
                        <p>Total # of NOTAMS: 7</p>
                        <p># of Acknowledged NOTAMs: 33</p>
                        <p># of Unacknowledged NOTAMs: 5</p>
                        <div className="recent-notam-con">
                            <h4>Recent NOTAM</h4>
                            <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Eos nihil asperiores adipisci </p>
                            <button className="news-cycle-bold">View</button>
                        </div>
                    </div> */}
                    <div className="notams-carousel-con">
                        {notams.map((notam) => {
                            return (
                                <div key={notam.notam_id}>
                                    <p>{notam.notam_mssg}</p>
                                </div>
                            )
                        })}
                    </div>
                </div>
                <div className="create-notam-form-con">
                    <h2>Create a new NOTAM</h2>
                    <form>
                        <label>New NOTAM</label>
                        <input type="text" placeholder="Enter NOTAM..." maxLength={2500} />
                        <label>Recieve by</label>
                        <select>
                            <option>To All</option>
                            <option>To Staff</option>
                            <option>To Pilots</option>
                        </select>
                        <label>Require Acknowledgement</label>
                        <input type="checkbox" defaultChecked/>
                    </form>
                </div>
            </div>
            <Footer />
        </>
    );
}

export default Notams;