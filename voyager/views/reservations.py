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
    return execute(conn, f"SELECT Reservations.roomNumber, Reservations.dateIn, Reservations.dateOut, Reservations.resID, Reservations.guestID FROM Reservations INNER JOIN HotelGuests ON Reservations.guestID = HotelGuests.gid WHERE '{guestname}' = HotelGuests.gName")
def views(bp):

    @bp.route("/reservations")
    def _get_all_reservations():
        with get_db() as conn:
            rows = reservations(conn)
        return render_template("table.html", name="Reservations", rows=rows)

    @bp.route("/reservations/myReservations", methods=["POST", "GET"])
    def _getMyRes():
        with get_db() as conn: 
            if(request.method == "GET"):
                return render_template("/myReservations.html")
            if(request.method == "POST"): 
                guestname = request.form['guestname']
                rows = getMyRes(conn, guestname)
        return render_template("table.html", name="Your Reservations", rows=rows)