from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

DB_URL = env.get('SQLALCHEMY_DATABASE_URL')

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + DB_URL
db = SQLAlchemy(app)