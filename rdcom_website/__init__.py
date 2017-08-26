from flask import Flask
from flask import request
from flask import render_template

from rdcom_website.settings import ARTICLES_PATH

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'nav_items': ['About', 'Projects']
    }
    return render_template("index.html", **context)


@app.route('/blog')
def blog():
    return render_template("index.html")


@app.route('/article/<string:post_name>')
def article(post_name):
    return render_template("index.html")


def get_articles():
    # Get all articles
    # ...

    # Order them by date
    # ...
    return []
