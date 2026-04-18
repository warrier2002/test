import os
import json
import uuid
import hashlib
from flask import Flask, request, jsonify, redirect, url_for, render_template, send_from_directory
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://harshitkumr9_db_user:Yk5i0hPdyCwTBvjq@test.z5qn1mj.mongodb.net/")
try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)
    # Ping the server to validate connection on start
    client.admin.command('ping')
    db = client['assignment_db']
    collection = db['submissions']
    todo_collection = db['todo_items']
except Exception as e:
    print(f"Warning: MongoDB connection failed on startup: {e}")
    db = None
    collection = None
    todo_collection = None

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
        
        # Additional fields from Part 4
        item_id = request.form.get('itemID')
        
        todo_data = {
            "itemName": item_name,
            "itemDescription": item_description,
            "itemID": item_id
        }
        
        todo_collection.insert_one(todo_data)
        return redirect(url_for('success'))
    except Exception as e:
        return render_template('todo.html', error=str(e))

@app.route('/viewdata')
def view_data():
    return render_template('viewdata.html')

@app.route('/api/alldata', methods=['GET'])
def get_all_data():
    try:
        subs = []
        if collection is not None:
            for doc in collection.find():
                doc.pop('_id', None)
                subs.append(doc)
        todos = []
        if todo_collection is not None:
            for doc in todo_collection.find():
                doc.pop('_id', None)
                todos.append(doc)
        return jsonify({"submissions": subs, "todos": todos})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
