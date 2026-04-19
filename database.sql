CREATE DATABASE event_db;
USE event_db;

-- EVENTS TABLE
CREATE TABLE Events (
    event_id INT PRIMARY KEY AUTO_INCREMENT,
    event_name VARCHAR(100),
    date DATE,
    location VARCHAR(100),
    organizer VARCHAR(100)
);

-- PARTICIPANTS TABLE
CREATE TABLE Participants (
    participant_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15)
);

-- REGISTRATIONS TABLE
CREATE TABLE Registrations (
    reg_id INT PRIMARY KEY AUTO_INCREMENT,
    event_id INT,
    participant_id INT,
    reg_date DATE,
    FOREIGN KEY (event_id) REFERENCES Events(event_id),
    FOREIGN KEY (participant_id) REFERENCES Participants(participant_id)
);
