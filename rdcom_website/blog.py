import glob
import os
import re
import markdown2
import itertools
from datetime import date

from rdcom_website.settings import ARTICLES_PATH, ARTICLES_METADATA_LINES

'''
Here some conventions:

article_file: the full absolute path to the article file
article_entry: the Dict representation of an article
'''


def get_articles(sort=True):
    """
    Get all articles from the directory specified in settings module
    :return: List
    """
    # Get all articles
    article_files = glob.glob(ARTICLES_PATH + '/*.md')
    articles = []
    for file in article_files:
        article_data = get_article(file)
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


def get_article(article_file):
    """
    Get an article given the filename
    :param string article_file:
    :return:
    """
    article_data = {
        "name": os.path.basename(article_file).rstrip('.md'),  # Stripping out .md
        "path": article_file
    }
    article_metadata = get_article_metadata(article_file)
    article_data.update(article_metadata)
    return article_data


def get_article_file(article_name):
    """
    Get the article file path given the article name
    :param string article_name:
    :return:
    """
    article_name = article_name+'.md'
    article_file = ARTICLES_PATH+'/'+article_name
    return article_file


def get_article_content(article_file):
    """
    Get the article content, stripping the metadata
    :param article_file:
    :return:
    """
    content = ""
    with open(article_file) as article_file:
        data = article_file.readlines()
        if len(data) > ARTICLES_METADATA_LINES:
            del data[:ARTICLES_METADATA_LINES]
            content = '\\n'.join(data)
    return content


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


def get_article_neighbours(article_entry):
    """
    Get the next and the prev article of the specified article entry
    :param Dict article_entry:
    :return Tuple:
    """
    # See: http://effbot.org/zone/python-list.htm
    # See: https://stackoverflow.com/questions/1011938/python-previous-and-next-values-inside-a-loop
    '''
    Remember: get_articles(True) returns the article sorted by date, with the [0] as the most recent article
    '''
    articles = get_articles(True)
    prev_article = None
    next_article = None
    articles_num = len(articles)
    article_index = articles.index(article_entry)
    if article_index == 0 and articles_num > 0:
        prev_article = articles[1]
    elif article_index > 0 and article_index+1 != articles_num:
        next_article = articles[article_index-1]
        prev_article = articles[article_index+1]
    elif article_index > 0 and article_index+1 == articles_num:
        next_article = articles[article_index-1]
    return prev_article, next_article


def parse_article_content(content):
    """
    Parse the article content
    :param string content:
    :return:
    """
    html = markdown2.markdown(content)
    return html