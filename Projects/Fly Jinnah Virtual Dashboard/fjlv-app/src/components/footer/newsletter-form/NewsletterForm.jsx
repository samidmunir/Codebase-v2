import "./NewsletterForm.css";

const NewsletterForm = () => {
    return (
        <form className="NewsletterForm">
            <label>Email</label>
            <input type="email" placeholder="johndoe@email.com" />
            <button>Subscribe</button>
        </form>
    );
}

export default NewsletterForm;