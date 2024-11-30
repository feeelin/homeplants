DROP TABLE IF EXISTS places;
DROP TABLE IF EXISTS plants;
DROP TABLE IF EXISTS plants_info;
DROP TABLE IF EXISTS plants_classes;
DROP TABLE IF EXISTS rooms;

CREATE TABLE plants_classes (
    id SERIAL,
    class_name TEXT NOT NULL,
    soil_type TEXT NOT NULL,
    replanting_time TEXT NOT NULL,
    feed_type TEXT NOT NULL,
    feed_time TEXT NOT NULL,
    winter_water_regime TEXT NOT NULL,
    summer_water_regime TEXT NOT NULL,

    PRIMARY KEY (id)
);

CREATE TABLE plants_info (
    id SERIAL,
    plant_name TEXT NOT NULL,
    class_id INTEGER,

    PRIMARY KEY (id),
    FOREIGN KEY (class_id)
        REFERENCES plants_classes (id)
);

CREATE TABLE plants (
    id SERIAL,
    info_id INTEGER,
    AGE INTEGER DEFAULT 0,

    PRIMARY KEY (id),
    FOREIGN KEY (info_id)
        REFERENCES plants_info (id)
);

CREATE TABLE rooms (
    id SERIAL,
    places_count INTEGER NOT NULL,
    room_type TEXT NOT NULL,

    PRIMARY KEY (id)
);

CREATE TABLE places (
    id SERIAL,
    room_id INTEGER,
    plant_id INTEGER,

    PRIMARY KEY (id),
    FOREIGN KEY (room_id)
        REFERENCES rooms (id)
        ON DELETE CASCADE,
    FOREIGN KEY (plant_id)
        REFERENCES plants (id)
        ON DELETE SET NULL
);

INSERT INTO plants_classes (class_name, soil_type, replanting_time, feed_type, feed_time, winter_water_regime, summer_water_regime)
VALUES ('Деревья', 'Питательная смесь', 'Весна', 'Минеральная', '1 раз в месяц', 'Умеренный', 'Легкий')

INSERT INTO plants_info (plant_name, class_id)
VALUES ('Фикус Бенджамина', 1)

INSERT INTO plants (info_id, age)
VALUES (2, 5)

SELECT * FROM plants
JOIN plants_info
ON plants.id = plants_info.id
JOIN plants_classes
ON plants_classes.id = plants_info.class_id
WHERE 'plants.id' = 2;