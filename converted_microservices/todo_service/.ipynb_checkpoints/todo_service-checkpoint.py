# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# In a real application, this would interact with a database
todos = []

@app.route('/add_todo', methods=['POST'])
def add_todo():
    todo_item = request.json['todo']
    todos.append(todo_item)
    return jsonify({'message': 'Todo added successfully'})

@app.route('/get_todos', methods=['GET'])
def get_todos():
    return jsonify({'todos': todos})

if __name__ == '__main__':
    app.run(debug=True)