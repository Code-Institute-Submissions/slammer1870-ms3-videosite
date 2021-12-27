from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import pymongo

from forms import RegisterForm, LogInForm, PostForm
import models


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# Database
client = pymongo.MongoClient(os.environ.get("MONGO_URI"))
db = client[str(os.environ.get("DB_NAME"))]


# Render index page with all posts
@app.route("/")
def index():
    posts = db.posts.find().limit(12)
    return render_template("index.html", posts=posts)

@app.route('/register/', methods=['POST', 'GET'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():  
        user = models.User()
        if user.register(form):
            return redirect(url_for('index'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
