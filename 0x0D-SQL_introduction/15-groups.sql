-- lists number of records with equal scores
SELECT
	score, count(*)
AS NUMBER FROM
	second_table
GROUP BY
	score
ORDER BY
	score DESC;
