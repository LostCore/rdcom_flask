import glob
import os
from rdcom_website.settings import ARTICLES_PATH, ARTICLES_METADATA_LINES


def get_articles():
    # Get all articles
    # ...
    article_files = glob.glob(ARTICLES_PATH + '/*.md')
    articles = []
    for file in article_files:
        article_content_path = file
        article_name = os.path.basename(file)
        article_metadata = get_article_metadata(file)
        articles.append({
            "name": article_name,
            "path": article_content_path
        })
    # Order them by date
    # ...
    return article_files


def get_article_metadata(article_file):
    with open(article_file) as article_file:
        data = article_file.readlines()
        if len(data) > ARTICLES_METADATA_LINES:
            metadata_list = data[:ARTICLES_METADATA_LINES]

        else:
            metadata = {}
    return metadata

