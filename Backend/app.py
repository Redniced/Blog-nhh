# filepath: c:\Users\sbpau\.vscode\Blog\Backend\app.py
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from pymongo.errors import ConnectionFailure
from bson.objectid import ObjectId
from flask import request
from datetime import datetime 

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

@app.route("/api/blogs/<string:title>")
def get_blog_by_title(title):
    blog = posts_collection.find_one({"title": title}, {"_id": 0})
    if blog:
        return jsonify(blog)    
    else:
        return jsonify({"error": "Blog not found"}), 404

@app.route("/api/blogs", methods=["POST"])
def create_blog():
    data = request.json

    # Validate required fields
    if "title" not in data or "content" not in data:
        return jsonify({"error": "Title and content are required"}), 400

    # Build the blog document
    blog = {
        "_id": ObjectId(),  # Automatically generate a unique ObjectId
        "title": data["title"],
        "content": data["content"],
        "author": data.get("author", "Anonymous"),  # Default if not provided
        "timestamp": data.get("timestamp", datetime.timestamp()),  # Use current time if not provided
        "created_at": data.get("created_at", datetime.timestamp())  # Optional, fallback to now
    }

    # Insert into MongoDB
    posts_collection.insert_one(blog)

    # Return the inserted blog (optional)
    return jsonify({
        "message": "Blog created successfully",
        "blog": {
            "_id": str(blog["_id"]),
            "title": blog["title"],
            "author": blog["author"],
            "timestamp": blog["timestamp"].isoformat(),
            "created_at": blog["created_at"].isoformat()
        }
    }), 201

if __name__ == "__main__":
    app.run(debug=True)