import glob
import os
from rdcom_website.settings import ARTICLES_PATH


def get_articles():
    # Get all articles
    # ...
    article_files = glob.glob(ARTICLES_PATH + '/*.md')
    articles = []
    for file in article_files:
        article_content_path = file
        article_name = os.path.basename(file)
        articles.append({
            "name": article_name,
            "path": article_content_path
        })
    # Order them by date
    # ...
    return article_files
