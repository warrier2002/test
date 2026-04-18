import os
import json
import uuid
import hashlib
from flask import Flask, render_to_directory, request, jsonify, redirect, url_for, render_template
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://placeholder:uri@cluster0.mongodb.net/test?retryWrites=true&w=majority")
client = MongoClient(MONGO_URI)
db = client['assignment_db']
collection = db['submissions']
todo_collection = db['todo_items']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def get_api_data():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = {
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "message": request.form.get('message')
        }
        
        # Insert into MongoDB
        collection.insert_one(data)
        return redirect(url_for('success'))
    except Exception as e:
        # If error, stay on same page and show error
        return render_template('index.html', error=str(e))

@app.route('/success')
def success():
    return render_template('success.html')

# Part 3 & 4 routes (Placeholder for now, will be committed in respective branches/merges)
@app.route('/todo')
def todo_page():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    try:
        # Base fields from Part 3
        item_name = request.form.get('itemName')
        item_description = request.form.get('itemDescription')
        
        # Additional fields from Part 4 (IDs, UUID, Hash)
        item_id = request.form.get('itemID')
        item_uuid = request.form.get('itemUUID')
        item_hash = request.form.get('itemHash')
        
        todo_data = {
            "itemName": item_name,
            "itemDescription": item_description,
            "itemID": item_id,
            "itemUUID": item_uuid,
            "itemHash": item_hash
        }
        
        todo_collection.insert_one(todo_data)
        return jsonify({"status": "success", "message": "To-Do item stored in MongoDB"}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
# Backend enhancement 1.0
