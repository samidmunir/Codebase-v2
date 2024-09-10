from config import db

# creating the Contact class
# - inherits from db.Model (a database model)
# - can describe the different fields in the database as a Python object.
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80), unique = False, nullable = False)
    last_name = db.Column(db.String(80), unique = False, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)

    # this function will convert our Contact object into a JSON object
    def to_json(self):
        return {
                "id": self.id, 
                "firstName": self.first_name, 
                "lastName": self.last_name, 
                "email": self.email
        }