-- Query all the cities in the hbtn_0d_usa database

SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states
   WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
