from flask import Flask
from flask_cors import CORS
#import config from Config
from flask_sqlalchemy import SQLAlchemy

#################################################
## Flask Initialization
## __name__ is the name of the module where 
## flask will look for modules
#################################################
app = Flask(__name__)
CORS(app)
#app.run(debug=True)
#app.config.from_object(Config)
app.config['SECRET_KEY'] = '2345612342534dkekgksle1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/researchimpactreview.sqlite'
db = SQLAlchemy(app)

###############################################
## Import other things below app initialization
###############################################
# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()
from application import analysis
from application import models
from application import routes


