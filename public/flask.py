from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
app.config['DEBUG'] = True

# Connect to the SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create a table for user registration if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstName TEXT,
    lastName TEXT,
    email TEXT,
    password TEXT
)''')
conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    email = request.form['email']
    password = request.form['password']

    # Insert user registration data into the database
    c.execute('INSERT INTO users (firstName, lastName, email, password) VALUES (?, ?, ?, ?)', (firstName, lastName, email, password))
    conn.commit()

    return 'Registration successful'

if __name__ == '__main__':
    app.run()
