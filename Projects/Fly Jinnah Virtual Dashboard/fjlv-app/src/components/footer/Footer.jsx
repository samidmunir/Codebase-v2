import "./Footer.css";
import NewsletterForm from "./newsletter-form/NewsletterForm";

const Footer = () => {
    return (
        <div className="Footer">
            <div className="footer-flex-con news-cycle-regular">
                <div className="footer-col">
                    <h2>Directory</h2>
                    <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Corporis atque, saepe omnis quae quas, suscipit veniam dignissimos alias vero exercitationem ab maxime, asperiores quis ullam itaque impedit voluptatibus eius illo.</p>
                </div>
                <div className="footer-col">
                    <h2>About Us</h2>
                    <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Corporis atque, saepe omnis quae quas, suscipit veniam dignissimos alias vero exercitationem ab maxime, asperiores quis ullam itaque impedit voluptatibus eius illo.</p>
                </div>
                <div className="footer-col">
                    <h2>Quick Links</h2>
                    <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Corporis atque, saepe omnis quae quas, suscipit veniam dignissimos alias vero exercitationem ab maxime, asperiores quis ullam itaque impedit voluptatibus eius illo.</p>
                </div>
                <div className="footer-col">
                    <h2>Contact Us</h2>
                    <NewsletterForm />
                </div>
            </div>
            <p className="footer-note news-cycle-regular">Munir Code Forge | Est. 2024</p>
        </div>
    );
}

export default Footer;