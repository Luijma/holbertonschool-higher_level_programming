-- lists number of records with equal scores
SELECT score, count(*)
AS number FROM
	second_table
GROUP BY
	score
ORDER BY
	score DESC;
