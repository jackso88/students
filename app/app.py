from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch
import asyncio

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)
es = Elasticsearch(hosts=["http://127.0.0.1:9200"])
loop = asyncio.new_event_loop()

