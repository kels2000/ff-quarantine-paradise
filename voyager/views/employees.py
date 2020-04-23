from collections import namedtuple

from flask import g
from flask import escape
from flask import render_template
from flask import request
from flask import redirect
from flask import flash

from voyager.db import get_db, execute
from voyager.validate import validate_field, render_errors
from voyager.validate import NAME_RE, INT_RE, DATE_RE

def employees(conn):
    return execute(conn, "SELECT distinct e.eid, e.name, e.phone_num, e.address, e.email, e.pos, e.salary, e.clock_in, e.clock_out FROM Employees AS e ORDER BY e.eid desc;")

def employeeInfo(conn, eid):
    return execute(conn, f"SELECT e.name, e.phone_num, e.address, e.email, e.pos, e.salary, e.latest_clock_in, e.latest_clock_out FROM Employees as e where e.eid = '{eid}'")

def employeeClockIn(conn, eid, clock_in):
    return execute(conn, f"UPDATE Employees SET latest_clock_in = '{clock_in}' WHERE eid = '{eid}'")

def employeeClockOut(conn, eid, clock_out):
    return execute(conn, f"UPDATE Employees SET latest_clock_out = '{clock_out}' WHERE eid = '{eid}'")

def views(bp):
    @bp.route("/employees")
    def _employees():
        with get_db() as conn:
            rows = employees(conn)
        return render_template("table.html", name="employees", rows=rows)

    @bp.route("/employees/info", methods=["GET", "POST"])
    def employeeInfoPage():
        if request.method == 'POST':
            with get_db() as conn:
                eid = request.form["employee-info"]
                rows = employeeInfo(conn, eid)
            return render_template("employees.html", name='ID: ' + eid, rows=rows)

    @bp.route("/employees/info/in", methods=["GET", "POST"])
    def employeeInPage():
        if request.method == 'POST':
            with get_db() as conn:
                eid = request.form["employee-info"]
                clock_in = request.form['employee-in']
                rows = employeeClockIn(conn, eid, clock_in)
            flash('Clocked In!')
            return redirect('/')

    @bp.route("/employees/info/out", methods=["GET", "POST"])
    def employeeOutPage():
        if request.method == 'POST':
            with get_db() as conn:
                eid = request.form["employee-info"]
                clock_out = request.form['employee-out']
                rows = employeeClockOut(conn, eid, clock_out)
            flash('Clocked Out!')
            return redirect('/')
