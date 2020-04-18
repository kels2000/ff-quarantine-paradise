
from collections import namedtuple

from flask import render_template
from flask import request
from flask import escape

from voyager.db import get_db, execute

def employees(conn):
    return execute(conn, "SELECT e.eid, e.name, e.phone_num, e.address, e.email, e.pos, e.salary, e.clock_in, e.clock_out FROM Employees AS e ORDER BY e.eid desc;")

def views(bp):
    @bp.route("/employees")
    def _employees():
        with get_db() as conn:
            rows = employees(conn)
        return render_template("table.html", name="employees", rows=rows)
