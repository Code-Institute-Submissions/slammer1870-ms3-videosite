from flask import Flask, session, g, redirect, url_for, flash, render_template, request, abort
import uuid
from datetime import datetime

from werkzeug.urls import url_parse
from passlib.hash import pbkdf2_sha256
from main import db
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
        if db.users.find_one({"email": user['email']}):
            flash("User already exists", "bg-red-400")
            return False

        # Creates the new user and starts session
        if db.users.insert_one(user):
            self.start_session(user)
            flash("Thank you for registering, you are now logged in!", "bg-green-400")
            return True

    # Login method
    def login(self, form):

        user = db.users.find_one({
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
        db.users.update_one({"_id": user['_id']}, {"$set": user})
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


