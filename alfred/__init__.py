##########################################
# Alfred - Flask version
#  Custom CMS for Mutaku
#  Matthew Martz 2013
##########################################

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore

app = Flask(__name__)
app.config.from_object('local_settings')

db = SQLAlchemy(app)

from alfred import models, views

@app.errorhandler(404)
def not_found(error):
    return reder_template('404.html'), 404

security_ds = SQLAlchemyUserDatastore(db,
        models.User,
        models.Role)
app.security = Security(app, security_ds)

@app.before_first_request
def before_first_request():
    try:
        models.db.create_all()
    except Exception, e:
        app.logger.error(str(e))


