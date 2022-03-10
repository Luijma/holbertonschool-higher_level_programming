-- lists all shows and all genres linked to that show
SELECT
	tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_shows_genres
ON tv_show_genres.show_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
