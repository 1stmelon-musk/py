
from flask import Flask

app = Flask(__name__, template_folder='../templates')  # Adjust the path if necessary
app.secret_key = 'your_secret_key'  # Replace with a real secret key

# Import routes after initializing the app
from app import routes

