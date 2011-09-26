from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy

UPLOAD_FOLDER='/Users/lcruzc/develop/igualitos/uploads'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
