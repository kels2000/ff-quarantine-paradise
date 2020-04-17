
from voyager.db import get_db
import csv, sqlite3

def main():
    with get_db() as conn:
        with open('sqlite-schema.sql') as f:
            conn.executescript(f.read())
        conn.commit()
        with open('test-data.sql') as f:
            conn.executescript(f.read())
        conn.commit()

        cur = conn.cursor()
        with open('/Users/kelsifulton/Downloads/employees.csv','rt') as fin: # `with` statement available in 2.5+
        # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin) # comma is default delimiter
            to_db = [(i['eid'], i['name'], i['phone_num'], i['birthdate'], i['address'], i['email'], i['pos'], i['salary'], i['clock_in'], i['clock_out']) for i in dr]

        cur.executemany("INSERT INTO Employees (eid, name, phone_num, birthdate, address, email, pos, salary, clock_in, clock_out) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
        conn.commit()
        conn.close()

if __name__ == '__main__':
    main()
