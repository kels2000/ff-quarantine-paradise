from collections import namedtuple

from flask import render_template
from flask import request

from voyager.db import get_db, execute

def views(bp):
    @bp.route("/voyages")
    def _voyages():
        return 'not implemented'
