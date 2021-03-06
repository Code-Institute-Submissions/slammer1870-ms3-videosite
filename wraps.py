from functools import wraps
from flask import session, request, redirect, url_for
from flask.helpers import flash


# Login Required Decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            flash("You must be logged in to access", "bg-red-400")
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# Admin Required Decorator


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin' not in session['user']:
            flash("You must be an admon in to access", "bg-red-400")
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function
