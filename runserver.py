"""
This script runs the fl application using a development server.
"""
from os import environ
from views import app  # Import the Flask app from views.py

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '0.0.0.0')  # Use 0.0.0.0 for cloud deployment
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))  # Default to 5000
    except ValueError:
        PORT = 5000
    app.run(host=HOST, port=PORT)
