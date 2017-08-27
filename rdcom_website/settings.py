import os

# Thanks to: https://stackoverflow.com/questions/14825787/flask-how-to-read-a-file-in-application-root

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')
ARTICLES_PATH = os.path.join(APP_ROOT, 'contents')
ARTICLES_METADATA_LINES = 2
