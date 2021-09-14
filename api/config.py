from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

DB_URI = env.get('DATABASE_URI')

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + DB_URI
db = SQLAlchemy(app)

# Fix error due to Azure's filesystem
# from sqlalchemy import create_engine
# from sqlalchemy import event

# engine = create_engine('sqlite:///' + DB_URL)
# def set_sqlite_pragma(dbapi_con, con_record):
#     dbapi_con.execute('PRAGMA journal_mode=WAL')
# event.listen(engine, 'connect', set_sqlite_pragma)