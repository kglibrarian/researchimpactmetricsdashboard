import os 

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or "secret_string"
    SQLALCHEMY_DATABASE_URI = {'sqlite:///static/db/researchimpactreview.sqlite'}
