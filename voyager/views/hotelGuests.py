from collections import namedtuple

from flask import g
from flask import escape
from flask import render_template
from flask import request

from voyager.db import get_db, execute
from voyager.validate import validate_field, render_errors
from voyager.validate import NAME_RE, INT_RE, DATE_RE

def hotelGuests(conn):
    return execute(conn, "SELECT h.gName, h.phone, h.bday, h.homeAddress, h.email FROM HotelGuests AS h")
    
def views(bp):

    @bp.route("/hotelGuests")
    def _get_all_guests():
        with get_db() as conn:
            rows = hotelGuests(conn)
        return render_template("table.html", name="hotelGuests", rows=rows)
