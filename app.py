from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import pymongo


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# Database
client = pymongo.MongoClient(os.environ.get("MONGO_URI"))
db = client[str(os.environ.get("DB_NAME"))]


# Render index page with all posts and hero video
@app.route("/")
def index():
    posts = db.posts.find().limit(12)
    return render_template("index.html", posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
