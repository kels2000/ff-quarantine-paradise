
from flask import Blueprint

from voyager.views import index
from voyager.views import sailors
from voyager.views import employees
from voyager.views import voyages
from voyager.views import reservations
from voyager.views import availableRooms
from voyager.views import hotelGuests

blueprint = Blueprint('views', __name__)
index.views(blueprint)
sailors.views(blueprint)
employees.views(blueprint)
voyages.views(blueprint)
reservations.views(blueprint)
availableRooms.views(blueprint)
hotelGuests.views(blueprint)
def init_app(app):
    app.register_blueprint(blueprint)
    app.add_url_rule('/', endpoint='index')

