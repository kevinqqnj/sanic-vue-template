"""
Global Flask Application Setting

See `.flaskenv` for default settings.
 """

import os


class Config(object):
    # If not set fall back to production for safety
    SANIC_ENV =  os.getenv('SANIC_ENV', 'production')
    DEBUG = bool(os.getenv('DEBUG', False))
    # Set SANIC_SECRET on your production Environment
    SECRET_KEY = os.getenv('SANIC_SECRET', 'Secret')

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, 'dist')

    if not os.path.exists(DIST_DIR):
        raise Exception(
            'DIST_DIR not found: {}'.format(DIST_DIR))

