from collections import namedtuple

from flask import g
from flask import escape
from flask import render_template
from flask import request

from voyager.db import get_db, execute
from voyager.validate import validate_field, render_errors
from voyager.validate import NAME_RE, INT_RE, DATE_RE

def reservations(conn):
    return execute(conn, "SELECT r.roomNumber, r.dateOut, r.dateIn, r.resID, r.guestID FROM Reservations AS r")
    
def views(bp):

    @bp.route("/reservations")
    def _get_all_reservations():
        with get_db() as conn:
            rows = reservations(conn)
        print(rows)
        return render_template("table.html", name="Reservations", rows=rows)
