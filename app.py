from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import os

app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/goloo')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
restroom = db.restroom
reviews = db.reviews 



@app.route('/')
def hompage():
    """Show Hompage"""
    return render_template('base.html')
