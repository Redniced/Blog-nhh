# filepath: c:\Users\sbpau\.vscode\Blog\Backend\app.py
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from pymongo.errors import ConnectionFailure 

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
CORS(app)

# Connect to MongoDB using the connection string from .env
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["blognhh"]
posts_collection = db["posts"]
print("Mongo URI:", mongo_uri)


@app.route("/api/posts", methods=["GET"])
def get_posts():
    posts = list(posts_collection.find({}, {"_id": 0}))
    return jsonify(posts)

@app.route("/status")
def status():
    try:
        # The ping command is cheap and doesn't require auth beyond connection
        client.admin.command('ping')
        return jsonify({
            "status": "ok",
            "message": "Connected to MongoDB successfully"
        })
    except Exception as e:  
        return jsonify({
            "status": "error",
            "message": f"MongoDB connection failed: {str(e)}"
        }), 500

@app.route("/api/blogs/latest")
def get_latest_blogs():
    latest = posts_collection.find().sort("created_at", -1).limit(5)
    return jsonify([{
        "title": blog["title"],
        "content": blog["content"],
        "created_at": blog["created_at"]
    } for blog in latest])


if __name__ == "__main__":
    app.run(debug=True)