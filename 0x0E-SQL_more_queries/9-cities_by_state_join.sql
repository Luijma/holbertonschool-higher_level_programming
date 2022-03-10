-- lists all cities contained in databaes hbtn_0d_usa
SELECT
	cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.id = states.id
ORDER BY cities.id ASC;
