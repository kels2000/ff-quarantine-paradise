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
def getMyRes(conn, guestname): 
    return execute(conn, f"SELECT r.roomNumber, r.dateIn, r.dateOut, r.resID, r.guestID FROM Reservations AS r INNER JOIN HotelGuests ON Reservations.guestID = HotelGuest.gid WHERE HotelGuest.gName = '{guestname}'")
def views(bp):

    @bp.route("/reservations")
    def _get_all_reservations():
        with get_db() as conn:
            rows = reservations(conn)
        return render_template("table.html", name="Reservations", rows=rows)

    @bp.route("/reservations/myReservations", methods=["POST", "GET"])
    def _getMyRes():
        with get_db() as conn: 
            guestname = request.form['guestname']
            rows = getMyRes(conn, guestname)
        return render_template("myReservations.html", name="Reservation", rows=rows)