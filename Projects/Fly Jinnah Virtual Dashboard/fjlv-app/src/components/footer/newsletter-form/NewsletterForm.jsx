import "./NewsletterForm.css";

const NewsletterForm = () => {
    return (
        <>
            <form className="NewsletterForm">
                <label>Email</label>
                <input type="email" placeholder="johndoe@email.com" />
                <button>Subscribe</button>
            </form>
            <p className="message">We would love to get in touch! Please be on the lookout for ticket promotions and stay up to date with the latest from FJL ❤️</p>
        </>
    );
}

export default NewsletterForm;