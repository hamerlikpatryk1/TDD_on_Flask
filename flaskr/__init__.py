import os

from flask import Flask

from . import db

""" 
Args: 
create_app -> create and configure the app

if test_config is None -> load the instance config, if it exists, when not testing
else -> load the test config if passed in

test (try) ->  ensure the instance folder exists

create -> a simple page that says hello
"""

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return "Hello World"
    
    db.init_app(app)

    return app
