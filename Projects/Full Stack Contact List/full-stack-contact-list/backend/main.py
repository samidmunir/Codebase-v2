# CRUD
# - create
#   - id
#   - firstName
#   - lastName
#   - email
# - read
# - update
#   - id
# - delete
#   - id

# CRUD endpoints
#   localhost:5000/create_contact
#   localhost:5000/contacts
#   localhost:5000/update_contact/{id}
#   localhost:5000/delete_contact/{id}

# Request
# - type (GET, POST, PATCH, DELETE)
# - JSON (data that comes alongside a request)
#   - JSON is an object of key/value pairs

# Response
# - status (success, error/failure)

from flask import request, jsonify
from config import app, db
from models import Contact

@app.route("/contacts", methods = ["GET"])
def get_contacts():
    # getting all the different contacts in our database (Python objects).
    contacts = Contact.query.all()
    # for each Python Contact object -> convert to JSON using to_json() function.
    json_contacts = list(map(lambda contact: contact.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

@app.route("/create_contact", methods = ["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return jsonify({"message": "You must include a first name, last name, and email."}), 400
    new_contact = Contact(first_name = first_name, last_name = last_name, email = email)
    try:
        # staging area (ready to write to database).
        db.session.add(new_contact)
        # write whatever in staging area to the database.
        # - encapsulate within try/catch block to handle any errors.
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    return jsonify({"message": "User created!"}), 201

@app.route("/update_contact/<int:user_id>", methods = ["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)
    if not contact:
        return jsonify({"message": "User not found."}), 404
    
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "User updated."}), 200

@app.route("/delete_contact/<int:user_id>", methods = ["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)
    if not contact:
        return jsonify({"message": "User not found."}), 404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted."}), 200

if __name__ == "__main__":
    # instantiating database
    # - when we start the application, get the context.
    # - then create all the different models defined in our database.
    #   - spin up the database if not already existing.
    with app.app_context():
        db.create_all()
    app.run(debug = True)