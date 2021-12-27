from flask import Flask, session, g, redirect, url_for, flash, render_template, request, abort
import uuid
from datetime import datetime

from werkzeug.urls import url_parse
from passlib.hash import pbkdf2_sha256
import app
import os
import requests
from urllib.parse import urlparse


# Define User class


class User:

    # Method to start a new session
    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        g.user = user
        return 200

    # User object register method
    def register(self, form):

        # Create the user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": form.name.data,
            "email": form.email.data,
            "password": form.password.data
        }

        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(form.password.data)

        # Check for existing email address
        if app.db.users.find_one({"email": user['email']}):
            flash("User already exists", "bg-red-400")
            return False

        # Creates the new user and starts session
        if app.db.users.insert_one(user):
            self.start_session(user)
            flash("Thank you for registering, you are now logged in!", "bg-green-400")
            return True

    # Login method
    def login(self, form):

        user = app.db.users.find_one({
            "email": form.email.data
        })

        # Checks that encrypted password is valid
        if user and pbkdf2_sha256.verify(form.password.data, user['password']):
            self.start_session(user)
            flash("Welcome back, you are now logged in!", "bg-green-400")
            return True

        return flash("Invalid login credentials", "bg-red-400")

    # Logout method
    def logout(self):
        session.clear()
        flash("You have been succesfully logged out", "bg-green-400")
        return redirect(url_for('index'))

    # Method to set a user as admin
    def set_admin(self, user):
        user['admin'] = True
        app.db.users.update_one({"_id": user['_id']}, {"$set": user})
        return True


# Make  request to the Vimoe API to retireve a thumbnail by parsing the video id

def set_thumbnail(url):

    parsed = urlparse(url)

    id = parsed.path.split('/')[-1]

    endpoint = "https://vimeo.com/api/v2/video/{}.json".format(id)
    data = {"ip": "1.1.2.3"}
    headers = {"Authorization": "Bearer {}".format(
        os.environ.get("VIMEO_ACCESS_TOKEN"))}

    res = requests.get(endpoint)
    thumbnail = res.json()[0]['thumbnail_large']
    return thumbnail


class Post:

    def __init__(self, title=None, description=None, url=None, category=None, difficulty=None):
        self.title = title
        self.description = description
        self.url = url
        self.category = category
        self.difficulty = difficulty

    def create(self, form):
        post = {
            "_id": uuid.uuid4().hex,
            "created_at": datetime.now(),
            "title": form.title.data,
            "description": form.description.data,
            "url": form.url.data,
            "thumbnail": set_thumbnail(form.url.data),
            "category": form.category.data,
            "difficulty": form.difficulty.data,
            "section": form.section.data
        }

        app.db.posts.insert_one(post)
        return True

    # Post edit method
    def edit(self, id, form):
        app.db.posts.find_one_and_update(
            {"_id": id}, {"$set": {"updated_at": datetime.now(),
                                   "title": form.title.data,
                                   "description": form.description.data,
                                   "url": form.url.data,
                                   "thumbnail": set_thumbnail(form.url.data),
                                   "category": form.category.data,
                                   "difficulty": form.difficulty.data,
                                   "section": form.section.data}})
        return True

    # Post delete method
    def delete(self, id):
        app.db.posts.delete_one({"_id": id})
        return True

    def __str__(self):
        return f"{self.title} by {self.author}"
