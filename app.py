from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import os

TENOR_API_KEY = os.getenv("TENOR_API_KEY")

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

@app.route('/reviews')
def show_reviews():
    """Show Recommedations"""
    return render_template('show_reviews.html', reviews = reviews.find())

@app.route('/reviews/create_new', methods=['POST'])
def create_review():
    """Create a New Review"""
    review = {
        'title': request.form.get('title'),
        'name': request.form.get('name'),
        'content': request.form.get('content'),
    }
    review_id = reviews.insert_one(review).inserted_id
    return redirect(url_for('show_reviews.html', review=review, review_id=review_id))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))