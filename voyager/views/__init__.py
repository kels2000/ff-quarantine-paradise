
from flask import Blueprint

from voyager.views import index
from voyager.views import sailors
from voyager.views import employees
from voyager.views import voyages

blueprint = Blueprint('views', __name__)
index.views(blueprint)
sailors.views(blueprint)
employees.views(blueprint)
voyages.views(blueprint)

def init_app(app):
    app.register_blueprint(blueprint)
    app.add_url_rule('/', endpoint='index')

