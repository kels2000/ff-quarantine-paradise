CREATE TABLE IF NOT EXISTS Sailors (
  sid INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  age INTEGER,
  experience INTEGER -- years of experience
);

CREATE TABLE IF NOT EXISTS Employees (
  eid INTEGER PRIMARY KEY,
  name TEXT,
  phone_num TEXT,
  birthdate DATE,
  address TEXT,
  email TEXT,
  pos TEXT,
  salary INTEGER,
  clock_in DATETIME,
  clock_out DATETIME
);

CREATE TABLE IF NOT EXISTS Reservations (
  roomNumber INTEGER PRIMARY KEY,
   guestID INTEGER PRIMARY KEY,
  dateIn DATETIME,
  dateOut DATETIME
);

CREATE TABLE IF NOT EXISTS AvailableRooms (
  roomNumber INTEGER PRIMARY KEY,
  roomPrice INTEGER,
  roomType TEXT,
);
-- CREATE TABLE IF NOT EXISTS Voyages (
--   sid INTEGER NOT NULL,
--   bid INTEGER NOT NULL,
--   date_of_voyage DATE NOT NULL,
--   PRIMARY KEY(sid, bid, date_of_voyage)
-- );
