from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import pymongo

from forms import RegisterForm, LogInForm, PostForm
import models

from wraps import admin_required, login_required

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

@app.route('/login/', methods=['POST', 'GET'])
def login():
    form = LogInForm(request.form)
    print("request initiated", form)
    if request.method == 'POST' and form.validate():  
        print("validated")
        user = models.User()
        if user.login(form):
            print("logged in")
            return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/logout/')
@login_required
def logout():
    user = models.User()
    return user.logout()

# Render category page with all posts in that category
@app.route("/videos/<difficulty>/<section>/")
def category(section, difficulty):
    posts = db.posts.find({"section": section, "difficulty": difficulty})
    return render_template("category.html", posts=posts, difficulty=difficulty, section=section)

# Render lesson page with all videos in that lesson


@app.route("/videos/<difficulty>/<category>/<lesson>/")
def lesson(category, difficulty, lesson):
    posts = db.posts.find({"category": category, "difficulty": difficulty})
    lesson = db.posts.find_one({"_id": lesson})
    return render_template("lesson.html", posts=posts, lesson=lesson)

if __name__ == '__main__':
    app.run(debug=True)
