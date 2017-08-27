import glob
import os
import re
from rdcom_website.settings import ARTICLES_PATH, ARTICLES_METADATA_LINES


def get_articles():
    # Get all articles
    # ...
    article_files = glob.glob(ARTICLES_PATH + '/*.md')
    articles = []
    for file in article_files:
        article_data = {
            "name": os.path.basename(file),
            "path": file
        }
        article_metadata = get_article_metadata(file)
        article_data.update(article_metadata)
        articles.append(article_data)
    # Order them by date
    # ...
    return article_files


def get_article_metadata(article_file):
    with open(article_file) as article_file:
        data = article_file.readlines()
        if len(data) > ARTICLES_METADATA_LINES:
            metadata = {}
            metadata_list = data[:ARTICLES_METADATA_LINES]
            search_pattern = re.compile("^#@([a-z]+): ?([a-zA-Z0-9-_ !?]+)$")
            for line in metadata_list:
                r = search_pattern.findall(line)
                if len(r) == 1:
                    metadata[r[0][0]] = r[0][1]
        else:
            metadata = {}
    return metadata
