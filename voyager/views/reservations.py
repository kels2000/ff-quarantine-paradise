from collections import namedtuple

from flask import g
from flask import escape
from flask import render_template
from flask import request
from flask import redirect

from voyager.db import get_db, execute
from voyager.validate import validate_field, render_errors
from voyager.validate import NAME_RE, INT_RE, DATE_RE

def reservations(conn):
    return execute(conn, "SELECT r.roomNumber, r.dateOut, r.dateIn, r.resID, r.guestID FROM Reservations AS r")
def getMyRes(conn, guestname): 
    return execute(conn, f"SELECT Reservations.roomNumber, Reservations.dateIn, Reservations.dateOut, Reservations.resID, Reservations.guestID, Reservations.bill FROM Reservations INNER JOIN HotelGuests ON Reservations.guestID = HotelGuests.gid WHERE '{guestname}' = HotelGuests.gName")
def menu(conn):
    return execute(conn, f"SELECT m.item, m.price FROM Menu as m")
def roomService(conn, resID, item):
    return execute(conn, f"UPDATE Reservations SET bill = bill + (SELECT Menu.price FROM Menu WHERE Menu.item = '{item}') WHERE Reservations.resID = '{resID}'")
def viewBill(conn, resID):
    return execute(conn, f"select gname, resID, bill from HotelGuests inner join Reservations on HotelGuests.gid = Reservations.guestid where resID = '{resID}'")
    
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
    
    @bp.route("/hotelGuests/roomService", methods=["POST", "GET"])
    def _roomService():
        with get_db() as conn: 
            if(request.method == "GET"):
                rows = menu(conn)
                return render_template("roomService.html", name="Order Room Service!", rows=rows)
            if(request.method == "POST"): 
                resID  = request.form['res_id']
                item = request.form['item']
                rows = roomService(conn, resID, item)
        return redirect('/')

    @bp.route("/hotelGuests/bill", methods=["GET", "POST"])
    def billPage():
        if(request.method == "GET"):
                return render_template("viewBill.html", name="View Your Bill")
        if request.method == 'POST':
            with get_db() as conn:
                resID = request.form["res_id"]
                rows = viewBill(conn, resID)
            return render_template("table.html", name='Your Bill', rows=rows)