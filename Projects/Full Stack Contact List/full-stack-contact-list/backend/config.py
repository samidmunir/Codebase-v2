from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# - cross origin request
#   - allows us to send a request to his backend by a different URL.
#   - different server of front-end compared to server of back-end.
#   - takes of CORS error.

# initializing Flask application.
app = Flask(__name__)
# wrapping app in CORS to allow cross origin requests.
CORS(app)

# database initialization.
# - specifying the location of the local SQL database on our machine.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
# - not going to track the modifications to our database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# creating a database instance (giving CRUD operations on the database above).
# - this is an ORM (object-relational-mapping)
db = SQLAlchemy(app)