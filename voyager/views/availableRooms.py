from collections import namedtuple

from flask import g
from flask import escape
from flask import render_template
from flask import request
from flask import redirect

from voyager.db import get_db, execute
from voyager.validate import validate_field, render_errors
from voyager.validate import NAME_RE, INT_RE, DATE_RE

def availableRooms(conn):
    return execute(conn, "SELECT a.roomType, a.roomNumber, a.roomPrice FROM AvailableRooms AS a")

def availableOnDate(conn, checkin, checkout):
    return execute(conn, f"SELECT DISTINCT Reservations.roomNumber, AvailableRooms.roomType, AvailableRooms.roomPrice FROM AvailableRooms INNER JOIN Reservations ON Reservations.roomNumber = AvailableRooms.roomNumber WHERE '{checkin}' > Reservations.dateOut AND '{checkout}' > Reservations.dateOut OR '{checkin}' < Reservations.dateIn AND '{checkout}' < Reservations.dateIn")
def views(bp):

    @bp.route("/availableRooms")
    def _get_all_available():
        with get_db() as conn:
            rows = availableRooms(conn)
        return render_template("table.html", name="availableRooms", rows=rows)

    @bp.route("/availableRooms/availableOnDate", methods=["POST", "GET"])
    def _show_available_rooms_on_date():
        with get_db() as conn:
            if(request.method == "GET"):
                return render_template("/availableRooms.html")
            if(request.method == "POST"): 
                checkin = request.form['check-in-date']
                checkout = request.form['check-out-date']
                rows = availableOnDate(conn, checkin, checkout) 
            return render_template("table.html", name="availableRoomsOnDate", rows=rows)

        

