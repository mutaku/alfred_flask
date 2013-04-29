# decorators.py

from functools import wraps
from flask import g, flash, redirect, url_for, request

def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            flash(u'You must be logged in.')
            return redirect(url_for('alfred.login',
                next=request.path))
        return f(*args, **kwargs)
    return decorated_function
