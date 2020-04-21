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
  address TEXT,
  email TEXT,
  pos TEXT,
  salary INTEGER,
  clock_in TEXT,
  clock_out TEXT
);

CREATE TABLE IF NOT EXISTS Reservations (
  roomNumber INTEGER,
   guestID INTEGER,
  dateIn DATETIME,
  dateOut DATETIME,
  resID INTEGER PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS AvailableRooms (
  roomType TEXT,
  roomNumber INTEGER PRIMARY KEY,
  roomPrice INTEGER
);


CREATE TABLE IF NOT EXISTS HotelGuests (
  gid INTEGER PRIMARY KEY, 
  gName TEXT, 
  phone TEXT, 
  bday TEXT, 
  homeAddress TEXT, 
  email TEXT
);
-- CREATE TABLE IF NOT EXISTS Voyages (
--   sid INTEGER NOT NULL,
--   bid INTEGER NOT NULL,
--   date_of_voyage DATE NOT NULL,
--   PRIMARY KEY(sid, bid, date_of_voyage)
-- );
