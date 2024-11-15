import os
import gridfs
from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)

mongo_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongo_uri)
db = client['Baseball']
collection = db['game_records']
fs = gridfs.GridFS(db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    date = request.form.get('date')
    teams = [team.strip() for team in request.form.get('teams').split(',')]
    location = request.form.get('location')
    notes = request.form.get('notes')
    files = request.files.getlist('photos')

    photo_ids = []
    for file in files:
        if file:
            file_id = fs.put(file, filename=file.filename, content_type=file.content_type)
            photo_ids.append(file_id)

    record = {
        "name": name,
        "date": datetime.strptime(date, '%Y-%m-%d'),
        "game_info": {
            "teams": teams,
            "location": location
        },
        "notes": notes,
        "photos": photo_ids
    }

    collection.insert_one(record)
    return jsonify({"message": "Record added successfully!"})

if __name__ == '__main__':
    app.run(debug=True)

