from flask import Flask
from flask import request
from flask import render_template

from rdcom_website.blog import get_articles

app = Flask(__name__)
app.config.from_object('rdcom_website.settings')  # See: http://flask.pocoo.org/docs/0.12/config/#development-production
app.config.from_pyfile('env.py')


@app.route('/')
def index():
    articles = get_articles()
    context = {
        'site_title': app.config.get('SITE_TITLE'),
        'articles': articles
    }
    return render_template("index.html", **context)


@app.route('/blog')
def blog():
    articles = get_articles()
    context = {
        'site_title': app.config.get('SITE_TITLE'),
        'page_title': 'Blog',
        'articles': articles
    }
    return render_template("index.html")


@app.route('/article/<string:post_name>')
def article(post_name):
    return render_template("index.html")
