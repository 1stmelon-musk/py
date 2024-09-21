from flask import render_template, redirect, url_for, flash, session, request
from app import app  # Import the Flask app instance from __init__.py
from flask_socketio import SocketIO, emit

# Initialize SocketIO
socketio = SocketIO(app)

# Define the correct code (you can replace this with your logic for validation)
VALID_CODE = 'ttrw'

# Route for the index page
@app.route('/')
def index():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    return render_template('index.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        code = request.form.get('code')
        if code == VALID_CODE:
            session['authenticated'] = True
            return redirect(url_for('index'))
        else:
            flash('Invalid code', 'error')
    return render_template('login.html')

# SocketIO event handler for color changes
@socketio.on('color_change')
def handle_color_change(data):
    emit('color_update', data, broadcast=True)

# If you want to add more routes, you can define them here.
# For example:
@app.route('/logout')
def logout():
    session.pop('authenticated', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

# Ensure to run socketio when you launch the app from runserver.py
if __name__ == '__main__':
    socketio.run(app)
