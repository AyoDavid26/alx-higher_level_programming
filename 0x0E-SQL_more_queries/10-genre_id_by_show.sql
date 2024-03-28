-- Lists all shows contained in hbtn_0d_tvshows
-- Records are sorted by ascending tv_show.title and tv_show_genres.genre.id
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
	INNER JOIN `tv_show_genres` AS g
	ON S.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
