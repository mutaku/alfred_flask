# views.py

from alfred import app

@app.route("/")
def index():
    '''
    Default index view
    '''
    return "Hello, world!"

@app.route("/add")
@login_required
def add():
    '''
    Add a new post
    '''
    return "Let's add a new post!"
