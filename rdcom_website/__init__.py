from flask import Flask
from flask import request
from flask import render_template

from rdcom_website.blog import get_articles, get_article_content, get_article_file, get_article, parse_article_content

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
    for k, article_entry in enumerate(articles):  # https://stackoverflow.com/questions/9152431/iterating-over-list-of-dictionaries
        article_content = get_article_content(article_entry.get('path'))
        article_content = parse_article_content(article_content)
        articles[k].update({'content': article_content})
    context = {
        'site_title': 'Blog - '+app.config.get('SITE_TITLE'),
        'page_title': 'Blog',
        'articles': articles
    }
    return render_template("blog.html", **context)


@app.route('/article/<string:post_name>')
def article(post_name):
    article_file = get_article_file(post_name)
    article_content = get_article_content(article_file)
    article_content = parse_article_content(article_content)
    the_article = get_article(article_file)
    context = {
        'site_title': the_article.get('title')+' - '+app.config.get('SITE_TITLE'),
        'page_title': the_article.get('Blog'),
        'article': the_article,
        'article_content': article_content
    }
    return render_template("article.html", **context)
