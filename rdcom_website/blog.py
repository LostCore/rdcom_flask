import glob
import os
import re
from datetime import date

from rdcom_website.settings import ARTICLES_PATH, ARTICLES_METADATA_LINES


def get_articles(sort=True):
    """
    Get all articles from the directory specified in settings module
    :return: List
    """
    # Get all articles
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
    if sort:
        articles.sort(key=get_article_sort_key)  # https://stackoverflow.com/questions/11848773/python-equivalent-for-phps-usort
    return articles


def get_article_sort_key(article_entry):
    """
    Retrieve the sort key to be used in articles sorting
    :param article_entry: Dict
    :return: date
    """
    # http://www.php2python.com/wiki/function.array-map/
    # http://book.pythontips.com/en/latest/map_filter.html
    # https://docs.python.org/3.5/library/datetime.html
    article_date_string = article_entry['date']
    article_date_list = list(map(int, article_date_string.split("-")))
    article_date = date(year=article_date_list[0], month=article_date_list[1], day=article_date_list[2])
    return article_date


def get_article_metadata(article_file):
    """
    Get the metadata out of an article file. The metadata are stored in the first ARTICLES_METADATA_LINES of the file.

    MAYBE I can code something more like: http://jekyllrb.com/docs/frontmatter/ in the future

    :param article_file: the absolute path to the article file
    :return: Dict
    """
    with open(article_file) as article_file:
        data = article_file.readlines()
        if len(data) > ARTICLES_METADATA_LINES:
            metadata = {}
            metadata_list = data[:ARTICLES_METADATA_LINES]
            search_pattern = re.compile("^#@([a-z]+): ?([a-zA-Z0-9-_ !?]+)$")
            for line in metadata_list:
                r = search_pattern.findall(line)
                # Here we got a LIST of TUPLES with all the string matching the pattern,
                # so in [0][0] we got the metadata name and in [0][1] we got the metadata value
                if len(r) == 1:
                    metadata[r[0][0]] = r[0][1]  # Is there a better way?
        else:
            metadata = {}
    return metadata
