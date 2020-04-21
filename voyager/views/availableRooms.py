from collections import namedtuple

from flask import g
from flask import escape
from flask import render_template
from flask import request

from voyager.db import get_db, execute
from voyager.validate import validate_field, render_errors
from voyager.validate import NAME_RE, INT_RE, DATE_RE

def availableRooms(conn):
    return execute(conn, "SELECT a.roomType, a.roomNumber, a.roomPrice FROM AvailableRooms AS a")
    
def views(bp):

    @bp.route("/availableRooms")
    def _get_all_available():
        with get_db() as conn:
            rows = availableRooms(conn)
        return render_template("table.html", name="availableRooms", rows=rows)
