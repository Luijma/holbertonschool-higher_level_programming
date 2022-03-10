-- uses database to list all genres of the show Dexter
SELECT
	tv_genres.name
FROM
	tv_genres
INNER JOIN
	tv_show_genres
INNER JOIN
	tv_shows
ON
	tv_shows.title = "Dexter"
AND tv_show_genres.show_id = tv_shows.id
AND tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_genres.name ASC;
