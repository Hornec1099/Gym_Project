DROP TABLE bookings;
DROP TABLE activities;
DROP TABLE members;

CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT
);

CREATE TABLE activities(
    id SERIAL PRIMARY KEY,
    name_of_activity VARCHAR(255),
    day_of DATE,
    time_of INT,
    description VARCHAR(255)
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    activity_id INT REFERENCES activities(id) ON DELETE CASCADE,
    member_id INT REFERENCES members(id) ON DELETE CASCADE
);