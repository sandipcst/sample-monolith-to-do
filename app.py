# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In a real application, this would interact with a database
users = {}
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = {'password': password}
            return redirect(url_for('login'))
        else:
            return "User already exists!"
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            return f"Welcome, {username}!"
        else:
            return "Invalid credentials!"
    return render_template('login.html')

@app.route('/add_todo', methods=['POST'])
def add_todo():
    todo_item = request.form['todo']
    todos.append(todo_item)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
