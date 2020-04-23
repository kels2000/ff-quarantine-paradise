
DROP TABLE Employees;

CREATE TABLE IF NOT EXISTS Employees (
  eid INTEGER PRIMARY KEY,
  name TEXT,
  phone_num TEXT,
  address TEXT,
  email TEXT,
  pos TEXT,
  salary INTEGER,
  latest_clock_in TEXT,
  latest_clock_out TEXT
);

CREATE TABLE IF NOT EXISTS Reservations (
  roomNumber INTEGER,
  guestID INTEGER,
  dateIn DATETIME,
  dateOut DATETIME,
  resID INTEGER PRIMARY KEY AUTOINCREMENT
);


CREATE TABLE IF NOT EXISTS AvailableRooms (
  roomType TEXT,
  roomNumber INTEGER PRIMARY KEY,
  roomPrice INTEGER
);

CREATE TABLE IF NOT EXISTS RoomService (
  item TEXT PRIMARY KEY,
  price INTEGER
);


CREATE TABLE IF NOT EXISTS HotelGuests (
  gid INTEGER PRIMARY KEY, 
  gName TEXT, 
  phone TEXT, 
  bday TEXT, 
  homeAddress TEXT, 
  email TEXT
);

