from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your secret key
socketio = SocketIO(app)

# Define the correct code
VALID_CODE = 'ttrw'

@app.route('/')
def index():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    return render_template('index.html')

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

@socketio.on('color_change')
def handle_color_change(data):
    emit('color_update', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
