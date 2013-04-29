##########################################
# Alfred - Flask version
#  Custom CMS for Mutaku
#  Matthew Martz 2013
##########################################

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('local_settings')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return reder_template('404.html'), 404

# register blueprints now
