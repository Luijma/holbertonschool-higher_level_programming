-- lists all cities of california in hbtn_0d_usa
SELECT
	cities
FROM
	states
WHERE
	name='California'
ORDER BY
	cities.id ASC;
