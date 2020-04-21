from collections import namedtuple

from flask import g
from flask import escape
from flask import render_template
from flask import request

from voyager.db import get_db, execute
from voyager.validate import validate_field, render_errors
from voyager.validate import NAME_RE, INT_RE, DATE_RE

def employees(conn):
    return execute(conn, "SELECT distinct e.eid, e.name, e.phone_num, e.address, e.email, e.pos, e.salary, e.clock_in, e.clock_out FROM Employees AS e ORDER BY e.eid desc;")

def employeeInfo(conn, eid):
    return execute(conn, f"SELECT e.name, e.phone_num, e.address, e.email, e.pos, e.salary, e.clock_in, e.clock_out FROM Employees as e where e.eid = '{eid}'")

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
            return render_template("table.html", name='ID: ' + eid, rows=rows)
