# app.py
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["blog_db"]
posts_collection = db["posts"]

@app.route("/api/posts", methods=["GET"])
def get_posts():
    posts = list(posts_collection.find({}, {"_id": 0}))
    return jsonify(posts)

if __name__ == "__main__":
    app.run(debug=True)