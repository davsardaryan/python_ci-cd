# app.py

from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://bestMongoDB:27017/")
db = client.dockerized_app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    data = list(db.test.find())

    # Convert ObjectId to string for JSON serialization
    for entry in data:
        entry['_id'] = str(entry['_id'])

    print("MongoDB Data:", data)  # Debugging print
    return jsonify(data)

@app.route('/submit', methods=['POST'])
def submit_data():
    data = {
        'name': request.form['name'],
        'surname': request.form['surname'],
        'age': int(request.form['age'])
    }
    db.test.insert_one(data)
    return render_template('index.html', message='Data submitted successfully!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

