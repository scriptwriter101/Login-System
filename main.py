from flask import Flask, render_template, request, redirect, url_for
import os
import secrets

app = Flask(__name__)

# Get the signup secret from the environment
SIGNUP_SECRET = os.getenv('SIGNUP_SECRET')

# ... (rest of the code will go here)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        secret = request.form.get('secret')

        if secret == SIGNUP_SECRET:
            # Store the username (e.g., in a file or database)
            # ... (Replace this with your actual storage mechanism)
            with open('users.txt', 'a') as f:
                f.write(f'{username}\n')
            return redirect(url_for('login'))
        else:
            error = 'Invalid secret!'
            return render_template('index.html', error=error)
    else:
        return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        # ... (Get the user's ID and roles using Replit Auth)
        user_id = request.headers.get('X-Replit-User-Id')
        user_name = request.headers.get('X-Replit-User-Name')
        user_roles = request.headers.get('X-Replit-User-Roles')

        # Verify if the user exists (replace with your storage method)
        if username in open('users.txt').read().splitlines():
            return render_template('login.html', user_id=user_id, user_name=user_name, user_roles=user_roles)
        else:
            error = 'Invalid username!'
            return render_template('index.html', error=error)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
  
from flask import Flask, render_template, request, redirect, url_for
import os
import secrets

app = Flask(__name__)

# Get the signup secret from the environment
SIGNUP_SECRET = os.getenv('SIGNUP_SECRET')

# ... (rest of the code will go here)# ... (previous code)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        secret = request.form.get('secret')

        if secret == SIGNUP_SECRET:
            # Store the username (e.g., in a file or database)
            # ... (Replace this with your actual storage mechanism)
            with open('users.txt', 'a') as f:
                f.write(f'{username}\n')
            return redirect(url_for('login'))
        else:
            error = 'Invalid secret!'
            return render_template('index.html', error=error)
    else:
        return render_template('index.html')# ... (previous code)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        # ... (Get the user's ID and roles using Replit Auth)
        user_id = request.headers.get('X-Replit-User-Id')
        user_name = request.headers.get('X-Replit-User-Name')
        user_roles = request.headers.get('X-Replit-User-Roles')

        # Verify if the user exists (replace with your storage method)
        if username in open('users.txt').read().splitlines():
            return render_template('login.html', user_id=user_id, user_name=user_name, user_roles=user_roles)
        else:
            error = 'Invalid username!'
            return render_template('index.html', error=error)
    else:
        return render_template('index.html')



