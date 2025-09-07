# filepath: c:\Users\sbpau\.vscode\Blog\Backend\app.py
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
CORS(app)

# Connect to MongoDB using the connection string from .env
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["blognhh"]
posts_collection = db["posts"]

@app.route("/api/posts", methods=["GET"])
def get_posts():
    posts = list(posts_collection.find({}, {"_id": 0}))
    return jsonify(posts)

if __name__ == "__main__":
    app.run(debug=True)